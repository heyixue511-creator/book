from pathlib import Path

book_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

folders = [f for f in book_path.iterdir() if f.is_dir()]
multi_file_folders = []

for folder in folders:
    files = list(folder.glob("*.md"))
    if len(files) > 1:
        multi_file_folders.append({
            'folder': folder.name,
            'files': [f.name for f in files]
        })

print(f"Folders with multiple files: {len(multi_file_folders)}")

if multi_file_folders:
    print("\nDetails:")
    for item in multi_file_folders:
        print(f"\n{item['folder'][:80]}:")
        for fname in item['files']:
            print(f"  - {fname[:80]}")
