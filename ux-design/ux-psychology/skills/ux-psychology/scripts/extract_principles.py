#!/usr/bin/env python3
"""
Generates markdown reference files from growth_design_psychology_parsed.json.
Creates 4 category files + 1 scenario-index.md in the references/ directory.
"""

import json
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REFERENCES_DIR = SCRIPT_DIR.parent / "references"
# Source JSON — adjust path if needed
SOURCE_JSON = Path(__file__).resolve().parents[4] / "Mystery School - Make art not content" / "src" / "output" / "growth_design_psychology_parsed.json"

CATEGORY_FILES = {
    "Information": "information-biases.md",
    "Meaning": "meaning-biases.md",
    "Time": "time-biases.md",
    "Memory": "memory-biases.md",
}

CATEGORY_DESCRIPTIONS = {
    "Information": "Users filter out a lot of the information that they receive, even when it could be important.",
    "Meaning": "When users try to give sense to information, they make stories and assumptions to fill the gaps.",
    "Time": "Users are busy so they look for shortcuts and jump to conclusions quickly.",
    "Memory": "Users try to remember what's most important, but their brain prefers some elements over others.",
}

CATEGORY_EMOJIS = {
    "Information": "\U0001f648",  # 🙈
    "Meaning": "\U0001f52e",      # 🔮
    "Time": "\u23f0",             # ⏰
    "Memory": "\U0001f4be",       # 💾
}


def format_bias(bias: dict) -> str:
    """Format a single bias/principle as markdown."""
    emoji = bias.get("emoji", "")
    title = bias["title"]
    one_liner = bias["description"]
    is_coming_soon = bias.get("is_coming_soon", False)
    definition = bias.get("definition", "").strip()
    examples = bias.get("examples", [])
    checklist = bias.get("checklist", [])
    sources = bias.get("sources", [])

    header = f"## {emoji} {title}".strip() if emoji else f"## {title}"
    lines = [header]
    lines.append(f"**One-liner:** {one_liner}")

    if is_coming_soon or not definition:
        # Coming soon — use one-liner as definition + generic tip
        lines.append(f"**Definition:** {one_liner}.")
        lines.append(f"**Tip:** Consider how {title.lower()} affects your users' experience. Audit your current design for opportunities to leverage this principle.")
    else:
        lines.append(f"**Definition:** {definition}")

        # Product example — first example text
        if examples:
            example_text = examples[0].get("text", "").strip()
            if example_text:
                lines.append(f"**Product Example:** {example_text}")

        # Tip — from checklist or derived from definition
        if checklist:
            # Join checklist items as a single tip
            tip_items = [item.strip() for item in checklist if item.strip()]
            lines.append(f"**Tip:** {' '.join(tip_items)}")
        elif examples and len(examples) > 1:
            # Use second example as additional insight
            alt = examples[-1].get("text", "").strip()
            if alt:
                lines.append(f"**Tip:** {alt}")
        else:
            lines.append(f"**Tip:** Apply {title} thoughtfully in your design. Test with real users to validate the effect.")

    # Sources
    if sources:
        source_links = []
        for s in sources[:3]:  # Max 3 sources
            text = s.get("text", "Link")
            url = s.get("url", "")
            if url:
                source_links.append(f"[{text}]({url})")
            else:
                source_links.append(text)
        lines.append(f"**Sources:** {', '.join(source_links)}")

    return "\n".join(lines)


def generate_category_file(category: dict, filename: str):
    """Generate a category markdown file."""
    name = category["name"]
    emoji = CATEGORY_EMOJIS.get(name, "")
    description = CATEGORY_DESCRIPTIONS.get(name, category.get("description", ""))
    biases = category["biases"]

    lines = [
        f"# {emoji} {name} — {len(biases)} Principles",
        f"> {description}",
        "",
    ]

    for bias in biases:
        lines.append(format_bias(bias))
        lines.append("")  # Blank line between entries
        lines.append("---")
        lines.append("")

    filepath = REFERENCES_DIR / filename
    filepath.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✓ {filename}: {len(biases)} principles")


