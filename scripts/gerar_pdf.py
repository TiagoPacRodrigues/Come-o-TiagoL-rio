#!/usr/bin/env python3
"""Gera PDFs com a identidade da Lírio do Vale a partir de relatórios em Markdown.

Uso: python3 scripts/gerar_pdf.py docs/relatorios/1-site.md [outros.md ...]
O PDF sai ao lado do .md. Requer pandoc e Chromium.
"""
import html, os, re, subprocess, sys, tempfile, datetime

CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
MESES = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
@page { size: A4; margin: 16mm 15mm 18mm 15mm; }
:root { --marrom:#7A4A1E; --ouro:#FBC32D; --bronze:#A07030; --creme:#FBF6EC; --linha:#E8DFCF; --tinta:#2b2b2b; }
* { box-sizing: border-box; }
body { font-family: 'Montserrat', Arial, sans-serif; color: var(--tinta); font-size: 9.6pt; line-height: 1.55; margin: 0; }
.capa { height: 262mm; display:flex; flex-direction:column; page-break-after: always; background: var(--creme); border-radius: 6px; overflow:hidden; }
.capa .faixa { background: var(--marrom); height: 22mm; display:flex; align-items:center; padding: 0 14mm; color:#fff; font-weight:700; letter-spacing:3px; font-size:8.5pt; text-transform:uppercase; }
.capa .faixa span { color: var(--ouro); margin-right:8px; }
.capa .meio { flex:1; padding: 30mm 14mm 0 14mm; }
.capa img.logo { width: 62mm; max-height:none; margin-bottom: 18mm !important; display:block !important; }
.capa h1 { font-size: 30pt; color: var(--marrom); line-height:1.1; margin: 0 0 6mm 0; border:0; padding:0; page-break-before: avoid; }
.capa .sub { font-size: 13pt; color:#5b4a3a; max-width: 150mm; }
.capa .ouro { width: 40mm; height: 3mm; background: var(--ouro); margin: 10mm 0; border-radius:2px; }
.capa .info { font-size: 9.5pt; color:#6d5d4d; }
.capa .rodape { background: var(--ouro); padding: 6mm 14mm; font-size: 8.5pt; color: var(--marrom); font-weight:600; }
h1 { font-size: 17pt; color: var(--marrom); border-bottom: 3px solid var(--ouro); padding-bottom: 4px; margin: 0 0 10px 0; page-break-before: always; page-break-after: avoid; }
.capa + h1, .capa + * h1:first-child { page-break-before: avoid; }
h2 { font-size: 12.5pt; color: var(--marrom); margin: 18px 0 6px; page-break-after: avoid; }
h3 { font-size: 10.5pt; color: var(--bronze); margin: 14px 0 4px; page-break-after: avoid; }
p { margin: 6px 0; }
strong { color: #1d1d1d; }
a { color: var(--marrom); text-decoration: none; word-break: break-word; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8pt; background: #F3ECDD; padding: 1px 4px; border-radius: 3px; word-break: break-all; }
blockquote { margin: 10px 0; padding: 8px 12px; background: #FFF8E1; border-left: 4px solid var(--ouro); border-radius: 0 4px 4px 0; page-break-inside: avoid; }
blockquote p { margin: 3px 0; }
table { border-collapse: collapse; width: 100%; font-size: 8.4pt; margin: 8px 0 12px; }
th { background: var(--marrom); color: #fff; text-align: left; padding: 5px 6px; font-weight: 600; }
td { border-bottom: 1px solid var(--linha); padding: 5px 6px; vertical-align: top; }
tr { page-break-inside: avoid; }
tr:nth-child(even) td { background: var(--creme); }
ul, ol { padding-left: 18px; margin: 6px 0; }
li { margin: 3px 0; }
img { max-width: 100%; max-height: 105mm; width: auto; display: block; margin: 8px auto; border: 1px solid var(--linha); border-radius: 4px; page-break-inside: avoid; }
.cor, .capa img.logo { display:inline-block; border:0; margin:0 4px 0 0; }
figure { margin: 10px 0 14px; page-break-inside: avoid; text-align:center; }
figure img { max-height: 120mm; }
figcaption { font-size: 8pt; color: #7a6a5a; margin-top: 3px; font-style: italic; }
.cor { display:inline-block; width: 12px; height: 12px; border-radius: 3px; vertical-align: middle; margin-right: 4px; }
hr { border:0; border-top:1px solid var(--linha); }
"""


def build(md_path):
    src = open(md_path, encoding="utf-8").read()
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", src, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        src = src[m.end():]
    body = subprocess.run(["pandoc", "-f", "gfm+raw_html", "-t", "html5"], input=src,
                          capture_output=True, text=True, check=True).stdout
    hoje = datetime.date.today()
    data = f"{hoje.day} de {MESES[hoje.month - 1]} de {hoje.year}"
    base = os.path.abspath(os.path.dirname(md_path))
    logo = os.path.join(base, "img", "logo.png")
    capa = f"""
<div class="capa">
  <div class="faixa"><span>✦</span> Lírio do Vale · Marketing</div>
  <div class="meio">
    {'<img class="logo" src="file://' + logo + '">' if os.path.exists(logo) else ''}
    <h1>{html.escape(meta.get('titulo', ''))}</h1>
    <div class="sub">{html.escape(meta.get('subtitulo', ''))}</div>
    <div class="ouro"></div>
    <div class="info"><b>Fonte:</b> {html.escape(meta.get('plataforma', ''))}<br><b>Data:</b> {data}<br>Preparado pelo Agente de Marketing (Claude) para a equipe da Lírio do Vale</div>
  </div>
  <div class="rodape">Documento interno · análise sincera e baseada no que foi possível verificar</div>
</div>"""
    doc = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<base href="file://{base}/"><title>{html.escape(meta.get('titulo', ''))}</title><style>{CSS}</style></head>
<body>{capa}{body}</body></html>"""
    out_pdf = os.path.splitext(md_path)[0] + ".pdf"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(doc)
        tmp = f.name
    args = [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
            "--virtual-time-budget=8000", f"--print-to-pdf={out_pdf}"]
    if os.environ.get("HTTPS_PROXY"):
        args.append(f"--proxy-server={os.environ['HTTPS_PROXY']}")
    subprocess.run(args + [f"file://{tmp}"], capture_output=True, check=True)
    os.unlink(tmp)
    print(out_pdf)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        build(p)
