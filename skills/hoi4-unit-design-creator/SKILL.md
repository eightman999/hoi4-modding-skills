---
name: hoi4-unit-design-creator
description: Create Hearts of Iron 4 unit designs (ship, plane, tank) through interactive dialogue. Use when the user (1) Requests to create unit designs for ships, aircraft, or tanks, (2) Wants to configure equipment variants with specific modules, (3) Needs to set up OOB designs for countries, or (4) Says phrases like "create ship design", "setup tank design", "configure plane variant", "艦船設計作成", "戦車設計", "航空機設計", etc. Handles complete implementation including design definition in OOB files, equipment modules selection, and proper configuration.
---

# HOI4 Unit Design Creator

## Overview

Create complete HOI4 unit designs (艦船・航空機・戦車) through interactive dialogue. Guides through selecting equipment archetypes, configuring modules with `create_equipment_variant` scripted effects, setting statistics, and automatically implements designs in history/units OOB files and scripted effects.

## When This Skill Triggers

This skill activates when:
- User explicitly requests creating unit designs (ship, plane, or tank)
- User mentions configuring equipment variants or modules
- While setting up countries, user specifies custom unit designs
- User says trigger phrases: "create ship design", "setup tank variant", "configure plane", "艦船設計作成", "戦車デザイン", "航空機バリアント", "make ship class", "design tank", "create variant", "make equipment variant"

## Interactive Workflow

Follow this step-by-step process to create a complete unit design implementation.

### Step 1: Gather Requirements

Ask the user the following information through interactive questions:

1. **Mod & Country Context**
   - "Which mod are you working on?" (to determine file paths)
   - "Which country is this design for?" (e.g., JPN, GER, USA)

2. **Unit Type**
   - "What type of unit design do you want to create?"
     - Ship (艦船)
     - Plane/aircraft (航空機)
     - Tank/armor (戦車)

3. **For Ships:**
   - "What hull/archetype?" (e.g., ship_hull_heavy, ship_hull_light, ship_hull_submarine, ship_hull_carrier)
   - "What ship role?" (capital_ship, cruiser, submarine, carrier, screen)
   - "What year level?" (1-5, or specific year like 1936, 1940, 1944)
   - "What is the design name?" (display name, e.g., "大和型戦艦", "Yamato-class")

4. **For Planes:**
   - "What airframe type?" (e.g., CAS_equipment, fighter_equipment, strategic_bomber_equipment, naval_bomber_equipment)
   - "What category?" (small_plane, medium_plane, large_plane, rocket_interceptor)
   - "What year level?" (0-10, or specific year)
   - "What is the design name?" (e.g., "零式艦上戦闘機", "A6M Zero")

5. **For Tanks:**
   - "What chassis type?" (e.g., light_tank_equipment, medium_tank_equipment, heavy_tank_equipment, modern_tank_equipment)
   - "What tank role?" (armor, anti_tank, artillery, anti_air, flame)
   - "What year level?" (1-5, or specific year)
   - "What is the design name?" (e.g., "九七式中戦車", "Type 97 Chi-Ha")

6. **Localization Language**
   - "What language(s) should I create localization for?" (japanese, english, etc.)

7. **Variant Creation Method**
   - "How should I create this variant?"
     - Option A: Create scripted effect with `create_equipment_variant` (recommended for custom designs)
     - Option B: Use existing variant level in OOB (simpler, less flexible)

8. **Variant Configuration** (if using create_equipment_variant)
   - "What variant name should I use?" (internal identifier, e.g., "JAP_yamato", "GER_panther", "USA_b29")
   - "What parent version/level?" (0-5 for most equipment, base variant level)
   - "Should I configure specific modules, or use upgrades?"
     - Modules: Specify exact module per slot (more control)
     - Upgrades: Apply upgrades to base variant (simpler)
   - If modules: Ask for module selections per slot

### Step 2: Confirm Implementation Plan

Present a summary to the user:

