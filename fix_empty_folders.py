import os
from pathlib import Path

base_path = Path(r"\\?\C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

folders = [f for f in base_path.iterdir() if f.is_dir()]
empty_folders = []

for folder in folders:
    md_files = list(folder.glob("*.md"))
    if len(md_files) == 0:
        empty_folders.append(folder)
        print(f"Empty folder: {folder.name}")

print(f"\nTotal empty folders: {len(empty_folders)}")

for folder in empty_folders:
    try:
        folder.rmdir()
        print(f"Deleted empty folder: {folder.name}")
    except Exception as e:
        print(f"Could not delete {folder.name}: {e}")
