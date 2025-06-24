import os
import json

SOURCE_DIR = "incoming_master"
DEST_ROOT = "public/umg_blocks"

def safe_filename(name):
    return name.strip().replace(" ", "_").replace("-", "_").lower()

def unpack_blocks():
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory '{SOURCE_DIR}' not found.")
        return

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".json")]
    if not files:
        print("No JSON files found in incoming_master.")
        return

    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                blocks = json.load(f)
            except json.JSONDecodeError:
                print(f"Invalid JSON in {filename}, skipping.")
                continue

        for block in blocks:
            category = block.get("category")
            block_id = block.get("block_id")
            if not category or not block_id:
                print(f"Skipping block with missing category or block_id: {block}")
                continue

            dest_dir = os.path.join(DEST_ROOT, *category.split("/"))
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, f"{block_id}.json")

            if os.path.exists(dest_path):
                print(f"File already exists, skipping: {dest_path}")
                continue

            with open(dest_path, "w", encoding="utf-8") as out_file:
                json.dump(block, out_file, indent=2)
                print(f"✅ Created {dest_path}")

if __name__ == "__main__":
    unpack_blocks()