```
I will create the following unit design:

Type: Ship (Battleship)
Hull: ship_hull_heavy
Year Level: 4 (1944)
Name: 大和型戦艦 (Yamato-class)

Modules:
  - Ship type: SRM_BB
  - Primary armament: SM_HG_level_4
  - Secondary armament: SM_HG_level_3
  - AA: SM_AA_level_4
  - Engine: SM_TR_level_4
  - Fire control: SM_FCS_level_3
  - Armor: SM_OT_level_4

Variant Method: Scripted effect with create_equipment_variant
Variant Name: JPN_yamato_variant
Parent Version: 0
Modules:
  - Fixed battery: ship_JAP_heavy_battery
  - Fixed AA: ship_dp_Bofors_battery_3
  - Fixed FCS: ship_fire_control_system_4
  - Fixed radar: ship_radar_4
  - Fixed engine: SM_engine_4
  - Fixed armor: sm_armor_4
  - Front slot: ship_anti_air_rocket_2
  - Mid slot 1: ship_depth_charge_2
  - Mid slot 2: ship_JAP_torpedo_2
  - Rear slot: ship_JAP_heavy_battery
Upgrades:
  - ship_mtg_naval_range_upgrade = 6
  - ship_mtg_armor_upgrade = 5
  - ship_mtg_main_battery_upgrade = 5

Files to create/modify:
  1. common/scripted_effects/JPN_variants.txt (add create_equipment_variant)
  2. history/units/JPN_1936.txt (add division/navy with variant)
  3. localisation/japanese/JPN_units_l_japanese.yml (add name)

Proceed? (yes/no)
```

### Step 3: Determine File Locations

Based on mod structure, determine where files should be created:

**Scripted Effect (Variant Definition):**
- Path: `<mod_root>/common/scripted_effects/`
- Filename: Usually `<country_tag>_variants.txt` (e.g., JPN_variants.txt, GER_variants.txt)
- Or append to existing variants file for the country
- Format: `<country>_variants = { create_equipment_variant = { ... } }`

**OOB File (Unit Deployment):**
- Path: `<mod_root>/history/units/`
- Filename: `<country_tag>_<year>.txt` (e.g., JPN_1936.txt, GER_1939.txt)
- If file exists, append to `divisions = {}` or `navies = {}` or `air_wings = {}` block
- For units using the variant: use `create_equipment_variant` effect or apply in OOB

**Localization:**
- Path: `<mod_root>/localisation/<language>/`
- Filename: Usually `<country_tag>_units_l_<language>.yml` or existing file

### Step 4: Implement Scripted Effect with create_equipment_variant

Add to `common/scripted_effects/<country>_variants.txt`:

**For Ships:**

```
<COUNTRY>_variants = {
  create_equipment_variant = {
    name = "<variant_name>"
    type = <ship_hull_type>
    parent_version = <0-5>
    icon = "<GFX_icon_id>"  # Optional
    name_group = <name_group_id>  # Optional for automatic naming

    modules = {
      fixed_ship_battery_slot = <module_id>
      fixed_ship_anti_air_slot = <module_id>
      fixed_ship_fire_control_system_slot = <module_id>
      fixed_ship_radar_slot = <module_id>
      fixed_ship_engine_slot = <module_id>
      fixed_ship_secondaries_slot = <module_id>
      fixed_ship_armor_slot = <module_id>
      front_1_custom_slot = <module_id>
      mid_1_custom_slot = <module_id>
      mid_2_custom_slot = <module_id>
      rear_1_custom_slot = <module_id>
      # Additional slots as needed
    }

    upgrades = {
      ship_mtg_naval_range_upgrade = <0-10>
      ship_mtg_armor_upgrade = <0-10>
      ship_mtg_main_battery_upgrade = <0-10>
      ship_mtg_secondary_battery_upgrade = <0-10>
      ship_mtg_anti_air_upgrade = <0-10>
      ship_mtg_fire_control_system_upgrade = <0-10>
      ship_mtg_radar_upgrade = <0-10>
      ship_mtg_engine_upgrade = <0-10>
      # Other upgrades as needed
    }

    obsolete = yes/no  # Optional
  }
}
```

**For Planes:**

