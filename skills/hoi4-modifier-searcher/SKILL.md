---
name: hoi4-modifier-searcher
description: Search and discover Hearts of Iron 4 modifiers (static and dynamic) by keyword or category. Use when the user (1) Asks "what modifiers are available for X?", (2) Needs to find modifiers for specific effects like "stability", "production", "military strength", (3) Wants to browse modifiers by category, (4) Searches for existing dynamic modifiers in the mod, or (5) Says phrases like "show me modifiers for...", "what modifier affects...", "list production modifiers", "find dynamic modifiers", etc. Essential tool when creating ideas, national focuses, dynamic modifiers, or any game effects.
---

# HOI4 Modifier Searcher

## Overview

Search and discover Hearts of Iron 4 modifiers by keyword, category, or effect type. Supports both static modifiers (for ideas/focuses) and dynamic modifiers (variable-based with conditions). Quickly find the right modifiers for ideas, national focuses, decisions, and other game mechanics.

## When This Skill Triggers

This skill activates when:
- User asks about available modifiers ("What modifiers affect stability?")
- User needs to find modifiers for specific game mechanics
- While creating ideas/focuses, user wants to explore modifier options
- User says: "show modifiers for production", "list military modifiers", "what affects factories?"

## Quick Start

Use the search script to find modifiers:

```bash
# Search by keyword
python3 scripts/search_modifiers.py --search <keyword>

# Browse by category
python3 scripts/search_modifiers.py --category <category>

# List all categories
python3 scripts/search_modifiers.py --list-categories

# Show all modifiers
python3 scripts/search_modifiers.py --all
```

## Search by Keyword

Find modifiers containing specific words in their name, description, or tags.

**Examples:**

```bash
# Find stability-related modifiers
python3 scripts/search_modifiers.py --search stability

# Find production modifiers
python3 scripts/search_modifiers.py --search production

# Find factory-related modifiers
python3 scripts/search_modifiers.py --search factory

# Find attack modifiers
python3 scripts/search_modifiers.py --search attack
```

**Output shows:**
- Modifier name
- Category
- Description
- Example value
- Match type (name, tag, or description)

## Browse by Category

View all modifiers in a specific category:

```bash
# Show all political modifiers
python3 scripts/search_modifiers.py --category political

# Show all economy modifiers
python3 scripts/search_modifiers.py --category economy

# Show all military modifiers
python3 scripts/search_modifiers.py --category military

# Show all naval modifiers
python3 scripts/search_modifiers.py --category navy

# Show all air force modifiers
python3 scripts/search_modifiers.py --category air
```

## Search for Dynamic Modifiers

Search for existing dynamic modifiers defined in your mod's `common/dynamic_modifiers/` directory using Grep:

### Find All Dynamic Modifiers

Use Grep to find all dynamic modifier definitions:

```
Pattern: ^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*\{
Path: common/dynamic_modifiers/
```

This finds all modifier blocks in the format `modifier_name = { ... }`.

### Search by Name

Find a specific dynamic modifier:

```
Pattern: ^modifier_name\s*=
Path: common/dynamic_modifiers/
```

### Search by Feature

Find dynamic modifiers with specific features:

**With enable conditions:**
```
Pattern: enable\s*=
Path: common/dynamic_modifiers/
-B: 2  (show modifier name context)
```

**With variables:**
```
Pattern: var_
Path: common/dynamic_modifiers/
-B: 3  (show modifier name context)
```

**With remove triggers:**
```
Pattern: remove_trigger
Path: common/dynamic_modifiers/
-B: 2
```

**By scope (state modifiers):**
```
Pattern: state_.*factor
Path: common/dynamic_modifiers/
-B: 2
```

### Example Searches

**User asks: "What dynamic modifiers exist in my mod?"**
Use Grep with pattern `^[a-zA-Z_][a-zA-Z0-9_]*\s*=` in `common/dynamic_modifiers/`

**User asks: "Are there any war-related dynamic modifiers?"**
Use Grep with pattern `war` (case insensitive) in `common/dynamic_modifiers/`, show context lines

**User asks: "Which dynamic modifiers use variables?"**
Use Grep with pattern `var_` in `common/dynamic_modifiers/`, show context

## Available Categories

Run `--list-categories` to see all categories:

- **political** - Stability, war support, political power, ideology drift
- **economy** - Production, factories, construction, efficiency, resources
- **military** - Army stats, organization, training, combat modifiers
- **navy** - Naval combat, convoy operations, ship stats
- **air** - Aircraft stats, air combat, ace generation
- **intelligence** - Operatives, encryption, espionage
- **resources** - Resource extraction, trade
- **other** - Supply, attrition, AI behavior, misc

## Common Use Cases

### "I need a stability boost"

```bash
python3 scripts/search_modifiers.py --search stability
```

Returns:
- `stability_factor` - Direct stability modifier
- Related modifiers affecting internal stability

### "What modifiers improve production?"

```bash
python3 scripts/search_modifiers.py --search production
python3 scripts/search_modifiers.py --category economy
```

