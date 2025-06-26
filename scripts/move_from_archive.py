
import os
import shutil
from pathlib import Path

# Define paths
archive_dir = Path("incoming_master/archive_master")
incoming_dir = Path("incoming_master")

# Ensure incoming directory exists
incoming_dir.mkdir(parents=True, exist_ok=True)

# Move all .json files
moved = []
for json_file in archive_dir.glob("*.json"):
    target_path = incoming_dir / json_file.name
    shutil.move(str(json_file), str(target_path))
    moved.append((json_file.name, str(target_path)))

# Report moved files
if moved:
    print("✅ Moved files:")
    for src, dest in moved:
        print(f"  - {src} → {dest}")
else:
    print("⚠️ No .json files found in archive_master to move.")