```
<COUNTRY>_variants = {
  create_equipment_variant = {
    name = "<variant_name>"
    type = <plane_equipment_type>
    parent_version = <0-10>
    icon = "<GFX_icon_id>"  # Optional

    upgrades = {
      plane_gun_upgrade = <0-5>
      plane_engine_upgrade = <0-5>
      plane_reliability_upgrade = <0-5>
      plane_range_upgrade = <0-5>
      plane_bomb_upgrade = <0-5>  # For CAS/bombers
      plane_naval_upgrade = <0-5>  # For naval bombers
      plane_rocket_upgrade = <0-5>  # For rocket interceptors
      plane_agility_upgrade = <0-5>
      plane_defense_upgrade = <0-5>
      # Other upgrades as needed
    }

    obsolete = yes/no  # Optional
  }
}
```

**For Tanks:**

```
<COUNTRY>_variants = {
  create_equipment_variant = {
    name = "<variant_name>"
    type = <tank_chassis_type>
    parent_version = <0-5>
    icon = "<GFX_icon_id>"  # Optional

    modules = {
      main_armament_slot = <module_id>
      turret_type_slot = <module_id>
      suspension_type_slot = <module_id>
      armor_type_slot = <module_id>
      engine_type_slot = <module_id>
      special_type_slot_0 = <module_id>
      special_type_slot_1 = <module_id>
      special_type_slot_2 = <module_id>
      special_type_slot_3 = <module_id>
      special_type_slot_4 = <module_id>
    }

    upgrades = {
      tank_engine_upgrade = <0-5>
      tank_armor_upgrade = <0-5>
      tank_gun_upgrade = <0-5>
      tank_reliability_upgrade = <0-5>
      tank_nsb_engine_upgrade = <0-10>  # NSB DLC variant
      tank_nsb_armor_upgrade = <0-10>
      # Other upgrades as needed
    }

    obsolete = yes/no  # Optional
  }
}
```

### Step 5: Apply Variant in OOB (Optional)

If you want to immediately use the variant in OOB files:

**For Ships:**
Add to `history/units/<country>_<year>.txt` inside `navies = {}` block:

```
navies = {
  JPN = {
    name = "日本帝国海軍"
    task_forces = {
      <division_name> = {
        name = "<display_name>"
        location = <state_id>
        <equipment_level> = {
          <equipment_archetype> = <variant_level>
        }
        is_template = yes
        design = {
          name = "<internal_design_id>"
          design_name = "<display_name>"
          tasks = { <task_types> }
          equipment = {
            <slot_name> = <module_id>
            ...
          }
        }
      }
    }
  }
}
```

**Common ship slot names:**
- `ship_type_slot` - SRM_BB, SRM_BC, SRM_BBG, etc.
- `primary_armament_slot` - SM_HG_level_X, SM_LG_level_X
- `secondary_armament_slot` - SM_HG_level_X, SM_LG_level_X
- `primary_sub_armament_slot` - SM_MG_level_X, SM_AA_level_X
- `secondary_sub_armament_slot` - SM_MG_level_X, SM_AA_level_X
- `primary_light_armament_slot` - SM_AA_level_X, SM_RF_level_X
- `hidden_EN_slot` - SM_TR_level_X (engine)
- `hidden_ENPOWER_slot` - SM_ENPOWER_level_X
- `hidden_ARMOR_slot` - SM_OT_level_X (armor)
- `fire_control_system_slot` - SM_FCS_level_X
- `radar_slot` - SM_RADAR_level_X
- `sonar_slot` - SM_SONAR_level_X

**Common task types:**
- HOLD_THE_LINE, ATTACK, CONVOY_RAIDING, PATROL, INVADE, NAVAL_INVASION_SUPPORT, MINE_SWEEPING, MINES_PLANTING

### Step 6: Implement Plane Design (Optional OOB)

Add to `history/units/<country>_<year>.txt` inside `air_wings = {}` block:

```
air_wings = {
  <wing_name> = {
    name = "<display_name>"
    base = <state_id>
    mission = <mission_type>
    <equipment_level> = {
      <equipment_archetype> = <variant_level>
    }
    # For custom variant:
    variant = {
      <equipment_archetype> = {
        name = "<variant_name>"
        modules = {
          <module_slot> = <module_id>
          ...
        }
      }
    }
  }
}
```

**Common plane equipment archetypes:**
- CAS_equipment (Close Air Support)
- fighter_equipment (Fighter)
- strategic_bomber_equipment
- naval_bomber_equipment
- tactical_bomber_equipment
- heavy_fighter_equipment
- jet_fighter_equipment

