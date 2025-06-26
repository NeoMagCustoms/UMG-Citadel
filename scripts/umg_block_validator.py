
import os
import json
import pandas as pd

# Root directory to scan
ROOT = "umg_blocks"

# Required fields in each block
REQUIRED_FIELDS = ["block_id", "molt_type", "ledger", "label", "category"]

def scan_blocks():
    rows = []
    for dirpath, _, filenames in os.walk(ROOT):
        for filename in filenames:
            if filename.endswith(".json"):
                full_path = os.path.join(dirpath, filename)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    row = {
                        "file": full_path,
                        "missing_fields": [],
                        "invalid_block_id": False
                    }
                    for field in REQUIRED_FIELDS:
                        if field not in data:
                            row["missing_fields"].append(field)
                    if "block_id" in data and (" " in data["block_id"] or data["block_id"] == ""):
                        row["invalid_block_id"] = True
                    rows.append(row)
                except Exception as e:
                    rows.append({
                        "file": full_path,
                        "missing_fields": ["PARSE_ERROR"],
                        "invalid_block_id": True
                    })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = scan_blocks()
    df.to_csv("block_validation_report.csv", index=False)
    print("✅ Block validation report saved to block_validation_report.csv")