def generate_scenario_index():
    """Generate the scenario-to-principles lookup table."""
    content = """# Scenario Index — UX Psychology Principles

> Quick lookup: find the right principles for your UX scenario.
> Read this file first, then dive into the relevant category file for full details.

## How to use
1. Find your scenario below
2. Note the 3-6 recommended principles
3. Open the corresponding category file (Information, Meaning, Time, or Memory)
4. Apply selectively — not every principle fits every context

---

## Onboarding
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Progressive Disclosure | Information | Don't overwhelm new users — reveal features gradually |
| Cognitive Load | Information | Reduce mental effort in first-time experience |
| Aha! moment | Meaning | Help users discover core value fast |
| Commitment & Consistency | Time | Small first steps lead to bigger engagement |
| Zeigarnik Effect | Memory | Incomplete tasks pull users back |
| Priming | Information | Set expectations before key decisions |

## Pricing & Monetisation
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Anchoring Bias | Information | First price seen frames all others |
| Decoy Effect | Information | Third option steers choice toward target |
| Framing | Information | How you present price changes perception |
| Centre-Stage Effect | Information | Middle option gets chosen more often |
| Loss Aversion | Time | Fear of losing outweighs desire to gain |
| Cashless Effect | Time | Digital payments feel less "real" |

## Checkout & Conversion
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Hick's Law | Information | Fewer options = faster decisions |
| Fitts's Law | Information | Make CTAs large and easy to reach |
| Default Bias | Time | Pre-selected options stick |
| Social Proof | Meaning | Others' actions validate the purchase |
| Nudge | Information | Subtle cues guide without forcing |
| Spark Effect | Information | Low effort triggers action |

## Engagement & Retention
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Variable Reward | Meaning | Unpredictable rewards keep users coming back |
| Investment Loops | Time | User effort increases perceived value |
| Goal Gradient Effect | Meaning | Closer to goal = higher motivation |
| Internal Trigger | Memory | Habits form when emotions cue product use |
| Peak-End Rule | Memory | End on a high note for lasting impression |
| Sunk Cost Effect | Time | Past investment keeps users engaged |

## Forms & Input
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Cognitive Load | Information | Break complex forms into digestible chunks |
| Chunking | Memory | Group related fields together |
| Recognition Over Recall | Memory | Show options instead of blank fields |
| Tesler's Law | Information | Don't over-simplify at the user's expense |
| Provide Exit Points | Memory | Let users save progress and come back |
| Feedback Loop | Information | Confirm each step with clear feedback |

## Navigation & Information Architecture
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Mental Model | Meaning | Match structure to user expectations |
| Signifiers | Information | Elements must communicate their function |
| Law of Proximity | Information | Group related items spatially |
| Familiarity Bias | Meaning | Use conventions users already know |
| Visual Hierarchy | Information | Guide the eye to what matters most |
| Miller's Law | Meaning | Keep nav items within 7±2 limit |

## Trust & Credibility
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Social Proof | Meaning | Reviews and testimonials build trust |
| Authority Bias | Meaning | Expert endorsements carry weight |
| Noble Edge Effect | Meaning | Social responsibility increases loyalty |
| Halo Effect | Meaning | One positive trait colors overall perception |
| Reciprocity | Meaning | Give value before asking for commitment |

## Notifications & Re-engagement
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| External Trigger | Information | Prompt action with timely notifications |
| Curiosity Gap | Meaning | Tease enough to make users want more |
| Fresh Start Effect | Meaning | New beginnings motivate action |
| Reactance | Time | Too many notifications trigger rejection |
| Internal Trigger | Memory | Build emotional associations with your product |

## Empty States & Errors
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Feedforward | Meaning | Show users what to expect before they act |
| Discoverability | Time | Make next steps obvious in empty states |
| Framing | Information | Frame errors as opportunities, not failures |
| Storytelling Effect | Memory | Use narrative to make empty states engaging |
| Delighters | Memory | Turn error moments into brand moments |

## Dashboard & Data Visualisation
| Principle | Category | Why it matters |
|-----------|----------|----------------|
| Chunking | Memory | Group data into meaningful clusters |
| Visual Hierarchy | Information | Most important metrics should pop first |
| Miller's Law | Meaning | Don't exceed working memory limits |
| Law of Prägnanz | Meaning | Simplest interpretation wins |
| Contrast | Information | Use visual weight to direct attention |
| Attentional Bias | Information | Users focus on what matches their current goals |
"""
    filepath = REFERENCES_DIR / "scenario-index.md"
    filepath.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"  ✓ scenario-index.md: 10 scenarios")


def main():
    print(f"Source: {SOURCE_JSON}")
    if not SOURCE_JSON.exists():
        print(f"ERROR: Source JSON not found at {SOURCE_JSON}")
        return

    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)

    with open(SOURCE_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"\nGenerating reference files in {REFERENCES_DIR}/\n")

    total = 0
    for category in data["categories"]:
        name = category["name"]
        filename = CATEGORY_FILES.get(name)
        if filename:
            generate_category_file(category, filename)
            total += len(category["biases"])

    generate_scenario_index()

    print(f"\nDone! {total} principles across {len(CATEGORY_FILES)} categories + scenario index.")


if __name__ == "__main__":
    main()
