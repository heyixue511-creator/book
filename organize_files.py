import os
import shutil
from pathlib import Path

base_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

md_files = list(base_path.glob("*.md"))

for md_file in md_files:
    folder_name = md_file.stem
    dest_folder = base_path / folder_name
    
    try:
        dest_folder.mkdir(exist_ok=True)
        dest_file = dest_folder / md_file.name
        shutil.move(str(md_file), str(dest_file))
        print(f"Moved: {md_file.name}")
    except Exception as e:
        print(f"Error moving {md_file.name}: {e}")

print(f"\nProcessed {len(md_files)} files")
