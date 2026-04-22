"""Open a new Mail.app draft with subject, recipients, and body pre-filled.

Standalone helper for product-management. No external dependencies — only
Python stdlib + macOS `osascript`. Inspired by the logic of beeper's
mail_client.py but does NOT import from it; this project stays autonomous.

Safety contract:
- NEVER calls AppleScript `send` on any message.
- The only side effect is opening a compose window (`visible:true`). The user
  reviews and sends manually.

Two body modes:
- text (default): plain text via the AppleScript `content` property. Reliable,
  no Accessibility permission required.
- html: sets the clipboard to HTML, then pastes into the compose body via
  System Events. Requires "Accessibility" permission for the terminal /
  Claude Code in System Settings → Privacy & Security → Accessibility.

Usage (CLI):
    python tools/mail_draft.py --subject "Récap semaine du 21 avril" \
        --to alice@galigeo.com --to bob@galigeo.com \
        --body-file /tmp/cr.md --html
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

DEFAULT_TIMEOUT = 30


class MailDraftError(RuntimeError):
    pass


def _run_osascript(script: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Run an AppleScript via osascript stdin."""
    try:
        result = subprocess.run(
            ["osascript", "-"],
            input=script,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise MailDraftError(f"osascript timed out after {timeout}s")
    except FileNotFoundError:
        raise MailDraftError("osascript not found — is this macOS?")

    if result.returncode != 0:
        raise MailDraftError(f"osascript failed: {result.stderr.strip()}")
    return result.stdout


def _applescript_escape(s: str) -> str:
    """Escape a Python string so it can be embedded inside an AppleScript string literal."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def _set_html_clipboard(html: str) -> None:
    """Put rich-text content on the macOS clipboard so Cmd+V in Mail preserves formatting.

    The `«class HTML»` AppleScript flavor is NOT reliably recognized by Mail.app
    on recent macOS. Instead we convert HTML → RTF via `textutil` and put the
    RTF on the clipboard via `pbcopy -Prefer rtf`. Mail.app pastes RTF as
    formatted text.
    """
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(html)
        html_path = fh.name
    rtf_path = html_path.replace(".html", ".rtf")
    try:
        subprocess.run(
            ["textutil", "-convert", "rtf", html_path, "-output", rtf_path],
            check=True,
            capture_output=True,
            timeout=10,
        )
        subprocess.run(
            ["bash", "-c", f"cat {rtf_path} | pbcopy -Prefer rtf"],
            check=True,
            capture_output=True,
            timeout=10,
        )
    except subprocess.CalledProcessError as e:
        raise MailDraftError(f"Failed to put RTF on clipboard: {e.stderr.decode() if e.stderr else e}")


def open_new_draft(
    subject: str,
    body: str,
    to: list[str] | None = None,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    html: bool = False,
    paste_delay: float = 0.6,
) -> None:
    """Open a new Mail.app compose window with fields pre-filled.

    NEVER sends. The window stays open for manual review.

    Args:
        subject: email subject line.
        body: plain text (html=False) or HTML (html=True) body content.
        to: list of recipient email addresses.
        cc: list of cc email addresses.
        bcc: list of bcc email addresses.
        html: if True, use the HTML clipboard-paste path (requires Accessibility).
        paste_delay: seconds to wait between window creation and Cmd-V when html=True.
    """
    to = to or []
    cc = cc or []
    bcc = bcc or []

    subject_esc = _applescript_escape(subject)

    def _recipients_block(kind: str, addresses: list[str]) -> str:
        # kind: "to recipient" | "cc recipient" | "bcc recipient"
        lines = []
        for addr in addresses:
            addr_esc = _applescript_escape(addr)
            lines.append(
                f'        make new {kind} at end of {kind}s with properties {{address:"{addr_esc}"}}'
            )
        return "\n".join(lines)

    to_block = _recipients_block("to recipient", to)
    cc_block = _recipients_block("cc recipient", cc)
    bcc_block = _recipients_block("bcc recipient", bcc)

    if html:
        # Put HTML on clipboard first, then create compose. Navigate focus from
        # À → Cc → Objet → Body via Tab (3 tabs), then paste.
        _set_html_clipboard(body)
        script = f'''
tell application "Mail"
    activate
    set newMsg to make new outgoing message with properties {{subject:"{subject_esc}", visible:true}}
    tell newMsg
{to_block}
{cc_block}
{bcc_block}
    end tell
end tell

delay {paste_delay}

tell application "System Events"
    tell process "Mail"
        set frontmost to true
        delay 0.3
        -- Tab from "À" → "Cc" → "Objet" → body
        keystroke tab
        delay 0.1
        keystroke tab
        delay 0.1
        keystroke tab
        delay 0.2
        keystroke "v" using command down
    end tell
end tell
'''
    else:
        body_esc = _applescript_escape(body)
        script = f'''
tell application "Mail"
    activate
    set newMsg to make new outgoing message with properties {{subject:"{subject_esc}", content:"{body_esc}", visible:true}}
    tell newMsg
{to_block}
{cc_block}
{bcc_block}
    end tell
end tell
'''

    _run_osascript(script, timeout=DEFAULT_TIMEOUT)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _main() -> int:
    parser = argparse.ArgumentParser(description="Open a Mail.app draft with fields pre-filled (never sends).")
    parser.add_argument("--subject", required=True)
    parser.add_argument("--to", action="append", default=[], help="Recipient (repeatable)")
    parser.add_argument("--cc", action="append", default=[])
    parser.add_argument("--bcc", action="append", default=[])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--body", help="Body content (plain text or HTML depending on --html)")
    group.add_argument("--body-file", help="Read body content from file")
    parser.add_argument("--html", action="store_true", help="Treat body as HTML and paste via clipboard")
    args = parser.parse_args()

    body = args.body if args.body is not None else Path(args.body_file).read_text(encoding="utf-8")

    try:
        open_new_draft(
            subject=args.subject,
            body=body,
            to=args.to,
            cc=args.cc,
            bcc=args.bcc,
            html=args.html,
        )
    except MailDraftError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(_main())
