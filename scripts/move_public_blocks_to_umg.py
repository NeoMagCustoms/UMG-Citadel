
import os
import shutil
import csv

SOURCE_ROOT = "public/umg_blocks"
DEST_ROOT = "umg_blocks"
LOG_FILE = "move_log.csv"

def move_blocks():
    moved = []
    for root, dirs, files in os.walk(SOURCE_ROOT):
        for file in files:
            if file.endswith(".json"):
                rel_path = os.path.relpath(root, SOURCE_ROOT)
                dest_dir = os.path.join(DEST_ROOT, rel_path)
                os.makedirs(dest_dir, exist_ok=True)

                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)

                shutil.move(src_file, dest_file)
                moved.append((src_file, dest_file))

    with open(LOG_FILE, "w", newline="", encoding="utf-8") as log:
        writer = csv.writer(log)
        writer.writerow(["source", "destination"])
        writer.writerows(moved)

    print(f"✅ Moved {len(moved)} block files from public/umg_blocks to umg_blocks/")
    return moved

if __name__ == "__main__":
    move_blocks()
