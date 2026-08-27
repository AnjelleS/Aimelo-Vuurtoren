# Runbook — wat er elke dag gebeurt

Elke dagelijkse run start een **verse sessie zonder geheugen**. Alles wat die
sessie moet weten staat in dit bestand en in `state.json`.

**Kalender:** donderdag 27 augustus t/m woensdag 2 september 2026.
Dag 7 is de avond zelf, 18.00–21.00 bij Moving-In Almelo.

---

## Eenmalig — de aansluitcontrole

Draait vóór dag 1, zodra de Zapier-koppelingen er zijn. Dit bepaalt wat er de
hele week automatisch kan.

Per kanaal testen met een **concept of testpost**, niet met dag 1:

| Test | Waarom |
|---|---|
| LinkedIn: tekst + afbeelding-URL | de basis |
| LinkedIn: **GIF-URL in het afbeeldingveld** | dag 1, 3 gebruiken het gifje — komt die door, en blijft hij bewegen? |
| LinkedIn: eerste reactie plaatsen | wil je de link uit de post halen |
| Instagram: 4:5 beeld + caption | de basis |
| Facebook: tekst + link + beeld | de basis |

Schrijf de uitkomst in `state.json` onder `kanalen.<kanaal>.getest`:
`"ja"`, `"nee — reden"`, of `"alleen statisch"`.

**Komt het gifje niet door of verliest het zijn beweging**, zet dan
`beeld/woensdag-16x9.png` in de plaats — zelfde ontwerp, statisch. Meld het,
zet het niet stil om.

---

## Elke dag

### 1. Remmen controleren — vóór alles
```
lees state.json

REM B:  is vandaag > harde_stopdatum (2026-09-02)?
        → STOP. Publiceer niets. Log "gestopt: voorbij einddatum".

REM A:  is dag >= laatste_dag (7)?
        → dit is de laatste run. Publiceer nog wel, ruim daarna op (stap 6).

status != "actief"?
        → STOP. Gepauzeerd of nog niet gestart.
```
De datumcontrole draait vóór de teller, zodat een kapotte teller nooit tot een
publicatie na 2 september leidt.

### 2. De posts van vandaag ophalen
```
N = state.dag + 1

content/dag-0N.md          → Instagram, Facebook, WhatsApp
content/linkedin/dag-0N.md → LinkedIn

bestaat niet?          → STOP, meld het, hoog de teller NIET op
status != "gepland"?   → al gedaan of bewust overgeslagen. STOP.
```

### 3. Controleren of het te publiceren is
| Kanaal | Eis | Zo niet |
|---|---|---|
| LinkedIn | tekst niet leeg, beeld bereikbaar | overslaan, melden |
| Instagram | beeld is een publieke directe URL en geeft 200 | overslaan, melden — **niet** tekst-only proberen, dat weigert de API |
| Facebook | tekst niet leeg | overslaan, melden |

Haal de headers van elke beeld-URL echt op. Een dode link ontdekken op het
moment van posten is te laat.

### 4. Publiceren volgens `niveau`
```
niveau 1 → niets publiceren. Alles klaarzetten + seintje sturen.
niveau 2 → LinkedIn en Facebook publiceren. Instagram als concept + seintje.
niveau 3 → alle drie publiceren.
```
Publiceer per kanaal apart. **Mislukt het ene, ga door met het andere.**

WhatsApp doet de run nooit zelf — Status en Kanalen hebben geen API. Zet de
tekst en het 9:16-beeld klaar en stuur een seintje.

### 5. Vastleggen
```
logboek/dag-0N.json: { dag, datum, per kanaal: gelukt/mislukt, tijd, URL, fout }
content/dag-0N.md + content/linkedin/dag-0N.md → status: gepubliceerd
state.json → dag: N
commit + push
```
De teller gaat pas omhoog ná een geslaagde publicatie. Valt de run halverwege om,
dan pakt de volgende run dezelfde dag opnieuw op.

### 6. **Vooruitblik — kijk naar morgen**
Dit is de stap die voorkomt dat je 's ochtends voor verrassingen staat.

```
M = N + 1
open content/dag-0M.md en content/linkedin/dag-0M.md

controleer voor elk kanaal:
  - staat er een beeld, en is die URL bereikbaar?
  - staat er nog een placeholder in de tekst?
  - is dit kanaal getest en werkend? (state.kanalen.<kanaal>.getest)
  - is er iets bij dat de API niet kan — video, GIF, Stories?
```

**Meld morgen altijd**, ook als alles goed staat. Eén bericht, aan het eind van
de dagelijkse run:

```
Morgen — dag M, <dagnaam> <datum>

Automatisch:   LinkedIn 08:00, Facebook 19:00
Met de hand:   Instagram (concept staat klaar)
               WhatsApp Status — beeld/dag-0M-9x16.png
               WhatsApp Kanaal — tekst staat in dag-0M.md

Let op: <alles wat niet klopt, of "niets">
```

Is er niets handmatigs en klopt alles, zeg dat dan ook expliciet. "Morgen gaat
alles vanzelf" is ook informatie.

### 7. Alleen op dag 7 — opruimen
```
verwijder elke trigger-id in state.routines   (delete_trigger)
state.status = "afgerond"
zet een eenmalige afsluitrun voor donderdag 3 september
commit + push
meld: campagne afgerond, X van 7 geplaatst, automatisering uit
```
Let op: dag 7 is de **avond zelf**. De posts moeten eruit vóór 18.00 uur.

### 8. Donderdag 3 september — afsluiten en weg
Cijfers per kanaal naast elkaar, per `?van=`-parameter: li, ig, fb, wa. En de
enige vraag die telt: **hoeveel mensen zaten er woensdagavond?**
Schrijf `logboek/samenvatting.md`, verwijder daarna de eigen trigger.

---

## Wanneer stoppen en het melden

Publiceer níet, meld het en wacht:
- de tekst bevat nog een placeholder
- een beeld-URL geeft geen 200
- de Zapier-koppeling geeft een auth-fout
- `state.json` is niet te lezen of spreekt zichzelf tegen

Een dag overslaan en het melden is altijd beter dan iets halfs plaatsen.

---

## Handmatig ingrijpen

| Wat | Hoe |
|---|---|
| Morgen overslaan | `status: overgeslagen` in dat dagbestand |
| Alles pauzeren | `state.status` op `"gepauzeerd"` |
| Nu volledig stoppen | `harde_stopdatum` op gisteren zetten |
| Opschalen naar volautomatisch | `niveau` op `3` |
| LinkedIn dag 6 en 7 terugdraaien | verwissel de teksten van `content/linkedin/dag-06.md` en `dag-07.md` |