**Common plane module slots:**
- `plane_engine_slot` - P_engines_level_X
- `plane_airframe_slot` - P_wings_level_X
- `plane_bomb_slot` - P_bombs_level_X
- `plane_gun_slot` - P_guns_level_X
- `plane_defense_slot` - P_defguns_level_X
- `plane_radar_slot` - P_radar_level_X
- `plane_range_slot` - P_options_level_X (range modules)

### Step 7: Implement Tank Design (Optional OOB)

Add to `history/units/<country>_<year>.txt` inside `divisions = {}` block:

```
divisions = {
  <division_name> = {
    division_name = "<display_name>"
    division_template = "<template_name>"
    start_experience = <0.0 to 1.0>
    location = <state_id>
    <equipment_level> = {
      <equipment_archetype> = <variant_level>
    }
    # For custom variant:
    variant = {
      <equipment_archetype> = {
        name = "<variant_name>"
        modules = {
          <module_slot> = <module_id>
          ...
        }
      }
    }
  }
}
```

**Common tank equipment archetypes:**
- light_tank_equipment
- medium_tank_equipment
- heavy_tank_equipment
- modern_tank_equipment
- super_heavy_tank_equipment

**Common tank module slots:**
- `tank_engine_slot` - T_engine_level_X
- `turret_slot` - T_turrets_level_X
- `armor_slot` - T_armor_level_X
- `tank_gun_slot` - T_GT_gun_level_X (main gun)
- `secondary_gun_slot` - T_SEC_gun_level_X
- `tank_aa_gun_slot` - T_MW_tank_aa_level_X
- `tank_artillery_slot` - T_MW_art_level_X
- `tank_anti_tank_slot` - T_MW_tank_at_level_X
- `tank_radio_slot` - T_EE_radio_level_X
- `reliability_slot` - T_EE_radio_level_X
- `suspension_slot` - T_Suspensions_level_X

### Step 8: Implement Localization

Add to `localisation/<language>/<file>_l_<language>.yml`:

```yaml
l_<language>:
 <internal_design_id>:0 "<display_name>"
 <internal_design_id>_desc:0 "<description>"
```

**Important:**
- For designs in OOB files, localization keys use the internal design ID
- File must start with UTF-8 BOM (`﻿`)
- Use format `key:0 "value"` with space after colon
- Append to existing file if present

### Step 9: Verify Implementation

After creating/modifying files:

1. Confirm all file types were updated:
   - ✅ Scripted effect with `create_equipment_variant` in `common/scripted_effects/`
   - ✅ Design definition in `history/units/` (if OOB deployment)
   - ✅ Localization in `localisation/<language>/`

2. Show the user a summary of changes:
   ```
   Created/Modified:
   - common/scripted_effects/JPN_variants.txt (added yamato variant)
   - history/units/JPN_1936.txt (added division/navy with variant)
   - localisation/japanese/JPN_units_l_japanese.yml (added name)

   The variant is ready to use!

   To use this variant:
   1. In scripted effects: Create a new scripted effect that calls:
      JPN_variants = { create_equipment_variant = { name = "<variant_name>" type = <hull_type> parent_version = <version> } }
   2. In events/national focuses: Use the scripted effect
   3. In OOB: Units will automatically use the variant if specified

   The variant creates a custom equipment configuration that can be assigned to units.
   ```

## Using create_equipment_variant Scripted Effects

### Triggering Variant Creation

To create variants in-game, use scripted effects or events:

**In scripted effects:**
```
create_yamato_variant = {
  JPN_variants = {
    create_equipment_variant = {
      name = "大和型戦艦"
      type = ship_hull_heavy_4
      parent_version = 0
      # modules and upgrades...
    }
  }
}
```

**In events:**
```
country_event = {
  id = jap.1
  title = jap.1.t
  desc = jap.1.d

  option = {
    name = jap.1.a
    trigger = {
      has_technology = {
        ship_hull_heavy_4
      }
    }
    create_yamato_variant = yes
  }
}
```

### Available Equipment Types

