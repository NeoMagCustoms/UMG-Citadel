
import os
import json
import pandas as pd

ROOT = "umg_blocks"
PLACEHOLDER_PATTERNS = ["loading...", "placeholder", "todo"]

def is_empty_folder(path):
    return not any(fname.endswith(".json") for fname in os.listdir(path))

def is_placeholder_file(file_path):
    try:
        if file_path.endswith(".json"):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return any(str(v).strip().lower() in PLACEHOLDER_PATTERNS for v in data.values())
        elif file_path.endswith(".md") or file_path.endswith(".txt"):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip().lower()
            return any(p in content for p in PLACEHOLDER_PATTERNS)
    except:
        return False
    return False

def scan_repo():
    rows = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        relpath = os.path.relpath(dirpath, ROOT)
        has_gitkeep = any(f == ".gitkeep" for f in filenames)
        json_files = [f for f in filenames if f.endswith(".json")]
        placeholders = [f for f in filenames if is_placeholder_file(os.path.join(dirpath, f))]

        if has_gitkeep and not json_files:
            rows.append({
                "folder": relpath,
                "issue": ".gitkeep only (no JSON)",
                "status": "EMPTY_PLACEHOLDER",
                "suggestion": "Add valid blocks or confirm intentional empty state"
            })
        elif not filenames:
            rows.append({
                "folder": relpath,
                "issue": "Empty folder",
                "status": "UNUSED_FOLDER",
                "suggestion": "Delete or populate with valid content"
            })
        elif placeholders:
            rows.append({
                "folder": relpath,
                "issue": f"Contains placeholder file(s): {', '.join(placeholders)}",
                "status": "INCOMPLETE_BLOCK",
                "suggestion": "Replace placeholders with real content"
            })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = scan_repo()
    df.to_csv("block_repair_queue.csv", index=False)
    print("✅ Repair queue saved to block_repair_queue.csv")
