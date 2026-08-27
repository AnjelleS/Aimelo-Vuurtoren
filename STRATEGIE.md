# Publicatiestrategie — LinkedIn & Instagram
**7 dagen, elke dag een post, daarna automatisch stop.**

---

## 1. Het uitgangspunt

Je hebt de content al. Wat ontbreekt is de machine die hem eruit duwt.

De valkuil bij "een week lang automatisch posten" is dat mensen zeven posts in
één keer in een scheduler zetten en weglopen. Dan ligt je content een week van
tevoren vast: je kunt niet meer reageren op wat er die week gebeurt, en de
laatste post gaat de deur uit terwijl je hem eigenlijk had willen aanpassen.

Deze strategie draait dat om:

> **De wachtrij is levend, de aanjager is dom.**

De *aanjager* (wat er elke dag gebeurt) is saai, vast en betrouwbaar.
De *wachtrij* (wát er die dag uitgaat) mag tot het laatste moment veranderen.
Pas je vanavond de post van morgen aan, dan is dát wat er morgen uitgaat.

---

## 2. De drie onderdelen

```
   WACHTRIJ                AANJAGER                    REM
   content/dag-0N.md  →   1× per dag, vaste tijd  →   dag 7 = einde
   ─────────────────      ──────────────────────      ─────────────
   tekst LinkedIn         leest state.json            (a) teller op 7
   caption Instagram      pakt post van vandaag       (b) einddatum
   beeld-URL              publiceert                  beide onafhankelijk
   status                 logt + zet teller door      één faalt → ander vangt
   ↑ tot publicatie       ↑ verandert nooit           ↑ stopt gegarandeerd
     aanpasbaar
```

### Wachtrij — `content/dag-01.md` t/m `dag-07.md`
Eén bestand per dag. Beide platforms in hetzelfde bestand, want ze horen bij
dezelfde boodschap maar hebben een andere vorm. Zolang `status: gepland` staat,
mag je erin schrijven.

### Aanjager — een dagelijkse Routine
Eén keer per dag, op een vast tijdstip, start een verse run. Die run:
1. leest `state.json` → welke dag zijn we?
2. opent `content/dag-0N.md`
3. publiceert naar de kanalen die aan staan
4. schrijft het resultaat in `logboek/`
5. zet de teller op N+1

Elke run staat op zichzelf. Er is geen wachtrij die "loopt" — er is elke dag
één beslissing, opnieuw genomen op basis van wat er op dat moment in de map staat.

### Rem — twee onafhankelijke stoppen
Hier gaat het bij dit soort automatiseringen meestal mis: de stop wordt vergeten
en er staat in week drie nog steeds iets te posten. Daarom twee remmen die
niet van elkaar afhangen:

| | Rem | Vangt af |
|---|---|---|
| **a** | Teller: run 7 verwijdert de Routine | De normale weg |
| **b** | Einddatum in de opdracht zelf: is het later dan de einddatum, dan publiceert de run niks — wat de teller ook zegt | Teller corrupt, Routine twee keer per dag afgegaan, run 7 mislukt |

Rem (a) alleen faalt als `state.json` beschadigd raakt. Rem (b) alleen faalt als
de Routine vaker draait dan bedoeld. Samen faalt het veilig.

---

## 3. Stap 0 — koppelingen (dit ontbreekt nu)

Ik heb je Zapier-account gecontroleerd: **er is nog geen enkele koppeling actief**,
niet voor LinkedIn en niet voor Instagram. Zonder deze stap kan er niets
gepubliceerd worden.

### LinkedIn
Beschikbaar via Zapier (`LinkedIn`, 3 schrijf-acties). Je kiest:
- **Persoonlijk profiel** — een gewone share vanaf jouw naam
- **Bedrijfspagina** — een company update

Tekst-only werkt prima. Beeld is optioneel.

### Instagram — let op, hier zitten de echte beperkingen
Alleen **Instagram for Business** is beschikbaar. Een persoonlijk account kan
niet via de API gepost worden. Punt. Vereisten:

1. Een Instagram **Business- of Creator-account** (gratis om te wisselen)
2. Gekoppeld aan een **Facebook-pagina** — dit is niet optioneel, de API loopt via Meta
3. **Beeld is verplicht.** Je kunt via de API geen tekst-only post plaatsen.
   Elke post heeft een afbeelding of video nodig.
4. Dat beeld moet op een **publieke, directe URL** staan. Een Google Drive- of
   Dropbox-deellink werkt níet — dat zijn viewer-pagina's, geen bestanden.
   Wel goed: een eigen server, S3, Cloudinary, of een GitHub-repo via `raw.githubusercontent.com`.
5. Stories zijn niet beschikbaar via de API. Feed-posts, carrousels en reels wel.

> **Dit is het belangrijkste verschil om te snappen:** LinkedIn is tekst-first,
> Instagram is beeld-verplicht. Dezelfde boodschap heeft dus per dag ook een
> plaatje nodig, anders valt Instagram automatisch af.

---

## 4. Kies je niveau

Niet alles hoeft in één keer volautomatisch. Drie niveaus, oplopend in
gemak en in risico:

