#!/usr/bin/env python3
"""
Package HOI4 modding skills into .skill files (zip archives).
"""

import os
import sys
import zipfile
from pathlib import Path


def package_skill(skill_dir):
    """Package a skill directory into a .skill file."""
    skill_path = Path(skill_dir)

    if not skill_path.exists():
        print(f"Error: Skill directory '{skill_dir}' does not exist")
        return False

    if not skill_path.is_dir():
        print(f"Error: '{skill_dir}' is not a directory")
        return False

    # Check for SKILL.md
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"Error: SKILL.md not found in '{skill_dir}'")
        return False

    # Output file
    output_file = f"{skill_dir}.skill"

    print(f"Packaging {skill_dir}...")

    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add all files from the skill directory
            for root, dirs, files in os.walk(skill_path):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(skill_path)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")

        print(f"✓ Successfully created {output_file}")

        # Show file size
        size = Path(output_file).stat().st_size
        if size < 1024:
            size_str = f"{size}B"
        elif size < 1024 * 1024:
            size_str = f"{size / 1024:.1f}KB"
        else:
            size_str = f"{size / (1024 * 1024):.1f}MB"

        print(f"  Size: {size_str}")
        return True

    except Exception as e:
        print(f"Error packaging skill: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 package_skill.py <skill_directory>")
        print("\nExample: python3 package_skill.py hoi4-modifier-maker")
        sys.exit(1)

    skill_dir = sys.argv[1]
    success = package_skill(skill_dir)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
