from pathlib import Path

book_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

root_md_files = list(book_path.glob("*.md"))
folders = [f for f in book_path.iterdir() if f.is_dir()]

print(f"MD files in root: {len(root_md_files)}")
print(f"Folders: {len(folders)}")

if root_md_files:
    print("\nMD files in root directory:")
    for f in root_md_files[:10]:
        print(f"  - {f.name}")
