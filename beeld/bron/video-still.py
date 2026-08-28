# -*- coding: utf-8 -*-
"""16:9 still in de stijl van het aangeleverde gifje — valt in als de GIF niet door de API komt."""
import base64, pathlib
BRON = pathlib.Path(__file__).parent; UIT = BRON.parent
CREAM="#FBF2EA"; NAVY="#1E2A35"; LIME="#86C63F"; GRIJS="#5C6B75"

def f(n): return "data:font/woff2;base64," + base64.b64encode((BRON/n).read_bytes()).decode()

HTML = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:AntonL;src:url({a}) format('woff2');font-display:block;}}
@font-face{{font-family:AntonX;src:url({b}) format('woff2');font-display:block;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1280px;height:720px;}}
body{{background:{cream};font-family:AntonL,AntonX,Impact,sans-serif;}}
.c{{position:relative;width:1280px;height:720px;display:flex;flex-direction:column;
   align-items:center;justify-content:center;padding-bottom:44px;}}
.elke{{color:{lime};font-size:34px;letter-spacing:.34em;text-transform:uppercase;margin-bottom:14px;}}
.wo{{color:{navy};font-size:152px;line-height:.9;letter-spacing:.006em;text-transform:uppercase;}}
.sub{{color:{grijs};font-size:50px;line-height:1.1;margin-top:26px;letter-spacing:.004em;}}
.url{{position:absolute;left:64px;bottom:56px;color:{navy};font-size:46px;letter-spacing:.003em;}}
</style></head><body><div class="c">
  <span class="elke">&bull;&nbsp; Elke &nbsp;&bull;</span>
  <span class="wo">Woensdag</span>
  <span class="sub">gratis Ai-avond in Almelo</span>
  <span class="url">aimelo.nl/aanmelden/2/</span>
</div><script>document.body.dataset.klaar='1';</script></body></html>"""

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    pg = b.new_page(viewport={"width":1280,"height":720}, device_scale_factor=1)
    t = BRON/"video-still.html"
    t.write_text(HTML.format(a=f("anton-latin.woff2"), b=f("anton-latinext.woff2"),
                             cream=CREAM, navy=NAVY, lime=LIME, grijs=GRIJS), encoding="utf-8")
    pg.goto("file://"+str(t)); pg.wait_for_function("document.body.dataset.klaar==='1'"); pg.wait_for_timeout(200)
    pg.screenshot(path=str(UIT/"woensdag-16x9.png")); b.close()
    print("beeld/woensdag-16x9.png")
