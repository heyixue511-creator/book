from pathlib import Path

md_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\MD")
journal_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\期刊文献")
book_base = r"\\?\C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著"

journal_files = set(f.name for f in journal_path.iterdir() if f.is_file())
md_files = [f for f in md_path.iterdir() if f.is_file() and f.name not in journal_files]

max_path_length = 260
long_files = []

for md_file in md_files:
    folder_name = md_file.stem
    dest_folder = Path(book_base) / folder_name
    dest_file = dest_folder / md_file.name
    
    total_path_length = len(str(dest_file))
    if total_path_length > max_path_length:
        long_files.append({
            'name': md_file.name,
            'folder': folder_name,
            'path_length': total_path_length
        })

print(f"Total files in MD: {len(md_files)}")
print(f"Journal files excluded: {len(journal_files)}")
print(f"Files with path > 260 chars: {len(long_files)}")

if long_files:
    print("\nLongest 20 files:")
    long_files.sort(key=lambda x: x['path_length'], reverse=True)
    for f in long_files[:20]:
        print(f"  Length {f['path_length']}: {f['name'][:60]}...")
