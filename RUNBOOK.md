# Runbook — wat er elke dag gebeurt

Elke dagelijkse Routine start een **verse sessie zonder geheugen**. Alles wat
die sessie moet weten staat in dit bestand en in `state.json`. Niets zit in
iemands hoofd of in een oude conversatie.

---

## Stappen

### 1. Remmen controleren — vóór alles
```
lees state.json

REM B:  is vandaag > harde_stopdatum?
        → STOP. Publiceer niets. Log "gestopt: voorbij einddatum". Klaar.

REM A:  is dag >= laatste_dag?
        → dit is de laatste run. Publiceer nog wel, ruim daarna op (stap 6).

is status != "actief"?
        → STOP. De campagne is gepauzeerd of nog niet gestart.
```
Deze volgorde is met opzet: de datumcontrole staat vóór de teller, zodat een
kapotte of dubbel opgehoogde teller nooit tot een publicatie na de einddatum leidt.

### 2. De post van vandaag ophalen
```
N = state.dag + 1
open content/dag-0N.md

bestaat niet?          → STOP, meld het, hoog de teller NIET op
status != "gepland"?   → al gedaan of bewust overgeslagen. STOP.
```

### 3. Controleren of hij te publiceren is
| Platform | Eis | Zo niet |
|---|---|---|
| LinkedIn | tekst niet leeg | overslaan, melden |
| Instagram | `beeld:` is een publieke directe URL, en hij is bereikbaar | overslaan, melden — **niet** tekst-only proberen, dat weigert de API |

Controleer de beeld-URL echt (haal de headers op). Een dode link ontdekken op
het moment van posten is te laat.

### 4. Publiceren volgens `niveau`
```
niveau 1 → niets publiceren. Post klaarzetten + seintje sturen.
niveau 2 → LinkedIn publiceren. Instagram als concept klaarzetten + seintje.
niveau 3 → beide publiceren.
```
Publiceer per platform apart. **Mislukt het ene, ga door met het andere** — een
gefaalde Instagram-upload mag een geslaagde LinkedIn-post niet tegenhouden.

### 5. Vastleggen
```
schrijf logboek/dag-0N.json:
  { dag, datum, per platform: gelukt/mislukt, tijdstip, URL, foutmelding }

zet in content/dag-0N.md:   status: gepubliceerd
zet in state.json:          dag: N

commit + push
```
De teller gaat pas omhoog ná een geslaagde publicatie. Valt de run halverwege om,
dan pakt de volgende run dezelfde dag opnieuw op in plaats van er een over te slaan.

### 6. Alleen op dag 7 — opruimen
```
verwijder elke trigger-id in state.routines   (delete_trigger)
zet state.status = "afgerond"
zet een eenmalige afsluitrun voor morgen      (run_once_at, dag 8)
commit + push
meld: campagne afgerond, X van 7 geplaatst, automatisering uit
```

### 7. Dag 8 — afsluiten en weg
Haal de cijfers van de zeven posts op. Zet ze naast elkaar: welke invalshoek,
welk tijdstip, welk platform. Schrijf `logboek/samenvatting.md`.
Verwijder daarna ook je eigen trigger. **Daarna staat er niets meer aan.**

---

## Wanneer stoppen en het vragen

Publiceer níet, meld het en wacht:
- de tekst bevat nog een placeholder (`TEKST HIER`, `https://...`, `JJJJ-MM-DD`)
- de beeld-URL geeft geen 200 terug
- de Zapier-koppeling is weg of geeft een auth-fout
- `state.json` is niet te lezen of spreekt zichzelf tegen

Een dag overslaan en het melden is altijd beter dan iets halfs plaatsen. Er is
geen weg terug na publiceren.

---

## Handmatig ingrijpen

| Wat | Hoe |
|---|---|
| Morgen overslaan | `status: overgeslagen` in dat dagbestand |
| Alles pauzeren | `state.status` op `"gepauzeerd"` |
| Nu volledig stoppen | `harde_stopdatum` op gisteren zetten — rem B vangt alles af, ook als een Routine blijft staan |
| Opschalen naar volautomatisch | `niveau` op `3`, mits Instagram-vereisten allemaal `true` |
