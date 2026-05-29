from pathlib import Path

base_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

md_files = list(base_path.rglob("*.md"))
folders = [f for f in base_path.iterdir() if f.is_dir()]

print(f"Total md files: {len(md_files)}")
print(f"Total folders: {len(folders)}")

empty_folders = []
files_in_folders = []

for folder in folders:
    folder_files = list(folder.glob("*.md"))
    if len(folder_files) == 0:
        empty_folders.append(folder.name)
    else:
        files_in_folders.append(folder.name)

print(f"Folders with files: {len(files_in_folders)}")
print(f"Empty folders: {len(empty_folders)}")

if len(empty_folders) > 0:
    print("\nEmpty folders:")
    for name in empty_folders[:10]:
        print(f"  - {name[:80]}...")
