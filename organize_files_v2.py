import os
import shutil
from pathlib import Path

base_path = Path(r"\\?\C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

md_files = list(base_path.glob("*.md"))
processed = 0
errors = 0

for md_file in md_files:
    folder_name = md_file.stem
    dest_folder = base_path / folder_name
    
    try:
        dest_folder.mkdir(exist_ok=True)
        dest_file = dest_folder / md_file.name
        
        if not dest_file.exists():
            shutil.move(str(md_file), str(dest_file))
            processed += 1
        else:
            print(f"File already exists: {md_file.name[:50]}...")
            
    except Exception as e:
        errors += 1
        print(f"Error: {str(e)[:100]}")

print(f"\nProcessed: {processed} files")
print(f"Errors: {errors} files")