**Ship Hulls:**
- ship_hull_heavy_1 through ship_hull_heavy_5 (Battleships, Battlecruisers)
- ship_hull_light_1 through ship_hull_light_5 (Cruisers, Destroyers)
- ship_hull_carrier_1 through ship_hull_carrier_5 (Carriers)
- ship_hull_submarine_1 through ship_hull_submarine_4 (Submarines)
- Custom hull types defined in mod

**Plane Airframes:**
- fighter_equipment_0 through fighter_equipment_10
- CAS_equipment_0 through CAS_equipment_10
- strategic_bomber_equipment_0 through strategic_bomber_equipment_10
- naval_bomber_equipment_0 through naval_bomber_equipment_10
- tactical_bomber_equipment_0 through tactical_bomber_equipment_10
- heavy_fighter_equipment_0 through heavy_fighter_equipment_10
- jet_fighter_equipment_0 through jet_fighter_equipment_10
- Custom airframes defined in mod

**Tank Chassis:**
- light_tank_chassis_0 through light_tank_chassis_5
- medium_tank_chassis_0 through medium_tank_chassis_5
- heavy_tank_chassis_0 through heavy_tank_chassis_5
- modern_tank_chassis_0 through modern_tank_chassis_5
- super_heavy_tank_chassis_0 through super_heavy_tank_chassis_3
- Custom chassis defined in mod

## Module Selection Guidelines

### Ships - Module Levels

**Ship Module Slots (fixed_*_slot):**
- `fixed_ship_battery_slot` - Main battery (ship_JAP_heavy_battery, ship_old_medium_battery_3, etc.)
- `fixed_ship_anti_air_slot` - AA guns (ship_dp_Bofors_battery_2, ship_old_anti_air_2A)
- `fixed_ship_fire_control_system_slot` - FCS (ship_fire_control_system_1-4)
- `fixed_ship_radar_slot` - Radar (ship_radar_1-4)
- `fixed_ship_engine_slot` - Engine (SM_engine_1-6)
- `fixed_ship_secondaries_slot` - Secondary batteries (ship_old_secondaries_1-3)
- `fixed_ship_armor_slot` - Armor (sm_armor_1-4)

**Ship Custom Slots:**
- `front_1_custom_slot` - Front deck/weapon
- `mid_1_custom_slot`, `mid_2_custom_slot` - Mid deck/weapons
- `rear_1_custom_slot` - Rear deck/weapon

**Common Ship Modules:**
- Batteries: ship_JAP_heavy_battery, ship_medium_battery_1, ship_old_medium_battery_3
- AA: ship_dp_Bofors_battery_2, ship_old_anti_air_2A, ship_dp_old_light_battery_3
- FCS: ship_fire_control_system_1 through ship_fire_control_system_4
- Radar: ship_radar_1 through ship_radar_4
- Engine: SM_engine_1 through SM_engine_6 (higher = better speed)
- Armor: sm_armor_1 through sm_armor_4 (higher = more armor)
- Weapons: ship_torpedo_1-2, ship_depth_charge_1-2, ship_anti_air_rocket_1-2

**Ship Upgrade Types:**
- ship_mtg_naval_range_upgrade = <0-10>
- ship_mtg_armor_upgrade = <0-10>
- ship_mtg_main_battery_upgrade = <0-10>
- ship_mtg_secondary_battery_upgrade = <0-10>
- ship_mtg_anti_air_upgrade = <0-10>
- ship_mtg_fire_control_system_upgrade = <0-10>
- ship_mtg_radar_upgrade = <0-10>
- ship_mtg_engine_upgrade = <0-10>

**Ship Year Levels (parent_version):**
- Level 0: Base/early variant
- Level 1-2: Early war designs (1936-1939)
- Level 3: Mid war (1940-1942)
- Level 4-5: Late war (1943-1945+)

**Ship Type Slots (legacy OOB):**
- ship_type_slot - SRM_BB, SRM_BC, SRM_BBG (battleship types)
- ship_type_slot - SRM_CL, SRM_CA (cruiser types)
- ship_type_slot - SRM_DD (destroyer)
- ship_type_slot - SRM_SS (submarine)

### Planes - Upgrade System

