#!/usr/bin/env python3
"""
create_gist_from_blocks.py

Reads a category_<num>_*.json file in incoming_master/, splits each block into
individual JSON files, and uploads them as a multi‑file GitHub Gist.

Usage:
    python scripts/create_gist_from_blocks.py --category 30 --token <GITHUB_TOKEN>

NOTE: Requires the environment variable GITHUB_TOKEN or --token argument with a
personal‑access token that has `gist` scope.
"""

import argparse
import json
import os
import pathlib
import requests
from typing import Dict, Any

GIST_API_URL = "https://api.github.com/gists"


def load_category_file(category: int) -> pathlib.Path:
    root = pathlib.Path(__file__).resolve().parent.parent
    incoming = root / "incoming_master"
    for path in incoming.glob(f"category_{category}_*.json"):
        return path
    raise FileNotFoundError(f"No file found for category {category}")


def split_blocks(path: pathlib.Path) -> Dict[str, str]:
    blocks = json.loads(path.read_text())
    files = {}
    for block in blocks:
        block_id = block.get("block_id", "unnamed_block")
        files[f"{block_id}.json"] = {
            "content": json.dumps(block, indent=2) + "\n"
        }
    return files


def create_gist(files: Dict[str, Any], description: str, token: str) -> str:
    payload = {
        "description": description,
        "public": False,
        "files": files,
    }
    headers = {"Authorization": f"token {token}"}
    resp = requests.post(GIST_API_URL, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()["html_url"]


def main():
    parser = argparse.ArgumentParser(description="Create gist from UMG blocks")
    parser.add_argument("--category", type=int, required=True)
    parser.add_argument("--token", type=str, default=os.getenv("GITHUB_TOKEN"))
    args = parser.parse_args()

    if not args.token:
        raise SystemExit("GitHub token required via --token or GITHUB_TOKEN env var")

    path = load_category_file(args.category)
    gist_files = split_blocks(path)
    url = create_gist(gist_files, f"UMG blocks for category {args.category}", args.token)
    print(f"Created gist: {url}")


if __name__ == "__main__":
    main()
