import os
import json

SOURCE_DIR = "incoming_master"
DEST_ROOT  = "public/umg_blocks"

def safe_filename(name):
    return name.strip().replace(" ", "_").replace("-", "_").lower()

def unpack_blocks(dry_run=False):
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory '{SOURCE_DIR}' not found.")
        return

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".json")]
    if not files:
        print("No JSON files found in incoming_master.")
        return

    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as fp:
            try:
                blocks = json.load(fp)
            except json.JSONDecodeError:
                print(f"[Error] Invalid JSON in {filename}, skipping.")
                continue

        for block in blocks:
            if not isinstance(block, dict):
                print(f"[Skip] Invalid block in {filename}: not a dict.")
                continue

            category_path = block.get("category", "").strip("/")
            if not category_path:
                print(f"[Skip] Missing category in {filename}, skipping block.")
                continue

            dest_dir = os.path.join(DEST_ROOT, category_path)
            os.makedirs(dest_dir, exist_ok=True)

            dest_path = os.path.join(dest_dir, f"{safe_filename(block['block_id'])}.json")
            if os.path.exists(dest_path):
                print(f"[Skip] File already exists: {dest_path}")
                continue

            if dry_run:
                print(f"[DryRun] Would write: {dest_path}")
            else:
                with open(dest_path, "w", encoding="utf-8") as out_file:
                    json.dump(block, out_file, indent=2)
                print(f"[Write] {dest_path}")

if __name__ == "__main__":
    unpack_blocks()