**Plane Upgrade Types:**
- plane_gun_upgrade = <0-5> - Increased attack
- plane_engine_upgrade = <0-5> - Increased speed
- plane_reliability_upgrade = <0-5> - Increased reliability
- plane_range_upgrade = <0-5> - Increased range
- plane_bomb_upgrade = <0-5> - Increased bombing attack (CAS/bombers)
- plane_naval_upgrade = <0-5> - Increased naval attack (naval bombers)
- plane_rocket_upgrade = <0-5> - Increased rocket attack (rocket interceptors)
- plane_agility_upgrade = <0-5> - Increased agility (dogfighting)
- plane_defense_upgrade = <0-5> - Increased defense
- cv_plane_gun_upgrade = <0-5> - CV fighters
- cv_plane_bomb_upgrade = <0-5> - CAS on carriers

**Plane Year Levels (parent_version):**
- Level 0-3: Early war (1936-1939)
- Level 4-6: Mid war (1940-1942)
- Level 7-10: Late war (1943-1945+)

### Tanks - Module System

**Tank Module Slots:**
- `main_armament_slot` - Main gun (tank_heavy_cannon, tank_medium_cannon, tank_small_cannon_1-3)
- `turret_type_slot` - Turret type (tank_large_tank_turret, tank_medium_tank_turret, tank_small_tank_turret)
- `suspension_type_slot` - Suspension (tank_torsion_bar_suspension, tank_christie_suspension, tank_bogie_suspension)
- `armor_type_slot` - Armor type (tank_RHA_armor, tank_composite_armor)
- `engine_type_slot` - Engine (tank_diesel_engine, tank_gasoline_engine)
- `special_type_slot_0-4` - Special equipment (tank_radio_1-2, tank_gun_turret_lmg_1-2, sloped_armor, extra_ammo_storage, easy_maintenance)

**Common Tank Modules:**
- Main guns: tank_heavy_cannon, tank_medium_cannon, tank_small_cannon_1-3
- Turrets: tank_large_tank_turret, tank_medium_tank_turret, tank_small_tank_turret, tank_large_fixed_superstructure_turret
- Suspension: tank_torsion_bar_suspension, tank_christie_suspension, tank_bogie_suspension
- Armor: tank_RHA_armor, tank_composite_armor
- Engine: tank_diesel_engine, tank_gasoline_engine
- Special: tank_radio_1-2, tank_gun_turret_lmg_1-2, sloped_armor, extra_ammo_storage, easy_maintenance

**Tank Upgrade Types:**
- tank_engine_upgrade = <0-5>
- tank_armor_upgrade = <0-5>
- tank_gun_upgrade = <0-5>
- tank_reliability_upgrade = <0-5>
- tank_nsb_engine_upgrade = <0-10> (NSB DLC variant)
- tank_nsb_armor_upgrade = <0-10> (NSB DLC variant)

**Tank Year Levels (parent_version):**
- Level 0: Base/early variant
- Level 1-2: Early war (1936-1939)
- Level 3-4: Mid war (1940-1942)
- Level 5: Late war (1943-1945+)

## Common Design Patterns

### Battleship Design (Japan - Yamato-class)

**Scripted Effect:**
```
JPN_variants = {
  create_equipment_variant = {
    name = "大和型戦艦"
    type = ship_hull_heavy_4
    parent_version = 0
    icon = "GFX_JAP_battleship_1944_medium"

    modules = {
      fixed_ship_battery_slot = ship_JAP_heavy_battery
      fixed_ship_anti_air_slot = ship_dp_Bofors_battery_3
      fixed_ship_fire_control_system_slot = ship_fire_control_system_4
      fixed_ship_radar_slot = ship_radar_4
      fixed_ship_engine_slot = SM_engine_4
      fixed_ship_secondaries_slot = ship_old_secondaries_2
      fixed_ship_armor_slot = sm_armor_4
      front_1_custom_slot = ship_anti_air_rocket_2
      mid_1_custom_slot = ship_depth_charge_2
      rear_1_custom_slot = ship_JAP_heavy_battery
    }

    upgrades = {
      ship_mtg_naval_range_upgrade = 6
      ship_mtg_armor_upgrade = 5
      ship_mtg_main_battery_upgrade = 5
      ship_mtg_anti_air_upgrade = 4
      ship_mtg_fire_control_system_upgrade = 4
      ship_mtg_radar_upgrade = 4
      ship_mtg_engine_upgrade = 4
    }
  }
}
```

