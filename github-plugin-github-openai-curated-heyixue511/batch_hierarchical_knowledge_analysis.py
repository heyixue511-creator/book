from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(r"C:\Users\lenovo\Documents\Codex\2026-05-29")
BOOK_CHAPTER_DIR = ROOT / "书籍专著" / "_章节拆分"
JOURNAL_DIR = ROOT / "期刊文献"
OUTPUT_DIR = ROOT / "层级知识体系分析输出"

BOOK_OUT = OUTPUT_DIR / "书籍专著章节"
JOURNAL_OUT = OUTPUT_DIR / "期刊文献"
MANIFEST = OUTPUT_DIR / "analysis_manifest.json"

BAD_NAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")

STOP_WORDS_EN = {
    "the", "and", "for", "with", "that", "this", "from", "into", "have", "has", "are",
    "was", "were", "not", "but", "they", "their", "which", "there", "then", "than",
    "also", "such", "more", "these", "those", "been", "being", "can", "could", "would",
    "should", "may", "might", "will", "what", "when", "where", "who", "how", "about",
    "all", "some", "one", "new", "many", "much", "most", "other", "only", "over", "under",
    "between", "through", "within", "without", "during", "before", "after", "because",
    "design", "history", "chapter", "figure", "figures", "table", "source", "copyright",
    "image", "images", "jpg", "jpeg", "png", "tif", "tiff", "gif", "pdf",
    "und", "der", "des", "die", "das", "den", "dem", "ein", "eine", "einer", "eines",
    "von", "mit", "aus", "auf", "für", "oder", "als", "ist", "sind", "im", "am", "zu",
    "les", "une", "plus", "pour", "par", "dans", "avec", "sur", "aux", "des", "est",
    "sont", "qui", "que", "mais", "comme", "ses", "son", "che", "del", "della",
}

STOP_WORDS_ZH = {
    "我们", "这些", "这种", "一个", "一种", "以及", "因为", "但是", "可以", "可能", "认为",
    "通过", "进行", "出现", "没有", "不同", "其中", "之后", "之前", "相关", "已经", "为了",
    "作为", "它们", "他们", "人们", "需要", "具有", "包括", "使用", "开始", "这个", "这些",
    "能够", "文本", "来源", "原始文件", "识别方式",
}

DOMAIN_TERMS = {
    "设计本体与问题域": [
        "设计", "design", "function", "functional", "功能", "问题", "problem", "solution",
        "user", "用户", "需求", "need", "use", "使用", "artifact", "物", "产品", "product",
        "人类", "human", "生活", "life", "experience", "体验",
    ],
    "历史语境与社会机制": [
        "历史", "history", "modern", "modernism", "现代", "century", "世纪", "movement",
        "运动", "culture", "文化", "society", "社会", "political", "政治", "economic",
        "经济", "industrial", "工业", "revolution", "革命", "war", "战争", "gender", "阶级",
        "class", "nation", "国家",
    ],
    "技术思维与制造逻辑": [
        "技术", "technology", "tool", "工具", "machine", "机器", "production", "生产",
        "manufacturing", "制造", "craft", "工艺", "material", "材料", "process", "流程",
        "system", "系统", "structure", "结构", "construction", "构造", "engineering", "工程",
    ],
    "材料媒介与形式语言": [
        "材料", "material", "medium", "媒介", "form", "形式", "style", "风格", "color",
        "色彩", "typography", "字体", "graphic", "平面", "visual", "视觉", "image", "图像",
        "symbol", "符号", "ornament", "装饰", "pattern", "纹样", "aesthetic", "审美",
    ],
    "方法过程与研究范式": [
        "方法", "method", "research", "研究", "process", "过程", "thinking", "思维",
        "creativity", "创造", "creative", "protocol", "实验", "model", "模型", "framework",
        "框架", "analysis", "分析", "knowledge", "知识", "learning", "学习", "practice", "实践",
    ],
    "人物机构与案例网络": [
        "designer", "设计师", "architect", "建筑师", "artist", "艺术家", "company", "公司",
        "school", "学院", "press", "出版社", "museum", "博物馆", "bauhaus", "包豪斯",
        "case", "案例", "work", "作品", "project", "项目",
    ],
}

