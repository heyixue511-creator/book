from pathlib import Path
from collections import Counter

book_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

all_files = list(book_path.rglob("*.md"))
file_names = [f.name for f in all_files]

name_counts = Counter(file_names)

duplicates = {name: count for name, count in name_counts.items() if count > 1}

print(f"Total md files: {len(all_files)}")
print(f"Unique file names: {len(name_counts)}")
print(f"Duplicate files: {len(duplicates)}")

if duplicates:
    print("\nDuplicate files:")
    for name, count in duplicates.items():
        print(f"  - {name}: {count} copies")