Returns:
- `production_speed_buildings_factor` - All construction
- `production_speed_industrial_complex_factor` - Civilian factories
- `production_speed_arms_factory_factor` - Military factories
- `industrial_capacity_factory` - Factory output
- Many more production-related modifiers

### "Show me military buffs"

```bash
python3 scripts/search_modifiers.py --category military
```

Returns all army-related modifiers:
- Attack, defense, organization
- Training, experience
- Planning, reinforcement
- Morale and combat stats

### "What affects naval combat?"

```bash
python3 scripts/search_modifiers.py --category navy
python3 scripts/search_modifiers.py --search naval
```

Returns naval modifiers:
- Ship combat stats
- Convoy operations
- Naval coordination
- Range and speed

## Interpreting Results

### Modifier Format

Each result shows:
```
📌 stability_factor
   Category: political
   Description: Stability modifier
   Example: stability_factor = 0.10
   Match: name
```

### Understanding Values

**Percentage modifiers** (most common):
- `0.10` = +10%
- `-0.10` = -10%
- `0.05` = +5%

**Absolute values** (some modifiers):
- `operative_slot = 1` (adds 1 slot)
- `crypto_strength = 1` (adds 1 level)

### Typical Ranges

**Small buffs:** `0.05` to `0.10` (5-10%)
**Standard buffs:** `0.10` to `0.20` (10-20%)
**Large buffs:** `0.25` to `0.50` (25-50%)
**Debuffs:** Negative values (e.g., `-0.15` = -15%)

## Integration with idea-creator

When using with `hoi4-idea-creator`, combine searches to build modifier blocks:

1. User requests: "Create an economic boom idea"
2. Search for relevant modifiers:
   ```bash
   python3 scripts/search_modifiers.py --search production
   python3 scripts/search_modifiers.py --search stability
   ```
3. Select appropriate modifiers:
   ```
   modifier = {
       stability_factor = 0.10
       production_speed_industrial_complex_factor = 0.15
       industrial_capacity_factory = 0.10
   }
   ```

## Common Modifier Combinations

See `references/modifier_categories.md` for:
- Detailed category descriptions
- Common search patterns
- Thematic modifier combinations
- Example modifier blocks for different effects

**Economic Boom example:**
```bash
python3 scripts/search_modifiers.py --search production
python3 scripts/search_modifiers.py --search factory
```

Suggested combination:
```
modifier = {
    stability_factor = 0.10
    production_speed_industrial_complex_factor = 0.15
    industrial_capacity_factory = 0.10
}
```

**Military Focus example:**
```bash
python3 scripts/search_modifiers.py --category military
```

Suggested combination:
```
modifier = {
    conscription_factor = 0.10
    training_time_factor = -0.10
    army_org_factor = 0.05
}
```

## Advanced Search Tips

### Combining Searches

When unsure, try multiple related keywords:
```bash
python3 scripts/search_modifiers.py --search factory
python3 scripts/search_modifiers.py --search construction
python3 scripts/search_modifiers.py --search efficiency
```

### Exploring Related Modifiers

After finding one modifier, search its category:
```bash
# Found "stability_factor" in search
python3 scripts/search_modifiers.py --category political
# See all related political modifiers
```

### Negative Effects

Many modifiers work in reverse with negative values:
- `consumer_goods_factor = 0.05` (penalty)
- `training_time_factor = -0.10` (faster training)
- `attrition = -0.10` (reduced attrition)

## Reference Documentation

For complete details on modifier usage and combinations:
- `references/modifier_categories.md` - Category guide and common patterns
- Use the search script to explore the full modifier database

## Workflow with Other Skills

**With hoi4-idea-creator:**
1. User: "Create a military idea"
2. Use modifier-searcher to find relevant modifiers
3. Suggest appropriate modifiers to user
4. Pass selected modifiers to idea-creator for implementation

**With hoi4-modifier-maker:**
1. User requests creating modifier block
2. Use modifier-searcher to find relevant static modifiers
3. Or use Grep to find existing dynamic modifiers for reference
4. Pass found modifiers to modifier-maker for building the block

**With hoi4-gfx-searcher:**
1. Find appropriate modifiers for an idea
2. Suggest matching GFX sprites that fit the theme
3. Create complete idea with matching visuals and effects

## Dynamic vs Static Modifier Search

**Static Modifiers (Built-in):**
- Use: `python3 scripts/search_modifiers.py --search <keyword>`
- Searches the built-in modifier database
- Returns vanilla HOI4 modifiers with categories and descriptions
- Used in ideas, focuses, decisions (regular modifier blocks)

**Dynamic Modifiers (Custom in Mod):**
- Use: Grep tool with `common/dynamic_modifiers/` path
- Searches your mod's custom dynamic modifier definitions
- Returns modifier names with enable/remove conditions and variables
- Used with `add_dynamic_modifier` effect

**When to use each:**
- User asks "what modifiers affect X?" → Use static modifier search
- User asks "what dynamic modifiers exist?" → Use Grep on dynamic_modifiers/
- User asks "are there modifiers for Y?" → Search both (static first, then check dynamic)
