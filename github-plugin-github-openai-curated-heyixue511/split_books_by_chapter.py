from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著")
OUT_DIR = BASE_DIR / "_章节拆分"

BAD_NAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
HEADING_RE = re.compile(r"^(#{1,3})\s*(.*?)\s*$")
IMAGE_RE = re.compile(r"(!\[[^\]]*\]\()([^)]+)(\))")

FRONT_MATTER_WORDS = {
    "contents",
    "content",
    "table of contents",
    "illustrations",
    "figures",
    "tables",
    "preface",
    "acknowledgements",
    "acknowledgments",
    "introduction",
    "bibliography",
    "references",
    "notes",
    "index",
    "copyright",
    "目录",
    "前言",
    "序言",
    "序",
    "致谢",
    "参考文献",
    "索引",
    "版权",
}

NUMBER_WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty"
)


@dataclass
class SourceDoc:
    book_title: str
    path: Path
    digest: str


@dataclass
class Heading:
    line_no: int
    level: int
    title: str
    confidence: int
    reason: str


def long_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def read_bytes(path: Path) -> bytes:
    with open(long_path(path), "rb") as handle:
        return handle.read()


def read_text(path: Path) -> str:
    data = read_bytes(path)
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(long_path(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def sha1(path: Path) -> str:
    digest = hashlib.sha1()
    with open(long_path(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_size(path: Path) -> int:
    return os.stat(long_path(path)).st_size


def clean_title(raw: str) -> str:
    title = raw.strip()
    title = re.sub(r"\s+", " ", title)
    title = title.strip("#*`_[](){} \t\r\n")
    return title.strip()


def safe_name(raw: str, fallback: str, limit: int = 72) -> str:
    name = clean_title(raw) or fallback
    name = BAD_NAME_CHARS.sub("_", name)
    name = re.sub(r"\s+", " ", name).strip(" ._")
    if not name:
        name = fallback
    if len(name) > limit:
        name = name[:limit].rstrip(" ._")
    return name


def is_probably_noise(title: str) -> bool:
    if not title or len(title) < 2:
        return True
    if title in {"#", "-", ".", ":", "*", "$", "$$", "**"}:
        return True
    useful = sum(1 for ch in title if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")
    if useful == 0:
        return True
    if useful / max(len(title), 1) < 0.35:
        return True
    if not re.search(r"[\u4e00-\u9fff]", title) and re.search(r"[#$\\{}]", title):
        return True
    letters = [ch for ch in title if ch.isalpha()]
    if letters:
        ascii_letters = [ch for ch in letters if ch.isascii()]
        if (
            len(ascii_letters) / max(len(letters), 1) > 0.8
            and not any(ch.islower() for ch in ascii_letters)
            and not re.match(r"^(chapter|part|book)\b", title.lower())
        ):
            return True
        if len(ascii_letters) / max(len(letters), 1) > 0.8:
            vowels = sum(1 for ch in ascii_letters if ch.lower() in "aeiouy")
            if vowels / max(len(ascii_letters), 1) < 0.18:
                return True
    if len(title) <= 3 and not re.search(r"[\u4e00-\u9fff]", title):
        return True
    return False


def weak_fallback_title(title: str) -> bool:
    if re.search(r"[\u4e00-\u9fff]", title):
        return False
    letters = [ch for ch in title if ch.isalpha()]
    if not letters:
        return True
    if not any(ch.islower() for ch in letters if ch.isascii()) and not re.match(r"^(chapter|part|book)\b", title.lower()):
        return True
    if len(letters) >= 8 and "".join(letters).upper() == "".join(letters):
        return True
    symbol_count = sum(1 for ch in title if not (ch.isalnum() or ch.isspace() or ch in "-,.:;()'’&"))
    return symbol_count / max(len(title), 1) > 0.12


def is_front_matter(title: str) -> bool:
    lowered = title.lower().strip(" .:：")
    if lowered in FRONT_MATTER_WORDS:
        return True
    return lowered.startswith(("appendix", "notes", "references", "bibliography", "index"))


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def heading_confidence(level: int, title: str) -> tuple[int, str]:
    text = clean_title(title)
    lowered = text.lower()
    if is_probably_noise(text) or is_front_matter(text):
        return 0, "noise-or-front-matter"

    if re.match(rf"^(chapter|part|book)\s+(\d+|[ivxlcdm]+|{NUMBER_WORDS})\b", lowered):
        return 95, "english-chapter-marker"
    if re.match(r"^第[一二三四五六七八九十百千万〇零\d]+[章节篇部编讲卷]\b", text):
        return 95, "chinese-chapter-marker"
    if re.match(r"^[一二三四五六七八九十]+[、.．]\s*\S.{2,}$", text):
        return 85, "chinese-numbered-title"
    if re.match(r"^\d{1,2}[.、．]\s+\S.{3,}$", text):
        return 82, "numbered-title"
    if re.match(r"^\d{1,2}\s+[A-Za-z][A-Za-z ,:'’&-]{3,}$", text):
        return 82, "english-number-title"
    if level == 1 and 4 <= len(text) <= 90 and not weak_fallback_title(text):
        return 70, "level-one-title"
    if level == 2 and 5 <= len(text) <= 90 and re.search(r"[A-Za-z\u4e00-\u9fff]", text) and not weak_fallback_title(text):
        return 50, "level-two-title"
    return 0, "weak-heading"


def parse_headings(lines: list[str]) -> list[Heading]:
    headings: list[Heading] = []
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line.rstrip("\n\r"))
        if not match:
            continue
        level = len(match.group(1))
        title = clean_title(match.group(2))
        confidence, reason = heading_confidence(level, title)
        headings.append(Heading(idx, level, title, confidence, reason))
    return headings


def choose_chapter_starts(headings: list[Heading]) -> tuple[list[Heading], str]:
    strong = [h for h in headings if h.confidence >= 80]
    if 2 <= len(strong) <= 80:
        return strong, "强章节标记"

    h1 = [h for h in headings if h.level == 1 and h.confidence >= 70]
    if 2 <= len(h1) <= 80:
        return h1, "一级标题"

    h2 = [h for h in headings if h.level <= 2 and h.confidence >= 50]
    if 2 <= len(h2) <= 60:
        return h2, "一二级标题"

    if len(strong) > 80:
        h1_strong = [h for h in strong if h.level == 1]
        if 2 <= len(h1_strong) <= 80:
            return h1_strong, "一级强章节标记"

    return [], "未识别到稳定章节标题"


def rewrite_image_paths(text: str, source_dir: Path, chapter_dir: Path) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(2).strip()
        lowered = target.lower()
        if re.match(r"^[a-z][a-z0-9+.-]*:", lowered) or target.startswith(("/", "\\")):
            return match.group(0)
        source_target = (source_dir / target).resolve()
        rel = os.path.relpath(source_target, chapter_dir.resolve()).replace("\\", "/")
        return f"{match.group(1)}{rel}{match.group(3)}"

    return IMAGE_RE.sub(repl, text)


def collect_sources() -> list[SourceDoc]:
    sources: list[SourceDoc] = []
    seen_hashes: set[str] = set()

    for book_dir in sorted([p for p in BASE_DIR.iterdir() if p.is_dir() and p.name != OUT_DIR.name], key=lambda p: p.name.lower()):
        md_files = sorted(book_dir.glob("*.md"), key=lambda p: p.name.lower())
        if not md_files:
            continue
        preferred = max(md_files, key=file_size)
        digest = sha1(preferred)
        seen_hashes.add(digest)
        sources.append(SourceDoc(book_dir.name, preferred, digest))

    for md_file in sorted(BASE_DIR.glob("*.md"), key=lambda p: p.name.lower()):
        digest = sha1(md_file)
        if digest in seen_hashes:
            continue
        seen_hashes.add(digest)
        sources.append(SourceDoc(md_file.stem, md_file, digest))

    return sources


def split_source(source: SourceDoc, index: int) -> dict:
    text = read_text(source.path)
    lines = text.splitlines(keepends=True)
    headings = parse_headings(lines)
    starts, method = choose_chapter_starts(headings)
    if starts and has_cjk(source.book_title):
        cjk_starts = sum(1 for heading in starts if has_cjk(heading.title))
        if cjk_starts / max(len(starts), 1) < 0.5:
            starts = []
            method = "未识别到稳定章节标题"

    folder = OUT_DIR / f"{index:03d}_{safe_name(source.book_title, f'book_{index:03d}', 60)}"
    folder.mkdir(parents=True, exist_ok=True)

    outputs: list[dict] = []
    if not starts:
        filename = "01_全文.md"
        body = rewrite_image_paths(text, source.path.parent, folder)
        out_path = folder / filename
        write_text(out_path, f"# {source.book_title}\n\n> 原始文件：{source.path}\n> 拆分状态：未识别到稳定章节标题，保留为全文。\n\n{body}")
        outputs.append({"title": "全文", "file": filename, "lines": len(lines)})
    else:
        if starts[0].line_no > 8:
            front_text = "".join(lines[: starts[0].line_no]).strip()
            if front_text:
                filename = "00_前言与目录.md"
                body = rewrite_image_paths(front_text + "\n", source.path.parent, folder)
                write_text(folder / filename, f"# 前言与目录\n\n> 来源：{source.book_title}\n> 原始文件：{source.path}\n\n{body}")
                outputs.append({"title": "前言与目录", "file": filename, "lines": starts[0].line_no})

        for chapter_index, start in enumerate(starts, start=1):
            end_line = starts[chapter_index].line_no if chapter_index < len(starts) else len(lines)
            title = start.title or f"章节 {chapter_index:02d}"
            filename = f"{chapter_index:02d}_{safe_name(title, f'chapter_{chapter_index:02d}', 80)}.md"
            chapter_text = "".join(lines[start.line_no:end_line]).strip() + "\n"
            body = rewrite_image_paths(chapter_text, source.path.parent, folder)
            write_text(folder / filename, f"> 来源：{source.book_title}\n> 原始文件：{source.path}\n> 识别方式：{method}\n\n{body}")
            outputs.append({"title": title, "file": filename, "lines": end_line - start.line_no})

    index_lines = [
        f"# {source.book_title}",
        "",
        f"- 原始文件：`{source.path}`",
        f"- 识别方式：{method}",
        f"- 输出文档数：{len(outputs)}",
        "",
        "## 文档清单",
        "",
    ]
    for item in outputs:
        index_lines.append(f"- [{item['title']}]({item['file']})（约 {item['lines']} 行）")
    write_text(folder / "00_章节索引.md", "\n".join(index_lines) + "\n")

    return {
        "book": source.book_title,
        "source": str(source.path),
        "folder": str(folder),
        "method": method,
        "documents": len(outputs),
        "chapters": len(starts),
        "fallback": not bool(starts),
    }


def write_report(results: list[dict]) -> None:
    total_docs = sum(item["documents"] for item in results)
    fallback_count = sum(1 for item in results if item["fallback"])
    lines = [
        "# 书籍专著章节拆分报告",
        "",
        f"- 原始书籍数：{len(results)}",
        f"- 生成 Markdown 文档数：{total_docs}",
        f"- 未识别稳定章节、保留全文的书籍数：{fallback_count}",
        f"- 输出目录：`{OUT_DIR}`",
        "",
        "## 明细",
        "",
        "| 序号 | 书名 | 识别方式 | 输出数 | 输出目录 |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for idx, item in enumerate(results, start=1):
        folder_name = Path(item["folder"]).name
        book = str(item["book"]).replace("|", "\\|")
        lines.append(f"| {idx} | {book} | {item['method']} | {item['documents']} | `{folder_name}` |")
    write_text(OUT_DIR / "章节拆分报告.md", "\n".join(lines) + "\n")

    machine_report = OUT_DIR / "chapters_manifest.json"
    write_text(machine_report, json.dumps(results, ensure_ascii=False, indent=2))


def main() -> None:
    if not BASE_DIR.exists():
        raise SystemExit(f"目录不存在：{BASE_DIR}")
    if OUT_DIR.exists():
        if (OUT_DIR / "chapters_manifest.json").exists():
            shutil.rmtree(long_path(OUT_DIR))
        else:
            raise SystemExit(f"输出目录已存在且缺少生成清单，为避免覆盖用户文件已停止：{OUT_DIR}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    sources = collect_sources()
    results: list[dict] = []
    for idx, source in enumerate(sources, start=1):
        results.append(split_source(source, idx))
        if idx % 25 == 0:
            print(f"processed {idx}/{len(sources)}")
    write_report(results)
    print(f"done: {len(results)} books, {sum(item['documents'] for item in results)} markdown files")
    print(f"fallback full-text books: {sum(1 for item in results if item['fallback'])}")
    print(f"output: {OUT_DIR}")


if __name__ == "__main__":
    main()
