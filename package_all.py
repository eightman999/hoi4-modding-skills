#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def main():
    skills_dir = Path("skills")
    if not skills_dir.exists() or not skills_dir.is_dir():
        print("Error: 'skills' directory not found.")
        return

    # Find all subdirectories in 'skills'
    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]

    print(f"Found {len(skill_dirs)} skills to package.")

    for skill_dir in sorted(skill_dirs):
        # Run package_skill.py for each directory
        cmd = ["python3", "package_skill.py", str(skill_dir)]
        print(f"Executing: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # Print stdout, keeping it clean
            for line in result.stdout.splitlines():
                if line.strip():
                    print(f"  {line}")
        else:
            print(f"Failed to package {skill_dir.name}:")
            print(result.stderr)

if __name__ == "__main__":
    main()
