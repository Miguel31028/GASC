"""Gera o relatório de análise a partir do modelo do IPCA.

Uso: python3 build.py <modelo.docx> <pasta_diagramas> <pasta_mockups> <saida.docx>
Faz duas passagens: a segunda preenche os números de página dos índices
a partir da renderização em PDF (LibreOffice) da primeira.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Report  # noqa: E402
from front import front  # noqa: E402
from cap1_2 import cap1, cap2  # noqa: E402
from cap3 import cap3, RF  # noqa: E402
from cap4 import cap4, UCS  # noqa: E402
from cap5 import cap5  # noqa: E402
from cap6_9 import cap6, cap7, cap8, cap9, bibliografia, anexos  # noqa: E402
from cap_mockups import cap_mockups  # noqa: E402


def build(tpl, D, M, out, pages=None):
    r = Report(tpl, pages)
    fig_anchor, tab_anchor = front(r)
    r.strip_template_body()
    cap1(r, D); cap2(r, D); cap3(r, D); cap4(r, D); cap5(r, D)
    cap_mockups(r, D, M)
    cap6(r, D)
    cap7(r, D); cap8(r, D); cap9(r, D)
    r.end_chapters()
    bibliografia(r)
    r._section_break(r.sect[10])
    anexos(r, D, UCS, RF)
    r.build_toc()
    r.build_list_index(fig_anchor, r.figs, 'Figura')
    r.build_list_index(tab_anchor, r.tabs, 'Tabela')
    r.enable_update_fields()
    r.save(out)
    return r


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def compute_pages(pdf, r):
    """Determina a página impressa (rodapé) de cada título, figura e tabela."""
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    texts, folio = [], []
    for i in range(1, n + 1):
        t = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', pdf, '-'], capture_output=True, text=True).stdout
        lines = [norm(l) for l in t.split('\n') if l.strip()]
        texts.append(lines)
        folio.append(lines[-1] if lines and re.fullmatch(r'\d+', lines[-1]) else None)
    first = r.headings[0]
    start = next(i for i, lines in enumerate(texts) if f'{first[1]} {first[2]}' in lines)
    pages = {}

    def find(pred, from_idx):
        for i in range(from_idx, n):
            if any(pred(l) for l in texts[i]):
                return i
        return None

    def page_of(i):
        if folio[i]:
            return int(folio[i])
        j = i  # página sem número (primeira de secção): usa a seguinte com número
        while j < n and not folio[j]:
            j += 1
        return int(folio[j]) - (j - i) if j < n else i - start + 1

    cur = start
    for lvl, num, title, bm in r.headings:
        target = norm(f'{num} {title}' if num else title)
        i = find(lambda l: l == target or (l.startswith(target[:60]) and '....' not in l and not re.search(r'\d+$', l[len(target):])), cur)
        if i is not None:
            pages[bm] = page_of(i)
            cur = i
    for kind, items in (('Figura', r.figs), ('Tabela', r.tabs)):
        cur = start
        for num, text, bm in items:
            pref = norm(f'{kind} {num}: {text}')[:50]
            i = find(lambda l: l.startswith(pref) and '....' not in l, cur)
            if i is not None:
                pages[bm] = page_of(i)
                cur = i
    missing = [bm for *_, bm in r.headings if bm not in pages] + [bm for *_, bm in r.figs + r.tabs if bm not in pages]
    return pages, missing


def to_pdf(docx_path, outdir):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx_path],
                   capture_output=True, check=True, timeout=600)
    return os.path.join(outdir, os.path.splitext(os.path.basename(docx_path))[0] + '.pdf')


if __name__ == '__main__':
    tpl, D, M, out = sys.argv[1:5]
    tmp = tempfile.mkdtemp()
    first = os.path.join(tmp, 'passagem1.docx')
    r = build(tpl, D, M, first)
    pages, missing = compute_pages(to_pdf(first, tmp), r)
    print(f'títulos: {len(r.headings)}, figuras: {len(r.figs)}, tabelas: {len(r.tabs)}; sem página: {len(missing)}')
    build(tpl, D, M, out, pages)
    print('gerado', out)
