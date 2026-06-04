# Hearts of Iron IV Modding AI Agent Skills

This package is a collection of general-purpose AI agent skills (Skills) designed to assist in Hearts of Iron IV (HOI4) mod development.
These skills are independent of any specific mod project and can be universally used for any HOI4 modding work.

[日本語のドキュメントはこちら (Japanese Documentation)](README_ja.md)

## Included Skills (21 Skills Total)

| Skill Name | Description |
| :--- | :--- |
| `hoi4-decisions-helper` | Interactive assistance for creating and managing decisions. |
| `hoi4-decisions-searcher` | Search and reference existing decision definitions. |
| `hoi4-event-helper` | Interactive creation of events (country_event, news_event, etc.) and localization. |
| `hoi4-event-searcher` | Search and reference existing event definitions. |
| `hoi4-focus-searcher` | Search national focus definitions. |
| `hoi4-gfx-searcher` | Search GFX definitions and image asset paths. |
| `hoi4-gui` | Build and optimize scripted GUIs and interface (.gui) files. |
| `hoi4-idea-creator` | Create and structure national spirits (Ideas) and laws. |
| `hoi4-image-asset-creator` | Help create, convert, and hook up image assets (TGA/DDS). |
| `hoi4-modifier-maker` | Interactive creation of modifier blocks and dynamic modifiers. |
| `hoi4-modifier-searcher` | Search and reference available modifiers. |
| `hoi4-nf-creator` | Create national focus trees and individual focus definitions. |
| `hoi4-on-actions-helper` | Configure `on_actions` and event triggers. |
| `hoi4-opinion-modifiers-helper` | Create and manage diplomatic opinion modifiers. |
| `hoi4-scripted-effect-maker` | Define and create scripted effects. |
| `hoi4-scripted-effect-searcher` | Search existing scripted effects. |
| `hoi4-scripted-localisation-helper` | Create and integrate scripted localization (defined text). |
| `hoi4-scripted-triggers-helper` | Define and create scripted triggers. |
| `hoi4-techtree-creator` | Define and structure technology trees. |
| `hoi4-unit-design-creator` | Assist in creating division and ship designs. |
| `hoi4-variable-helper` | Build logic for variable and array operations. |

## Reference Documentation (`docs/`)

In addition to Skills, this package includes a collection of general-purpose HOI4 modding reference materials in the `docs/` folder. These files can be read by AI agents to dramatically improve coding precision.
- **`00_character/`**: Detailed guide for the leader and character system.
- **`00_coding_contexts/`**: Coding contexts, optimization guides, variable usage, and console command summaries.
- **`01_effects/`**, **`02_scopes/`**, **`04_triggers/`**: Structured `.json` databases of HOI4 scopes, triggers, and effects.
- **`gitflow.md`**: Guide for GitFlow branch strategy.

## Usage


### Importing Skills to AI Agents

These skills are designed to be loaded by AI agents (e.g., Claude Code, Cursor, etc.).

1. **Deploying as `.skill` files**
   - Each skill's `.skill` file is a ZIP archive.
   - Create a `.claude/skills/` directory at the root of your active mod development directory, and copy the desired `.skill` files (e.g., `hoi4-event-helper.skill`) into it.

2. **Deploying as directories**
   - Alternatively, you can unpack the `.skill` files and place the skill folders directly under `.claude/skills/`.

### Packaging Skills

If you edit the contents of a skill and need to rebuild the `.skill` zip archive, use the provided Python scripts.

- **To package a specific skill:**
  ```bash
  python3 package_skill.py skills/<skill-directory-name>
  ```
  *(Example: `python3 package_skill.py skills/hoi4-modifier-maker` will update `skills/hoi4-modifier-maker.skill`)*

- **To package all skills at once:**
  ```bash
  python3 package_all.py
  ```

---
This package is structured for easy distribution. Good luck with your HOI4 modding!
