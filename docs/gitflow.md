# Tsareich2 GitFlow Policy

This repository uses a branch-based workflow for all AI-assisted and human-assisted development.

## Branches

- `main`: protected release branch. Do not push directly.
- `develop`: integration branch for completed work.
- Work branches: created for each feature, fix, archive, or isolated task.

## Required Flow

1. Start from the appropriate base branch, usually `develop`.
2. Create a work branch before editing.
3. Keep one branch focused on one topic.
4. If a task expands into unrelated work, create or switch to another branch.
5. Merge completed work branches into `develop`.
6. Do not push directly to `main`.

## Branch Name Format

Use:

```text
type/scope_name
```

The part before `/` explains what kind of branch it is. The part after `/` explains the area and short purpose.

## Branch Types

- `feature`: new content, new systems, countries, map work, technology work, documentation
- `fix`: bug fixes, crash fixes, syntax fixes, broken event/focus/decision fixes
- `archive`: saved historical versions or preservation branches

## Scope Rules

Use a clear scope:

- `TAG`: country work, such as `GER`, `JAP`, `RUS`
- `_map`: map, states, provinces, strategic regions
- `_Technology`: technology and equipment unlocks
- `_system`: shared systems, GUI systems, scripted effects, scripted triggers, AI-agent documentation
- `crash_TAG`: crash fixes tied to a country or specific feature

## Examples

```text
feature/GER_project
feature/_map_africa
feature/_Technology_air_rework
feature/_system_parliament
feature/_system_ai_agent_guidelines
fix/crash_JAP_event
archive/1.0
```

## AI Agent Requirements

AI agents must:

- Check `git status --short --branch` before editing.
- Create or use a properly named branch before file changes.
- Avoid combining unrelated tasks in one branch.
- Never revert user changes unless explicitly asked.
- Report the active branch and changed files when finishing work.
