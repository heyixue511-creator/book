import os
import re
import shutil
from pathlib import Path

def shorten_filename(filename):
    """缩短文件名，移除冗余信息"""
    name = filename
    
    name = re.sub(r'\s*\(z-library\.sk,\s*1lib\.sk,\s*z-lib\.sk\)', '', name)
    
    name = re.sub(r'\s*--.*?Annas Archive', '', name)
    name = re.sub(r'\s*--.*?Annas\s*Archiv', '', name)
    name = re.sub(r'\s*--.*?Annas\s*Arc', '', name)
    name = re.sub(r'\s*--.*?Annas\s*A', '', name)
    
    name = re.sub(r'\s*--\s*isbn\d*\s*[a-zA-Z0-9]+', '', name)
    name = re.sub(r'\s*--\s*[a-f0-9]{32}', '', name)
    name = re.sub(r'\s*--\s*[a-f0-9]{40}', '', name)
    
    name = re.sub(r'\s*\(Review by.*?\)', '', name)
    name = re.sub(r'\s*\(ed\.\)', '', name)
    name = re.sub(r'\s*\(eds\.\)', '', name)
    
    name = re.sub(r'\s*--\s*\d{4}\s*--.*?(?=--)', '', name)
    name = re.sub(r'\s*--\s*\d{4}\s*$', '', name)
    
    name = name.strip()
    if name.endswith('.md'):
        name = name[:-3]
    
    return name

def get_safe_length_path(base_path, folder_name, file_ext):
    """计算安全的目标路径长度"""
    dest_folder = Path(base_path) / folder_name
    dest_file = dest_folder / (folder_name + file_ext)
    
    max_length = 240
    current_length = len(str(dest_file))
    
    if current_length <= max_length:
        return folder_name, current_length
    
    available = max_length - len(str(Path(base_path))) - len(file_ext) - 50
    return folder_name[:available], current_length

md_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\MD")
journal_path = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\期刊文献")
book_path = Path(r"\\?\C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")

journal_files = set(f.name for f in journal_path.iterdir() if f.is_file())
md_files = [f for f in md_path.iterdir() if f.is_file() and f.name not in journal_files]

print(f"Total files to process: {len(md_files)}")

copied = 0
skipped = 0
errors = 0

for md_file in md_files:
    try:
        original_name = md_file.stem
        short_name = shorten_filename(original_name)
        
        if len(short_name) < 10:
            short_name = original_name[:100]
        
        safe_name, path_len = get_safe_length_path(str(book_path), short_name, '.md')
        
        dest_folder = book_path / safe_name
        dest_file = dest_folder / (safe_name + '.md')
        
        if dest_file.exists():
            skipped += 1
            continue
        
        dest_folder.mkdir(exist_ok=True)
        
        try:
            shutil.copy2(str(md_file), str(dest_file))
            copied += 1
        except Exception as copy_error:
            if 'long path' in str(copy_error).lower() or '206' in str(copy_error):
                safe_name = safe_name[:min(len(safe_name), 80)]
                dest_folder = book_path / safe_name
                dest_file = dest_folder / (safe_name + '.md')
                dest_folder.mkdir(exist_ok=True)
                shutil.copy2(str(md_file), str(dest_file))
                copied += 1
            else:
                errors += 1
                
    except Exception as e:
        errors += 1
        print(f"Error processing {original_name[:50]}: {str(e)[:50]}")

print(f"\nSummary:")
print(f"  Copied: {copied}")
print(f"  Skipped (already exists): {skipped}")
print(f"  Errors: {errors}")
print(f"  Total: {copied + skipped + errors}")