CONCEPT_CANDIDATES = {
    "广义设计": ["广义设计", "broad definition", "design as"],
    "问题解决": ["问题解决", "problem solving", "problem-solution", "problem/solution"],
    "功能主义": ["功能主义", "functionalism", "function"],
    "身体延伸": ["身体延伸", "extension of the body"],
    "系统集成": ["系统集成", "system integration", "integrated", "integration"],
    "标准化": ["标准化", "standardization", "standardized"],
    "材料转化": ["材料转化", "material transformation", "transformative"],
    "视觉传达": ["视觉传达", "visual communication", "visual"],
    "符号系统": ["符号系统", "symbol system", "sign", "symbol"],
    "社会分工": ["社会分工", "division of labor", "specialization"],
    "设计思维": ["设计思维", "design thinking", "designerly"],
    "协同演化": ["co-evolution", "coevolution", "协同演化"],
    "创造性": ["creativity", "creative", "创造性", "创造"],
    "研究范式": ["research", "methodology", "paradigm", "研究范式"],
}


@dataclass
class SourceDoc:
    kind: str
    source_path: Path
    source_group: str
    doc_title: str
    out_path: Path


def long_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def read_text(path: Path) -> str:
    with open(long_path(path), "rb") as handle:
        data = handle.read()
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(long_path(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def sha1_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8", errors="ignore")).hexdigest()


def safe_name(value: str, fallback: str, limit: int = 88) -> str:
    name = BAD_NAME_CHARS.sub("_", value).strip(" ._")
    name = re.sub(r"\s+", " ", name)
    if not name:
        name = fallback
    if len(name) > limit:
        name = name[:limit].rstrip(" ._")
    return name


def strip_markdown(text: str) -> str:
    text = CODE_FENCE_RE.sub(" ", text)
    text = IMAGE_RE.sub(" ", text)
    text = LINK_RE.sub(r"\1", text)
    text = re.sub(r"^>\s?.*$", " ", text, flags=re.M)
    text = re.sub(r"[#*_`~|>\[\]{}]", " ", text)
    return text


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            title = match.group(2).strip(" #")
            if title:
                return title[:120]
    return fallback


def extract_headings(text: str, limit: int = 20) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            title = match.group(2).strip(" #")
            if title and title not in headings:
                headings.append(title)
        if len(headings) >= limit:
            break
    return headings


def tokenize(text: str) -> list[str]:
    plain = strip_markdown(text).lower()
    tokens: list[str] = []
    tokens.extend(t for t in re.findall(r"[a-z][a-z\-]{2,}", plain) if t not in STOP_WORDS_EN)
    cjk_chunks = re.findall(r"[\u4e00-\u9fff]{2,}", plain)
    for chunk in cjk_chunks:
        if chunk in STOP_WORDS_ZH:
            continue
        if len(chunk) <= 6:
            tokens.append(chunk)
        else:
            for size in (4, 3, 2):
                for i in range(0, len(chunk) - size + 1):
                    piece = chunk[i:i + size]
                    if piece not in STOP_WORDS_ZH:
                        tokens.append(piece)
    return tokens


def word_frequency(text: str, top_n: int = 40) -> list[tuple[str, int]]:
    counter = Counter(tokenize(text))
    return counter.most_common(top_n)


def score_dimensions(text: str, freqs: list[tuple[str, int]]) -> list[tuple[str, int, list[str]]]:
    lowered = strip_markdown(text).lower()
    freq_map = dict(freqs)
    results: list[tuple[str, int, list[str]]] = []
    for dimension, terms in DOMAIN_TERMS.items():
        hits: list[str] = []
        score = 0
        for term in terms:
            term_l = term.lower()
            count = lowered.count(term_l)
            if count:
                score += count
                hits.append(term)
            score += freq_map.get(term_l, 0)
        results.append((dimension, score, hits[:8]))
    return sorted(results, key=lambda item: item[1], reverse=True)


def extract_concepts(text: str) -> list[str]:
    lowered = strip_markdown(text).lower()
    concepts = []
    for concept, variants in CONCEPT_CANDIDATES.items():
        if any(v.lower() in lowered for v in variants):
            concepts.append(concept)
    return concepts


def extract_entities(text: str, max_items: int = 30) -> list[str]:
    plain = strip_markdown(text)
    entities: Counter[str] = Counter()

    for match in re.findall(r"\b(?:[A-Z][A-Za-zÀ-ÿ'.-]+(?:\s+|,\s*|&\s*)){1,5}[A-Z][A-Za-zÀ-ÿ'.-]+\b", plain):
        item = re.sub(r"\s+", " ", match.strip(" ,"))
        if len(item) < 4 or item.lower() in STOP_WORDS_EN:
            continue
        if item.lower().startswith(("the ", "this ", "that ")):
            continue
        entities[item] += 1

    for term_list in DOMAIN_TERMS.values():
        for term in term_list:
            if re.search(r"[\u4e00-\u9fff]", term) and term in plain:
                entities[term] += plain.count(term)

    for concept in CONCEPT_CANDIDATES:
        if concept in plain:
            entities[concept] += plain.count(concept)

    for year in re.findall(r"(?:公元前\s*)?\d{3,4}\s*年?|(?:19|20)\d{2}", plain):
        entities[year.strip()] += 1

    return [item for item, _ in entities.most_common(max_items)]


def first_meaningful_paragraph(text: str, max_len: int = 420) -> str:
    for para in re.split(r"\n\s*\n", text):
        cleaned = strip_markdown(para)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        lowered = cleaned.lower()
        if any(marker in lowered for marker in [
            "faculty of", "department of", "university", "copyright", "all rights reserved",
            "digitized by", "original edition", "isbn", "doi ",
        ]) and len(cleaned) < 500:
            continue
        if len(cleaned) >= 80 and not cleaned.lower().startswith(("来源", "原始文件")):
            return cleaned[:max_len]
    cleaned = re.sub(r"\s+", " ", strip_markdown(text)).strip()
    return cleaned[:max_len]


def infer_knowledge_points(headings: list[str], freqs: list[tuple[str, int]], entities: list[str], concepts: list[str]) -> list[str]:
    points: list[str] = []
    for heading in headings[:8]:
        points.append(f"围绕“{heading}”展开的章节性知识单元。")
    for term, count in freqs[:12]:
        if len(term) >= 2:
            points.append(f"高频主题“{term}”（出现约 {count} 次）构成文本关注点。")
    for concept in concepts[:8]:
        points.append(f"概念线索“{concept}”可作为抽象分析节点。")
    for entity in entities[:8]:
        points.append(f"实体/案例“{entity}”提供事实支撑。")
    seen: set[str] = set()
    unique: list[str] = []
    for point in points:
        if point not in seen:
            unique.append(point)
            seen.add(point)
    return unique[:24]


def make_core_thesis(title: str, top_dims: list[tuple[str, int, list[str]]], summary: str) -> str:
    dim = top_dims[0][0] if top_dims else "设计知识"
    return (
        f"本文档以“{title}”为中心，主要落在“{dim}”问题域中。"
        f"文本通过概念论述、案例材料与历史/实践语境，组织出关于设计对象、设计行动及其社会意义的知识链条。"
        f"从首段语义看，其核心关注可概括为：{summary}"
    )


def make_report(doc: SourceDoc, text: str) -> tuple[str, dict]:
    title = extract_title(text, doc.doc_title)
    headings = extract_headings(text)
    freqs = word_frequency(text)
    dimensions = score_dimensions(text, freqs)
    concepts = extract_concepts(text)
    entities = extract_entities(text)
    summary = first_meaningful_paragraph(text)
    knowledge_points = infer_knowledge_points(headings, freqs, entities, concepts)
    char_count = len(re.sub(r"\s+", "", strip_markdown(text)))
    line_count = len(text.splitlines())
    word_count = len(tokenize(text))

    active_dimensions = [item for item in dimensions if item[1] > 0][:4]
    if not active_dimensions:
        active_dimensions = dimensions[:3]

    report: list[str] = []
    report.append(f"# {title}：文本分析与层级知识体系")
    report.append("")
    report.append("## 0. 文档信息")
    report.append(f"- 文档类型：{doc.kind}")
    report.append(f"- 来源组：{doc.source_group}")
    report.append(f"- 原始文件：`{doc.source_path}`")
    report.append(f"- 文本行数：{line_count}")
    report.append(f"- 有效字符数：{char_count}")
    report.append(f"- 关键词/词段数：{word_count}")
    report.append("")

    report.append("## 1. 定量概览")
    report.append("| 高频词/词段 | 次数 |")
    report.append("| --- | ---: |")
    for term, count in freqs[:25]:
        report.append(f"| {term} | {count} |")
    report.append("")

    report.append("## 2. 语义分析")
    report.append("### 核心主旨")
    report.append(make_core_thesis(title, active_dimensions, summary))
    report.append("")
    report.append("### 关键主题")
    for dimension, score, hits in active_dimensions:
        hit_text = "、".join(hits[:6]) if hits else "由标题、词频和段落语义综合判断"
        report.append(f"- **{dimension}**：匹配强度 {score}；主要线索：{hit_text}。")
    report.append("")

    report.append("## 3. 概念、知识元与实体")
    report.append("### 核心概念")
    if concepts:
        for concept in concepts:
            report.append(f"- {concept}")
    else:
        report.append("- 未检测到高置信度预置概念，建议结合原文人工补充抽象概念。")
    report.append("")
    report.append("### 具体知识点")
    for point in knowledge_points:
        report.append(f"- {point}")
    report.append("")
    report.append("### 关键实体")
    if entities:
        for entity in entities[:30]:
            report.append(f"- {entity}")
    else:
        report.append("- 未提取到明显实体。")
    report.append("")

    report.append("## 4. 层级化知识体系")
    report.append("### 第一级：核心研究主题")
    report.append(f"**{title}中的设计知识结构：文本主题、案例证据与概念框架的组织关系**")
    report.append("")
    report.append("### 第二级：核心维度")
    for idx, (dimension, score, hits) in enumerate(active_dimensions, start=1):
        report.append(f"{idx}. **{dimension}**")
        report.append(f"   - 维度说明：由本文件中的关键词、标题结构和实体分布共同支撑，匹配强度 {score}。")
    report.append("")
    report.append("### 第三级与第四级：议题和知识要素")
    for idx, (dimension, score, hits) in enumerate(active_dimensions, start=1):
        terms = hits[:5] or [term for term, _ in freqs[:5]]
        related_entities = entities[(idx - 1) * 5: idx * 5] or entities[:5]
        report.append(f"#### 维度 {idx}：{dimension}")
        report.append(f"- **议题 {idx}.1：文本中的核心问题域**")
        report.append(f"  - 知识要素：{', '.join(terms) if terms else '需人工补充'}")
        report.append(f"- **议题 {idx}.2：案例、实体与证据链**")
        report.append(f"  - 知识要素：{', '.join(related_entities) if related_entities else '需人工补充'}")
        report.append(f"- **议题 {idx}.3：可迁移的分析概念**")
        report.append(f"  - 知识要素：{', '.join(concepts[:6]) if concepts else '从高频词与段落主题中继续归纳'}")
    report.append("")

    report.append("## 5. 可用于后续知识库的结构化条目")
    report.append("```json")
    report.append(json.dumps({
        "title": title,
        "document_type": doc.kind,
        "source_group": doc.source_group,
        "core_dimensions": [d[0] for d in active_dimensions],
        "concepts": concepts,
        "entities": entities[:20],
        "top_terms": freqs[:20],
    }, ensure_ascii=False, indent=2))
    report.append("```")
    report.append("")

    report.append("## 6. 方法说明")
    report.append("本报告沿用“数据化-语义提取-知识解构-层级建构”的路径生成：先统计词频和标题结构，再抽取概念、实体与知识点，最后按核心主题、维度、议题、知识要素四层组织。")
    report.append("")

    metadata = {
        "kind": doc.kind,
        "source": str(doc.source_path),
        "output": str(doc.out_path),
        "title": title,
        "group": doc.source_group,
        "lines": line_count,
        "chars": char_count,
        "terms": word_count,
        "dimensions": [d[0] for d in active_dimensions],
        "concepts": concepts,
        "entities": entities[:20],
        "sha1": sha1_text(text),
    }
    return "\n".join(report), metadata


def collect_book_docs() -> list[SourceDoc]:
    docs: list[SourceDoc] = []
    for path in sorted(BOOK_CHAPTER_DIR.rglob("*.md"), key=lambda p: str(p).lower()):
        if path.name in {"00_章节索引.md", "章节拆分报告.md"}:
            continue
        if path.name == "chapters_manifest.json":
            continue
        if path.parent == BOOK_CHAPTER_DIR:
            continue
        book_group = path.parent.name
        out_group = safe_name(book_group, "book", 72)
        out_name = safe_name(path.stem, "chapter", 72) + "_知识体系分析.md"
        docs.append(SourceDoc("书籍章节", path, book_group, path.stem, BOOK_OUT / out_group / out_name))
    return docs


def collect_journal_docs() -> list[SourceDoc]:
    docs: list[SourceDoc] = []
    for path in sorted(JOURNAL_DIR.glob("*.md"), key=lambda p: p.name.lower()):
        out_name = safe_name(path.stem, "journal", 100) + "_知识体系分析.md"
        docs.append(SourceDoc("期刊文献", path, "期刊文献", path.stem, JOURNAL_OUT / out_name))
    return docs


def write_indexes(results: list[dict]) -> None:
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for item in results:
        by_kind[item["kind"]].append(item)

    total_lines = [
        "# 层级知识体系分析总报告",
        "",
        f"- 分析文档总数：{len(results)}",
        f"- 书籍章节：{len(by_kind.get('书籍章节', []))}",
        f"- 期刊文献：{len(by_kind.get('期刊文献', []))}",
        f"- 输出目录：`{OUTPUT_DIR}`",
        "",
        "## 维度分布",
        "",
    ]
    dim_counter = Counter(dim for item in results for dim in item["dimensions"])
    total_lines.append("| 维度 | 文档数 |")
    total_lines.append("| --- | ---: |")
    for dim, count in dim_counter.most_common():
        total_lines.append(f"| {dim} | {count} |")
    total_lines.append("")
    total_lines.append("## 输出索引")
    total_lines.append("")
    total_lines.append("- [书籍专著章节索引](书籍专著章节_索引.md)")
    total_lines.append("- [期刊文献索引](期刊文献_索引.md)")
    write_text(OUTPUT_DIR / "总报告.md", "\n".join(total_lines) + "\n")

    for kind, filename in [("书籍章节", "书籍专著章节_索引.md"), ("期刊文献", "期刊文献_索引.md")]:
        lines = [f"# {kind}层级知识体系分析索引", "", "| 序号 | 标题 | 维度 | 报告 |", "| ---: | --- | --- | --- |"]
        for idx, item in enumerate(by_kind.get(kind, []), start=1):
            rel = os.path.relpath(item["output"], OUTPUT_DIR).replace("\\", "/")
            dims = "、".join(item["dimensions"][:3])
            title = str(item["title"]).replace("|", "\\|")
            lines.append(f"| {idx} | {title} | {dims} | [{Path(item['output']).name}]({rel}) |")
        write_text(OUTPUT_DIR / filename, "\n".join(lines) + "\n")

    csv_path = OUTPUT_DIR / "analysis_manifest.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(long_path(csv_path), "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["kind", "group", "title", "source", "output", "lines", "chars", "dimensions", "concepts", "sha1"])
        writer.writeheader()
        for item in results:
            writer.writerow({
                "kind": item["kind"],
                "group": item["group"],
                "title": item["title"],
                "source": item["source"],
                "output": item["output"],
                "lines": item["lines"],
                "chars": item["chars"],
                "dimensions": "；".join(item["dimensions"]),
                "concepts": "；".join(item["concepts"]),
                "sha1": item["sha1"],
            })


def prepare_output_dir() -> None:
    if OUTPUT_DIR.exists():
        if MANIFEST.exists():
            shutil.rmtree(long_path(OUTPUT_DIR))
        else:
            raise SystemExit(f"输出目录已存在且缺少生成清单，为避免覆盖用户文件已停止：{OUTPUT_DIR}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    prepare_output_dir()
    docs = collect_book_docs() + collect_journal_docs()
    results: list[dict] = []
    for idx, doc in enumerate(docs, start=1):
        text = read_text(doc.source_path)
        report, metadata = make_report(doc, text)
        write_text(doc.out_path, report)
        results.append(metadata)
        if idx % 100 == 0 or idx == len(docs):
            print(f"processed {idx}/{len(docs)}")

    write_text(MANIFEST, json.dumps(results, ensure_ascii=False, indent=2))
    write_indexes(results)
    print(f"done: {len(results)} reports")
    print(f"output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
