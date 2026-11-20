"""Optional, one-time BibTeX conversion. Prints Markdown; never edits your site.
Install: python -m pip install bibtexparser==1.4.3 pylatexenc==2.10
Usage:   python scripts/bibtex_to_markdown.py references.bib > imported.md
Review imported.md, then paste the desired entries into PUBLICATIONS.md.
"""
import re
import sys
from pathlib import Path
import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text


def plain(text):
    return ' '.join(LatexNodes2Text().latex_to_text(text or '').split())


def escaped(text):
    return re.sub(r'([\\`*_\[\]<>])', r'\\\1', text)


def render(entries):
    def year(e):
        y = plain(e.get('year', ''))
        return y if re.fullmatch(r'\d{4}', y) else 'Undated'
    def key(e):
        y = year(e)
        return (-int(y) if y.isdigit() else 0, plain(e.get('title', '')).lower())
    lines = []
    previous = None
    for e in sorted(entries, key=key):
        y = year(e)
        if y != previous:
            lines += [f'### {y}', '']
            previous = y
        title = escaped(plain(e.get('title', 'Untitled')))
        url = e.get('url', '').strip()
        if not url and e.get('doi'):
            url = 'https://doi.org/' + e['doi'].strip()
        if not url:
            match = re.search(r'arXiv\s*:?\s*(\d{4}\.\d{4,5}(?:v\d+)?)', e.get('journal', ''), re.I)
            if match:
                url = 'https://arxiv.org/abs/' + match.group(1)
        # Do not turn incomplete arXiv IDs or arbitrary URI schemes into links.
        if not re.match(r'^https?://[^\s<>]+$', url):
            url = ''
        author_names = []
        for name in re.split(r'\s+and\s+', e.get('author', '')):
            name = plain(name)
            if ', ' in name:
                parts = name.split(', ')
                name = ' '.join(parts[1:] + parts[:1])
            name = escaped(name)
            if name in ['Lei Yu', 'Jade Yu', 'Jade (Lei) Yu']:
                name = '**' + name + '**'
            if name:
                author_names.append(name)
        venue = escaped(plain(e.get('booktitle') or e.get('journal') or ''))
        lines += [f"<!-- bibtex: {e.get('ID', '')} -->", f'#### [{title}](<{url}>)' if url else f'#### {title}', ', '.join(author_names)]
        if venue:
            lines += [f'*{venue}*' + (f' · {y}' if y.isdigit() else '')]
        elif y.isdigit():
            lines += [y]
        lines += ['']
    return '\n'.join(lines)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python scripts/bibtex_to_markdown.py references.bib')
    with Path(sys.argv[1]).open(encoding='utf-8') as f:
        database = bibtexparser.load(f)
    if not database.entries:
        raise SystemExit('No BibTeX entries found. Your website has not been changed.')
    print(render(database.entries))
