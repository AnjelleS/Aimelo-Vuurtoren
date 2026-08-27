# AiMelo campagne v1.0 — klaar om aan te zetten

**Gratis AI-avond · woensdag 2 september 2026 · 18.00–21.00 · Moving-In Almelo**

Zeven dagen aanloop over vier kanalen, van vandaag tot en met de avond zelf.
Daarna stopt alles automatisch.

---

## 1. De kalender

| Dag | Datum | LinkedIn *(08:00)* | Instagram · Facebook *(19:00)* | WhatsApp |
|---|---|---|---|---|
| 1 | **do 27 aug** | De oorspronkelijke reden 🎞️ | Geen marketingbudget? | Status + kanaal |
| 2 | vr 28 aug | De vrijheid die volliep | Je mooiste werk hangt bij je klant | Status |
| 3 | za 29 aug | Voor wie al met AI werkt 🎞️ | Je tuinen zijn prachtig | Status |
| 4 | zo 30 aug | Vakmanschap | Je brood verkoopt zichzelf | Status |
| 5 | ma 31 aug | Vraagpost A t/m E | Je kasten zijn maatwerk | Status |
| 6 | di 1 sep | Morgenavond | Morgenavond. Nog plek. | Status + **herinnering 17:00** |
| 7 | **wo 2 sep** | Samen bouwen | Vanavond. Loop gewoon binnen. | Status + **12:00 het bericht** |
| — | do 3 sep | *afsluitrun: cijfers, daarna alles weg* | | |

🎞️ = gebruikt het gifje. Zie §5.

**Dag 7 gaat eruit vóór 18.00 uur**, niet erna.

---

## 2. Eén ding dat ik heb aangepast

Jouw LinkedIn-post 7 begint met *"Morgenavond één vraag"*. Met deze kalender zou
die op woensdag 2 september landen — de avond zélf. Dan klopt "morgenavond" niet.

**Daarom staan post 6 en 7 in omgekeerde volgorde ingepland:**

| | Ingepland op | Jouw post |
|---|---|---|
| Dag 6 · di 1 sep | *Morgenavond één vraag* | post **7** |
| Dag 7 · wo 2 sep | *Samen bouwen* | post **6** |

Geen woord veranderd, alleen de volgorde. Post 6 eindigt met *"Woensdag
18:00–21:00, Moving-In Almelo"* en dat leest op woensdag zelf prima.

Wil je het terug zoals je het aanleverde: verwissel de teksten van
`content/linkedin/dag-06.md` en `dag-07.md`.

---

## 3. Wat er in deze release zit

```
STRATEGIE.md        de opzet: kanalen, remmen, niveaus
LINKEDIN.md         LinkedIn-campagne, media, meting
WHATSAPP.md         WhatsApp als opkomstkanaal + kant-en-klare berichten
RUNBOOK.md          wat de dagelijkse run doet, inclusief de vooruitblik
RELEASE.md          dit bestand

state.json          teller, einddatum, kanalen, links
content/dag-01…07   Instagram · Facebook · WhatsApp
content/linkedin/   LinkedIn, 7 posts
content/BEELD.md    formaten en hoe je opnieuw rendert

beeld/              15 bestanden
  dag-0N-4x5.png      1080×1350 — feed, LinkedIn, Facebook
  dag-0N-9x16.png     1080×1920 — Stories en WhatsApp Status
  woensdag-16x9.png   1280×720  — statische versie van het gifje
  bron/               de renderscripts
```

**Alle teksten zijn compleet.** Geen placeholders meer, op parkeerinfo in één
WhatsApp-bericht na.

---

## 4. Wat automatisch gaat en wat niet

| Kanaal | Automatisch | Waarom niet |
|---|---|---|
| **LinkedIn** | Ja | — |
| **Facebook** | Ja | — |
| **Instagram** | Ja *(niveau 3)* | op niveau 2 zet de run een concept klaar |
| **WhatsApp Status** | **Nee** | geen API |
| **WhatsApp Kanaal** | **Nee** | geen API |
| **Instagram Stories** | **Nee** | geen API |

WhatsApp kost je **twee minuten per dag, op woensdag vijf.** Dat is niet op te
lossen — er bestaat geen koppeling voor. Het staat in de planning zodat het je
niet overvalt.

