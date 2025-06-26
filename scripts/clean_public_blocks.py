
import os
import shutil

TARGET_DIR = "public/umg_blocks"
LOG_FILE = "public_cleanup_log.txt"

def delete_all_json_blocks():
    deleted = []
    for root, dirs, files in os.walk(TARGET_DIR, topdown=False):
        for file in files:
            if file.endswith(".json"):
                fpath = os.path.join(root, file)
                os.remove(fpath)
                deleted.append(fpath)
        for d in dirs:
            dirpath = os.path.join(root, d)
            if not os.listdir(dirpath):  # if folder is now empty
                os.rmdir(dirpath)
                deleted.append(dirpath)

    with open(LOG_FILE, "w", encoding="utf-8") as log:
        for line in deleted:
            log.write(line + "\n")
    print(f"🧹 Deleted {len(deleted)} items from {TARGET_DIR}")
    return deleted

if __name__ == "__main__":
    delete_all_json_blocks()
