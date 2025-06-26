
import os
import shutil
import json

def rename_malformed_json_files():
    fixed_files = []
    for root, _, files in os.walk("incoming_master"):
        for fname in files:
            if fname.endswith(".jso"):
                correct_name = fname + "n"
                old_path = os.path.join(root, fname)
                new_path = os.path.join(root, correct_name)
                os.rename(old_path, new_path)
                fixed_files.append((old_path, new_path))
    return fixed_files

def move_loading_placeholders():
    repaired = []
    src_dir = "umg_blocks/analytics/9B_event_tracking"
    dst_dir = "archive_master/_placeholder_blocks"
    os.makedirs(dst_dir, exist_ok=True)
    for fname in os.listdir(src_dir):
        if "loading" in fname.lower():
            src = os.path.join(src_dir, fname)
            dst = os.path.join(dst_dir, fname)
            shutil.move(src, dst)
            repaired.append((src, dst))
    return repaired

def flag_gitkeep_only_folders():
    flagged = []
    for root, dirs, files in os.walk("umg_blocks/business/10_training"):
        if all(f == ".gitkeep" for f in files):
            flagged.append(root)
    return flagged

def rebuild_block_index():
    block_paths = []
    for root, _, files in os.walk("umg_blocks"):
        for fname in files:
            if fname.endswith(".json"):
                rel_path = os.path.join(root, fname)
                block_paths.append(rel_path)
    with open("vaults/block_index.json", "w") as f:
        json.dump(block_paths, f, indent=2)
    return len(block_paths)

if __name__ == "__main__":
    renamed = rename_malformed_json_files()
    moved = move_loading_placeholders()
    gitkeep_flags = flag_gitkeep_only_folders()
    count = rebuild_block_index()

    print("🔁 Renamed malformed files:", renamed)
    print("📦 Moved placeholder blocks:", moved)
    print("📋 Gitkeep-only folders flagged:", gitkeep_flags)
    print(f"🧾 block_index.json rebuilt with {count} entries")
