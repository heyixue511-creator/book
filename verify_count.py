from pathlib import Path

book_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

folders = [f for f in book_path.iterdir() if f.is_dir()]
md_files_in_folders = list(book_path.rglob("*.md"))

empty_folders = []
files_per_folder = {}

for folder in folders:
    files = list(folder.glob("*.md"))
    files_per_folder[folder.name] = len(files)
    if len(files) == 0:
        empty_folders.append(folder.name)

print(f"Total folders: {len(folders)}")
print(f"Total md files: {len(md_files_in_folders)}")
print(f"Empty folders: {len(empty_folders)}")

if empty_folders:
    print("\nEmpty folders:")
    for name in empty_folders[:10]:
        print(f"  - {name}")

print("\nFolders with files:")
folders_with_files = {k: v for k, v in files_per_folder.items() if v > 0}
print(f"  {len(folders_with_files)} folders have files")
