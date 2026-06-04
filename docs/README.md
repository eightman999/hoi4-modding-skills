# Tsareich2 Documents Entry Point

This directory contains HOI4 scripting references for coding agents and contributors. Use this file as the first stop before editing unfamiliar script, trigger, effect, localisation, character, or scope logic.

## Fast Path

- General scripting concepts: `00_coding_contexts/script_concept_documentation.md`
- Effects: `00_coding_contexts/effects_documentation.md` and `01_effects/effects.json`
- Triggers: `00_coding_contexts/triggers_documentation.md` and `04_triggers/triggers.json`
- Scopes: `02_scopes/hoi4_scopes.json` and `02_scopes/01_Dual scopes.md`
- Variables: `00_coding_contexts/00_variable.md` and `00_coding_contexts/dynamic_variables_documentation.md`
- Modifiers: `00_coding_contexts/modifiers_documentation.md`
- Localisation: `00_coding_contexts/loc_formatter_documentation.md`, `00_coding_contexts/loc_objects_documentation.md`, and `95_scripted_localisation.md`
- Characters and leaders: `00_character/`

## Task-Oriented Routes

- Events and decisions: check script concepts, scopes, triggers, and effects before editing.
- Scripted effects: check `99_scripted_effects.md`, then confirm individual effects in `01_effects/effects.json`.
- Scripted triggers: check `99_scripted_triggers.md`, then confirm individual triggers in `04_triggers/triggers.json`.
- Character or trait work: start in `00_character/`, then inspect nearby files in `common/characters/`, `common/country_leader/`, or `common/unit_leader/`.
- Country setup: use `98_country.md`, then inspect nearby files in `common/countries/` and `history/countries/`.
- Building or state-related work: use `96_buildings.md`, `03_map/01_River.md`, and nearby files in `history/states/` or `map/`.

## Agent Rules

- Read `../AGENTS.md` before editing repository files.
- Treat these documents as reference material, not as Tsareich2 gameplay content.
- Do not import reference-mod-specific systems or IDs unless the user explicitly asks.
- Prefer existing Tsareich2 naming and structure over examples from the reference documents.
