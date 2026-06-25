#!/usr/bin/env python3
"""Tiny markdown wiki engine for this repo.

Commands:
  python3 scripts/wiki_engine.py index docs/wiki
  python3 scripts/wiki_engine.py lint docs/wiki
  python3 scripts/wiki_engine.py search docs/wiki "query"
"""
from __future__ import annotations
import sys, re, json
from pathlib import Path
from datetime import date

PAGE_DIRS = ['concepts', 'pipelines', 'projects', 'prompt-libraries', 'checklists', 'raw']

FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
LINK_RE = re.compile(r'\[\[([^\]]+)\]\]')

def parse_fm(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        out[k.strip()] = v.strip().strip('"')
    return out

def pages(wiki: Path):
    for d in PAGE_DIRS:
        p = wiki / d
        if p.exists():
            yield from sorted(p.glob('*.md'))

def slug(path: Path) -> str:
    return path.stem

def title_of(path: Path, text: str, fm: dict) -> str:
    if fm.get('title'):
        return fm['title']
    for line in text.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return path.stem

def build_index(wiki: Path) -> int:
    groups = {d: [] for d in PAGE_DIRS}
    total = 0
    for p in pages(wiki):
        text = p.read_text(encoding='utf-8')
        fm = parse_fm(text)
        title = title_of(p, text, fm)
        summary = ''
        body = FM_RE.sub('', text).strip().splitlines()
        for line in body:
            line = line.strip()
            if line and not line.startswith('#'):
                summary = line[:180]
                break
        groups[p.parent.name].append((title, p.stem, summary))
        total += 1
    out = [
        '# Wiki Index', '',
        f'> Generated: {date.today()} | Total pages: {total}', '',
    ]
    names = {
        'concepts': 'Concepts',
        'pipelines': 'Pipelines',
        'projects': 'Projects',
        'prompt-libraries': 'Prompt Libraries',
        'checklists': 'Checklists',
        'raw': 'Raw Notes',
    }
    for d in PAGE_DIRS:
        out += [f'## {names[d]}', '']
        for title, s, summary in sorted(groups[d], key=lambda x: x[0].lower()):
            out.append(f'- [[{s}]] — {summary}')
        out.append('')
    (wiki / 'index.md').write_text('\n'.join(out), encoding='utf-8')
    return total

def lint(wiki: Path) -> int:
    all_pages = {p.stem: p for p in pages(wiki)}
    problems = []
    inbound = {s: 0 for s in all_pages}
    for p in all_pages.values():
        text = p.read_text(encoding='utf-8')
        fm = parse_fm(text)
        if not fm:
            problems.append(('error', str(p), 'missing YAML frontmatter'))
        for req in ['title','created','updated','type','tags']:
            if req not in fm:
                problems.append(('error', str(p), f'missing frontmatter field: {req}'))
        for link in LINK_RE.findall(text):
            target = link.split('|')[0].strip()
            if target not in all_pages:
                problems.append(('error', str(p), f'broken wikilink: [[{target}]]'))
            else:
                inbound[target] += 1
    for s, n in inbound.items():
        if n == 0 and s not in {'production-checklists'}:
            problems.append(('warn', str(all_pages[s]), 'orphan page: no inbound wikilinks'))
    if problems:
        for sev, p, msg in problems:
            print(f'{sev.upper()}: {p}: {msg}')
        return 1 if any(sev == 'error' for sev,_,_ in problems) else 0
    print('OK: wiki lint passed')
    return 0

def search(wiki: Path, q: str) -> int:
    terms = [t.lower() for t in q.split() if t.strip()]
    hits = []
    for p in pages(wiki):
        text = p.read_text(encoding='utf-8')
        low = text.lower()
        score = sum(low.count(t) for t in terms)
        if score:
            title = title_of(p, text, parse_fm(text))
            hits.append((score, title, p))
    for score, title, p in sorted(hits, reverse=True)[:20]:
        print(f'{score:3d}  {title}  {p}')
    return 0

def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, wiki = argv[1], Path(argv[2])
    if cmd == 'index':
        print(f'indexed {build_index(wiki)} pages')
        return 0
    if cmd == 'lint':
        return lint(wiki)
    if cmd == 'search':
        return search(wiki, ' '.join(argv[3:]))
    print('unknown command', cmd)
    return 2

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
