from pathlib import Path

book_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")
md_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\MD")
journal_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\期刊文献")

folders = [f for f in book_path.iterdir() if f.is_dir()]
md_files_in_book = list(book_path.rglob("*.md"))

journal_files = set(f.name for f in journal_path.iterdir() if f.is_file())
all_md_files = [f for f in md_path.iterdir() if f.is_file() and f.name.endswith('.md')]
md_to_copy = [f for f in all_md_files if f.name not in journal_files]

print(f"MD directory files: {len(all_md_files)}")
print(f"Journal files to exclude: {len(journal_files)}")
print(f"Files to copy (should be 333): {len(md_to_copy)}")
print(f"\nBooks directory:")
print(f"  Folders: {len(folders)}")
print(f"  MD files: {len(md_files_in_book)}")
print(f"\nDifference: {len(md_to_copy) - len(md_files_in_book)} files unaccounted for")
