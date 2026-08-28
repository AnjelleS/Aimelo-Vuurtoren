# -*- coding: utf-8 -*-
"""Rendert de AiMelo-posters op 1080x1350 (4:5) met de tijd erin."""
import base64, json, pathlib, sys

BRON = pathlib.Path(__file__).parent
UIT  = BRON.parent

CREAM = "#FBF2EA"; PANEL = "#F0EFEA"; NAVY = "#16293A"; LIME = "#86C63F"

def font_datauri(naam):
    b = (BRON / naam).read_bytes()
    return "data:font/woff2;base64," + base64.b64encode(b).decode()

POSTERS = [
  dict(bestand="dag-01", kop1=[("GEEN",1.0),("MARKETINGBUDGET?",1.0)],
       kop2=[("WEL WERK",1.0),("DAT GEZIEN MAG WORDEN.",0.60)]),
  dict(bestand="dag-02", kop1=[("JE MOOISTE WERK",1.0),("HANGT BIJ JE KLANT.",0.92)],
       kop2=[("NIET OP JE FEED.",1.0)]),
  dict(bestand="dag-03", kop1=[("JE TUINEN",1.0),("ZIJN PRACHTIG.",0.82)],
       kop2=[("MAAR WIE",1.0),("ZIET ZE?",1.0)]),
  dict(bestand="dag-04", kop1=[("JE BROOD",1.0),("VERKOOPT ZICHZELF.",0.80)],
       kop2=[("JE VERHAAL",1.0),("NOG NIET.",1.0)]),
  dict(bestand="dag-05", kop1=[("JE KASTEN",1.0),("ZIJN MAATWERK.",0.84)],
       kop2=[("JE MARKETING",1.0),("NOG NIET.",1.0)]),
  dict(bestand="dag-06", kop1=[("MORGEN",1.0),("AVOND.",1.0)],
       kop2=[("NOG","1.0"),("PLEK.",1.0)]),
  dict(bestand="dag-07", kop1=[("VANAVOND.",1.0)],
       kop2=[("LOOP GEWOON",1.0),("BINNEN.",1.0)]),
]
# los typefoutje in dag-06 herstellen
POSTERS[5]["kop2"] = [("NOG",1.0),("PLEK.",1.0)]

TEMPLATE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:AntonL;src:url({f_lat}) format('woff2');font-weight:400;font-display:block;}}
@font-face{{font-family:AntonX;src:url({f_ext}) format('woff2');font-weight:400;font-display:block;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
body{{background:{cream};font-family:AntonL,AntonX,Impact,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
.canvas{{position:relative;width:{W}px;height:{H}px;}}
.panel{{position:absolute;left:38px;top:{PT}px;right:38px;bottom:{PB}px;background:{panel};
  padding:64px 58px 64px;display:flex;flex-direction:column;justify-content:center;}}
.blok{{display:flex;flex-direction:column;}}
.regel{{color:{navy};text-transform:uppercase;line-height:.97;letter-spacing:.004em;white-space:nowrap;}}
.rule{{height:15px;width:296px;background:{lime};margin:30px 0 34px;flex:none;}}
.spacer{{height:96px;flex:none;}}
.voet{{display:flex;flex-direction:column;gap:2px;}}
.voet .elke{{color:{lime};font-size:31px;letter-spacing:.30em;line-height:1.25;text-transform:uppercase;}}
.voet .gratis{{color:{lime};font-size:58px;line-height:1.02;text-transform:uppercase;letter-spacing:.006em;}}
.voet .tijd{{color:{navy};font-size:52px;line-height:1.06;text-transform:uppercase;letter-spacing:.01em;}}
.voet .plaats{{color:{navy};font-size:52px;line-height:1.06;text-transform:uppercase;letter-spacing:.01em;}}
.url{{color:{navy};font-size:58px;line-height:1.06;letter-spacing:.003em;margin-top:26px;white-space:nowrap;}}
.bar{{position:absolute;left:38px;bottom:52px;width:104px;height:11px;background:{lime};}}
.hair{{position:absolute;left:38px;right:38px;bottom:34px;height:3px;background:{navy};}}
</style></head><body>
<div class="canvas">
  <div class="panel">
    <div class="blok" id="k1">{kop1}</div>
    <div class="rule"></div>
    <div class="blok" id="k2">{kop2}</div>
    <div class="spacer"></div>
    <div class="voet">
      <span class="elke">&bull; Elke woensdag &bull;</span>
      <span class="gratis">Gratis AI-avond</span>
      <span class="tijd">18.00 &ndash; 21.00 uur</span>
      <span class="plaats">in Almelo</span>
      <span class="url" id="url">aimelo.nl/aanmelden/2/</span>
    </div>
  </div>
  <div class="bar"></div><div class="hair"></div>
</div>
<script>
// Schaal elk kopblok zo dat de breedste regel precies de maat vult.
function fit(id, maxBase){{
  const el = document.getElementById(id);
  const regels = [...el.querySelectorAll('.regel')];
  if(!regels.length) return;
  const maat = el.clientWidth;
  let base = maxBase;
  regels.forEach(r => r.style.fontSize = (base * parseFloat(r.dataset.w)) + 'px');
  let ratio = Infinity;
  regels.forEach(r => {{ ratio = Math.min(ratio, maat / r.scrollWidth); }});
  base = Math.min(maxBase, base * ratio);
  regels.forEach(r => r.style.fontSize = (base * parseFloat(r.dataset.w)) + 'px');
}}
fit('k1', {FS}); fit('k2', {FS});
(function(){{
  const u = document.getElementById('url');
  const maat = u.parentElement.parentElement.clientWidth;
  const base = parseFloat(getComputedStyle(u).fontSize);
  if (u.scrollWidth > maat) u.style.fontSize = (base * maat / u.scrollWidth) + 'px';
}})();
document.body.dataset.klaar = '1';
</script></body></html>"""

def regels_html(regels):
    return "".join(
        '<span class="regel" data-w="%s">%s</span>' % (w, t)
        for t, w in regels)

FORMATEN = {
  "4x5":  dict(W=1080, H=1350, PT=52,  PB=118, FS=138),
  "9x16": dict(W=1080, H=1920, PT=180, PB=250, FS=150),
}

def bouw(p, fmt):
    m = FORMATEN[fmt]
    return TEMPLATE.format(
        f_lat=font_datauri("anton-latin.woff2"),
        f_ext=font_datauri("anton-latinext.woff2"),
        cream=CREAM, panel=PANEL, navy=NAVY, lime=LIME,
        kop1=regels_html(p["kop1"]), kop2=regels_html(p["kop2"]), **m)

def main():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        for fmt, m in FORMATEN.items():
            pg = b.new_page(viewport={"width":m["W"],"height":m["H"]}, device_scale_factor=1)
            for p in POSTERS:
                tmp = BRON / ("%s-%s.html" % (p["bestand"], fmt))
                tmp.write_text(bouw(p, fmt), encoding="utf-8")
                pg.goto("file://" + str(tmp))
                pg.wait_for_function("document.body.dataset.klaar === '1'")
                pg.wait_for_timeout(200)
                uit = UIT / ("%s-%s.png" % (p["bestand"], fmt))
                pg.screenshot(path=str(uit))
                print("%-8s %-5s -> %s" % (p["bestand"], fmt, uit.name))
            pg.close()
        b.close()

if __name__ == "__main__":
    main()