| | Niveau | Wat er gebeurt | Nodig | Risico |
|---|---|---|---|---|
| **1** | Herinnering | De run zet de post van vandaag klaar en stuurt je een seintje. Jij plakt en plaatst. | Niets | Geen |
| **2** | Half — **aanbevolen start** | LinkedIn gaat automatisch de deur uit. Instagram wordt klaargezet als concept. | LinkedIn-koppeling | Laag |
| **3** | Vol | Beide gaan live zonder dat jij ernaar kijkt. | IG Business + FB-pagina + beeld-pijplijn | Er gaat iets live dat je niet hebt gelezen |

**Advies: begin op niveau 2.** LinkedIn is tekst — daar kan weinig misgaan en
de winst is direct. Instagram heeft de beeldketen nodig; zolang die niet
waterdicht is, is een concept dat jij met één tik plaatst sneller dan een
mislukte upload repareren.

Je kunt halverwege de week opschalen. De wachtrij verandert er niet van.

---

## 5. Ritme over zeven dagen

### Weekend is niet neutraal
LinkedIn zakt in het weekend hard in — zakelijk publiek kijkt niet. Instagram
niet, die loopt in het weekend vaak juist beter. Zeven dagen op rij betekent
dus twee dagen waarop LinkedIn structureel minder doet.

Twee opties:
- **Doorgaan op beide.** Simpel, maar dag 6 en 7 op LinkedIn presteren minder.
- **LinkedIn op werkdagen (5 posts), Instagram alle 7.** Iets meer regelwerk,
  betere cijfers. Dit is de betere keuze als de cijfers ertoe doen.

### Tijdstippen
| Platform | Beste slot | Waarom |
|---|---|---|
| LinkedIn | 08:00–10:00, di t/m do | Mensen scrollen voor of aan het begin van de werkdag |
| Instagram | 11:00–13:00 of 19:00–21:00 | Lunchpauze en de avond |

Die vallen niet samen. Daarom: **twee Routines in plaats van één.**
Eén om 08:00 voor LinkedIn, één om 12:00 voor Instagram. Kost niets extra en
je haalt beide slots. Beide stoppen op dag 7.

Wil je het simpel houden: één run om 07:00 die allebei doet. Je levert wat
bereik in op Instagram, maar er is één ding om in de gaten te houden.

---

## 6. Zeven dagen vullen vanuit één post

Je hebt de content — maar zeven dagen vraagt zeven stukken. Eén kernpost is
genoeg materiaal, mits je hem uit elkaar trekt in invalshoeken in plaats van
hem te herhalen:

| Dag | Invalshoek |
|---|---|
| 1 | **De stelling** — je kernpost, zoals hij is |
| 2 | **Het voorbeeld** — één concreet geval waarin het klopte |
| 3 | **De tegenwerping** — "ja maar…" en jouw antwoord daarop |
| 4 | **Het cijfer** — de data of het bedrag eronder |
| 5 | **De fout** — waar jij het zelf verkeerd deed |
| 6 | **De stappen** — hoe iemand het morgen zou doen |
| 7 | **De vraag** — teruggeven aan je netwerk, oogst de reacties |

Dag 7 als vraag is geen toeval: dat is de post die de meeste reacties trekt, en
hij sluit de week af met een gesprek in plaats van een zender.

### Vormverschil per platform
Dezelfde boodschap, twee vormen — niet knippen en plakken:

**LinkedIn**
- De eerste twee regels bepalen alles: mobiel wordt afgekapt rond 140 tekens met "…meer". Je haak moet dáárvoor staan.
- Witregels tussen alinea's. Een blok tekst wordt niet gelezen.
- Geen externe link in de post zelf — die drukt je bereik. Link in de eerste reactie.
- 3 tot 5 hashtags, onderaan.

**Instagram**
- Het beeld doet het werk, de caption ondersteunt.
- Eerste regel wordt afgekapt rond 125 tekens — zelfde principe, kortere ruimte.
- 5 tot 10 hashtags, mix van groot en niche.
- Links werken niet in de caption. Verwijs naar de bio.

---

## 7. Meten en afsluiten

Elke run schrijft naar `logboek/dag-0N.json`: platform, tijdstip, de URL van de
geplaatste post, en of het gelukt is.

**Dag 8 — de afsluitrun.** Eén keer, eenmalig, daarna weg. Die haalt de cijfers
van de zeven posts op en zet ze naast elkaar: welke invalshoek deed het, welk
tijdstip, welk platform. Dat is wat je meeneemt naar een volgende week — en
meteen het bewijs dat alles daadwerkelijk gestopt is.

Daarna staat er niets meer aan.

---

## 8. Wat er moet gebeuren om te starten

| | Stap | Wie |
|---|---|---|
| 1 | Zapier koppelen aan LinkedIn | Jij — eenmalig, 2 min |
| 2 | Kiezen: persoonlijk profiel of bedrijfspagina | Jij |
| 3 | *(voor Instagram)* Account op Business/Creator + Facebook-pagina koppelen | Jij — eenmalig |
| 4 | *(voor Instagram)* Plek voor beeld met publieke URL | Samen |
| 5 | Kernpost in `content/dag-01.md`, invalshoeken over dag 2–7 | Samen |
| 6 | Routine(s) aanzetten met einddatum | Ik |
| 7 | Dag 1 draaien en meekijken | Samen |

Stap 1 tot 3 kan ik niet voor je doen — daar hoort een login bij. De rest wel.