### Fighter Design (Japan - Zero)

**Scripted Effect:**
```
JPN_variants = {
  create_equipment_variant = {
    name = "零式艦上戦闘機"
    type = fighter_equipment_2
    parent_version = 0
    icon = "GFX_JAP_small_airframe_1"

    upgrades = {
      plane_gun_upgrade = 2
      plane_engine_upgrade = 2
      plane_reliability_upgrade = 2
      plane_range_upgrade = 2
      plane_agility_upgrade = 2
    }

    obsolete = yes
  }
}
```

### Tank Design (Japan - Type 97 Chi-Ha)

**Scripted Effect:**
```
JPN_variants = {
  create_equipment_variant = {
    name = "九七式中戦車"
    type = medium_tank_chassis_1
    parent_version = 0
    icon = "GFX_JAP_medium_tank_chassis_1940_medium"

    modules = {
      main_armament_slot = tank_medium_cannon
      turret_type_slot = tank_medium_tank_turret
      suspension_type_slot = tank_bogie_suspension
      armor_type_slot = tank_RHA_armor
      engine_type_slot = tank_diesel_engine
      special_type_slot_0 = tank_gun_turret_lmg_1
      special_type_slot_1 = tank_radio_1
      special_type_slot_2 = easy_maintenance
      special_type_slot_3 = empty
      special_type_slot_4 = empty
    }

    upgrades = {
      tank_engine_upgrade = 2
      tank_armor_upgrade = 1
      tank_gun_upgrade = 1
      tank_reliability_upgrade = 1
    }

    obsolete = yes
  }
}
```

## Error Prevention

Common mistakes to avoid:

1. **Invalid Type References**
   - Verify equipment type exists (check equipment files)
   - Use correct chassis/hull/airframe IDs
   - Don't confuse chassis vs equipment names (e.g., medium_tank_chassis_1 vs medium_tank_equipment_1)

2. **Module ID Mismatches**
   - Ensure module IDs exist in module files
   - Check modules are compatible with hull/archetype
   - Verify slot names match hull definition

3. **Upgrade Value Limits**
   - Upgrade values should be 0-5 (or 0-10 for some NSB upgrades)
   - Don't exceed maximum upgrade level

4. **Scripted Effect Structure**
   - Wrap `create_equipment_variant` in a scripted effect block
   - Ensure proper bracket nesting
   - Don't mix modules and upgrades in ways that don't make sense

5. **Parent Version Issues**
   - parent_version must exist for the equipment type
   - Level 0 is typically base variant
   - Higher levels require technology research

6. **Localization Issues**
   - Use UTF-8 BOM for localization files
   - Variant names must match between scripted effect and localization
   - Use correct language directory path

7. **OOB Deployment Issues**
   - `force_equipment_variants` requires owner tag
   - Version name must match created variant name
   - Division/navy location must be valid state ID

## Reference Documentation

For detailed information on equipment and modules:
- `common/units/equipment/` - Equipment archetype definitions
- `common/units/equipment/modules/` - Module definitions (00_S_*.txt, 00_P_*.txt, 00_T_*.txt)
- `common/units/equipment/ship_hull_*.txt` - Ship hulls and slots
- `common/units/equipment/x_tank_chassis.txt` - Tank chassis types
- `common/units/equipment/x_plane_airframes.txt` - Plane airframe types
- `common/scripted_effects/` - Example variant definitions (_ssw_variants_*.txt)
- HOI4 Wiki on Equipment and OOB modding
- HOI4 Wiki on `create_equipment_variant` effect

### Finding Valid Modules

To find available modules for equipment:

```
# Search ship modules
rg "fixed_ship_battery_slot" SSW_mod/common/units/equipment/modules/ -A 2

# Search tank modules
rg "main_armament_slot" SSW_mod/common/units/equipment/modules/ -A 2

# Search plane upgrades
rg "plane_gun_upgrade" SSW_mod/common/units/equipment/ -A 2
```

### Example Variant Files

- `_ssw_variants_navy.txt` - Naval variants
- `_ssw_variants_air.txt` - Air variants
- `_ssw_variants_army.txt` - Tank/land variants
- These files show complete examples of working variants