### De vooruitblik
Elke dagelijkse run kijkt naar **morgen** en meldt wat er dan met de hand moet:

```
Morgen — dag 6, dinsdag 1 september

Automatisch:   LinkedIn 08:00, Facebook 19:00
Met de hand:   Instagram (concept staat klaar)
               WhatsApp Status — beeld/dag-06-9x16.png
               WhatsApp herinnering 17:00 — tekst in WHATSAPP.md
Let op:        niets
```

Ook als alles vanzelf gaat krijg je dat bericht. "Morgen gaat alles vanzelf" is
ook informatie.

---

## 5. Het gifje

Dag 1 en 3 gebruiken jouw gifje. Twee dingen:

**Ik heb het bestand zelf niet.** Het kwam binnen als stilstaand beeld. Zet de
echte `.gif` in `beeld/` voordat dag 1 draait.

**Het kan zijn dat het niet doorkomt.** De Zapier-koppeling van LinkedIn werkt met
een afbeelding-URL. Of een GIF daar doorheen komt — en of hij blijft bewegen —
is niet te voorspellen zonder te testen. **De aansluitcontrole test dit expliciet**
(zie `RUNBOOK.md`).

Komt hij niet door, dan valt `beeld/woensdag-16x9.png` in: hetzelfde ontwerp,
statisch. Je verliest de beweging, niet de post.

---

## 6. Aanzetten — in deze volgorde

| | Wat | Wie |
|---|---|---|
| 1 | Zapier koppelen: **LinkedIn, Instagram, Facebook Pages** | Jij |
| 2 | Instagram op Business of Creator, gekoppeld aan een Facebook-pagina | Jij |
| 3 | Het echte gifje in `beeld/` zetten | Jij |
| 4 | WhatsApp: zakelijk nummer, Business-app, kanaal, `wa.me`-link in je bio | Jij |
| 5 | **Aansluitcontrole draaien** — testpost per kanaal, GIF meetesten | Ik |
| 6 | Beeld op een publieke URL zetten | Ik |
| 7 | Routines aanzetten, harde stop 2 september | Ik |

Stap 1 tot 4 kan ik niet voor je doen — daar hoort een login bij.

**Nog niets gekoppeld.** Zolang dat zo is staat alles stil en gaat er niets de
deur uit.

---

## 7. Meten

Alle links zijn meetbaar en aimelo.nl herkent de parameters:

| | Link |
|---|---|
| LinkedIn | `aimelo.nl/aanmelden/2?van=li` |
| Instagram | `aimelo.nl/aanmelden/2?van=ig` |
| Facebook | `aimelo.nl/aanmelden/2?van=fb` |
| WhatsApp | `aimelo.nl/aanmelden/2?van=wa` |

De afsluitrun van donderdag 3 september zet ze naast elkaar, samen met de enige
vraag die telt: **hoeveel mensen zaten er woensdagavond?**

---

## 8. Twee dingen die je nog moet weten

**De posters zijn een reconstructie.** Ik had je Canva-bronbestanden niet. Ze zijn
nagebouwd in jullie stijl met **Anton** als kopletter — de dichtstbijzijnde vrij
beschikbare tegenhanger. Leg ze naast je originelen voordat dag 1 draait. Wijkt de
letter te veel af, dan is de schone route: dezelfde teksten in Canva en daar
exporteren op 1080×1350.

**LinkedIn en de posters zeggen iets anders.** Je LinkedIn-reeks vraagt *waarom ben
jij ondernemer geworden* en belooft ruimte en tijd terug. De posters zeggen *je
werk wordt niet gezien* en beloven zichtbaarheid. Twee campagnes over dezelfde
avond. De doelgroepen overlappen nauwelijks, dus het kán — maar het is nu een
keuze, geen ongeluk. Wil je dat de posters de LinkedIn-boodschap volgen, zeg het
en ik schrijf ze om in dezelfde stijl.

---

## 9. Stoppen

Twee remmen, los van elkaar:

- **Teller** — run 7 verwijdert de Routines
- **Datum** — na 2 september publiceert geen enkele run nog iets, wat de teller ook zegt

Eerder stoppen: zet `harde_stopdatum` in `state.json` op gisteren. Dat vangt alles
af, ook als er ergens nog een Routine blijft staan.
