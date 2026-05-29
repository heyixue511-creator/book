import os
import shutil
from pathlib import Path

md_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\MD")
journal_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\期刊文献")
book_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

journal_files = set(f.name for f in journal_path.iterdir() if f.is_file())
md_files = [f for f in md_path.iterdir() if f.is_file() and f.name not in journal_files]

print(f"Total files in MD: {len(list(md_path.iterdir()))}")
print(f"Journal files to exclude: {len(journal_files)}")
print(f"Files to copy: {len(md_files)}")

copied = 0
failed = 0

for md_file in md_files:
    folder_name = md_file.stem
    dest_folder = book_path / folder_name
    
    try:
        dest_folder.mkdir(exist_ok=True)
        dest_file = dest_folder / md_file.name
        
        if not dest_file.exists():
            shutil.copy2(str(md_file), str(dest_file))
            copied += 1
        else:
            print(f"Already exists: {md_file.name[:50]}...")
    except Exception as e:
        failed += 1
        print(f"Failed: {md_file.name[:50]}... - {str(e)[:50]}")

print(f"\nSuccessfully copied: {copied} files")
print(f"Failed: {failed} files")
