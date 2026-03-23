# Checklist Power User Claude Code

## Score actuel : 7.5/10 — Avancé

*Audit du 2026-03-23*

| Domaine | Score | Commentaire |
|---------|-------|-------------|
| CLAUDE.md & instructions | 9/10 | Projet + global, personas, glossaire, anti-patterns |
| Permissions & sécurité | 8/10 | Whitelist granulaire, approche défensive |
| Skills custom | 9/10 | UX (9 fichiers knowledge) + TouchDesigner dual-mode |
| Plugins & LSP | 8/10 | Pyright, TS, Playwright, frontend-design |
| MCP & intégrations | 7/10 | Figma + Atlassian + Notion, peu de MCP globaux |
| Hooks | 5/10 | Notifications uniquement, pas de hooks Edit/Write |
| Memory system | 2/10 | Non utilisé — gros potentiel perdu |
| Keybindings | 0/10 | Aucun configuré |
| Effort level dynamique | 4/10 | Fixé à "medium", pas de switching par tâche |
| Subagents & parallélisme | 7/10 | Documenté mais usage réel à confirmer |

**Axes prioritaires** : Memory system, keybindings, hooks post-edit

---

## Setup de base
- [x] CLAUDE.md projet avec contexte, personas, glossaire
- [x] CLAUDE.md global (`~/.claude/CLAUDE.md`) avec workflow et principes
- [x] Permissions granulaires (whitelist, pas de blanket access)
- [x] Plugins LSP activés (Pyright, TypeScript)
- [x] Extended thinking activé (`alwaysThinkingEnabled`)
- [x] Hook de notification macOS

## Intégrations & MCP
- [x] MCP Figma bridge (projet)
- [x] MCP Atlassian (Jira/Confluence)
- [x] MCP Notion
- [x] MCP Next.js devtools (global)
- [ ] MCP GitHub (alternative à `gh` CLI, plus riche en contexte)
- [ ] MCP Google (Drive, Sheets — utile pour un PM)
- [ ] MCP Slack (lire/poster des messages sans quitter Claude)

## Skills custom
- [x] Skill `/ux` avec knowledge base (9 fichiers)
- [x] Skill `/touchdesigner` dual-mode (UI + Python builder)
- [ ] Skill `/spec` — template de spec Galigeo pré-rempli
- [ ] Skill `/release-notes` — génération automatique depuis git log
- [ ] Skill `/stakeholder-update` — format standard update hebdo

## Memory system
- [ ] Initialiser le dossier memory du projet
- [ ] Sauvegarder les préférences utilisateur (style, langue, niveau de détail)
- [ ] Sauvegarder les décisions produit clés (architecture, choix stratégiques)
- [ ] Sauvegarder les conventions d'équipe Galigeo
- [ ] Sauvegarder les références externes (boards Jira, dashboards, docs Confluence)
- [ ] Maintenir un MEMORY.md index à jour

## Keybindings
- [ ] Configurer `~/.claude/keybindings.json`
- [ ] Raccourci pour `/compact` (libérer le contexte)
- [ ] Raccourci pour changer l'effort level
- [ ] Raccourci pour annuler/interrompre rapidement

## Hooks avancés
- [x] Hook Notification (idle, permission)
- [ ] Hook post-Edit : auto-format (prettier, black)
- [ ] Hook post-Write : lint automatique
- [ ] Hook pre-commit : vérification fichiers sensibles (.env, credentials)
- [ ] Hook pre-Bash : log des commandes exécutées

## Workflow quotidien
- [ ] Utiliser `/compact <focus>` quand le contexte grossit
- [ ] Switcher `/effort high` pour specs/stratégie, `/effort low` pour triage
- [ ] Utiliser les subagents pour la recherche parallèle
- [ ] Utiliser `/bmad-review-adversarial-general` avant de livrer un doc important
- [ ] Utiliser `/bmad-editorial-review-prose` pour les communications externes
- [ ] Créer des PRs et reviewer des issues via `gh` sans quitter Claude

## Techniques avancées
- [ ] Worktrees (`/worktree`) pour travailler sur plusieurs branches en parallèle
- [ ] Commande `!` pour les commandes interactives (auth, login)
- [ ] `/review` systématique avant merge
- [ ] Prompt chaining : enchaîner des skills dans une même session
- [ ] Background agents pour les tâches longues (tests, builds)

## Hygiène & maintenance
- [ ] Nettoyer les tasks/todos obsolètes régulièrement
- [ ] Mettre à jour les memories quand une décision change
- [ ] Auditer les permissions tous les mois
- [ ] Mettre à jour CLAUDE.md quand le contexte projet évolue
- [x] Auto-updates sur canal stable
