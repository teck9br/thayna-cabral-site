"""Gera os favicons a partir de assets/simbolo-gold.png com traço engrossado conforme o tamanho.
Uso: python gerar_favicon.py [pasta_para_previa]. Depois, suba o ?v= dos links de favicon."""
import sys
from PIL import Image, ImageDraw, ImageFilter

src = site = out = None
from pathlib import Path
src = str(Path(__file__).parent); site = src + "/site"; out = sys.argv[1] if len(sys.argv) > 1 else None
sim = Image.open(src + '/assets/simbolo-gold.png').convert('RGBA')
sim = sim.crop(sim.getbbox())
alpha = sim.split()[3]
NAVY = (11, 17, 32, 255)
GOLD = (222, 188, 112)


def icon(size, pad, stroke_px, radius=0.22, bg=True):
    """stroke_px: espessura extra do traço, em pixels do tamanho final."""
    k = 8  # supersample
    S = size * k
    inner = round(S * (1 - 2 * pad))
    r = min(inner / sim.width, inner / sim.height)
    a = alpha.resize((round(sim.width * r), round(sim.height * r)), Image.LANCZOS)
    a = a.point(lambda v: 255 if v > 60 else 0)
    n = max(1, round(stroke_px * k)) | 1
    if n > 1:
        a = a.filter(ImageFilter.MaxFilter(n))
    canvas = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    if bg:
        m = Image.new('L', (S, S), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, S - 1, S - 1], radius=round(S * radius), fill=255)
        canvas.paste(Image.new('RGBA', (S, S), NAVY), (0, 0), m)
    gold = Image.new('RGBA', a.size, GOLD + (255,))
    canvas.paste(gold, ((S - a.width) // 2, (S - a.height) // 2), a)
    return canvas.resize((size, size), Image.LANCZOS)


variants = {
    16: icon(16, 0.10, 0.9),
    32: icon(32, 0.11, 1.0),
    48: icon(48, 0.12, 1.1),
    64: icon(64, 0.12, 1.2),
}
variants[64].save(site + '/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
                  append_images=[variants[16], variants[32], variants[48]])
icon(192, 0.15, 1.6).save(site + '/favicon-192.png')
icon(512, 0.15, 3.0).save(site + '/logo-512.png')
icon(180, 0.17, 1.6, radius=0).convert('RGB').save(site + '/apple-touch-icon.png')  # iOS arredonda sozinho

# prévia
if out is None:
    sys.exit(0)
sheet = Image.new('RGB', (900, 330), (255, 255, 255))
dark = Image.new('RGB', (900, 70), (32, 33, 36))
x = 10
for s in [16, 32, 48]:
    im = variants[s]
    big = im.resize((s * 4, s * 4), Image.NEAREST); sheet.paste(big, (x, 10), big)
    sheet.paste(im, (x, 210), im); dark.paste(im, (x, 10), im); x += s * 4 + 20
a = Image.open(site + '/favicon-192.png'); sheet.paste(a, (x, 10), a)
b = Image.open(site + '/apple-touch-icon.png'); sheet.paste(b, (x + 210, 10))
sheet.paste(dark, (0, 260))
sheet.save(out + '/fav2.png')
