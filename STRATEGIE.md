# Publicatiestrategie — AiMelo
**Zeven dagen naar de woensdagavond toe. Daarna stopt het.**

---

## 1. Wat deze campagne is

Je hebt vijf posters die allemaal hetzelfde zeggen, in vijf verschillende
vakken: *het werk is goed, het wordt alleen niet gezien.* Een hovenier, een
bakker, een meubelmaker, een schilder — en één brede opener over
marketingbudget.

En je hebt een evenement dat elke woensdag terugkomt: de gratis AI-avond in
Almelo.

Dat tweede gegeven bepaalt de hele opzet. Dit is geen losse contentweek — het
is **een aanloop naar één woensdagavond.** Zeven dagen die ergens naartoe
lopen, in plaats van zeven dagen die toevallig achter elkaar vallen.

> **Alles loopt naar woensdag 2 september toe.**
> Zeven dagen, van donderdag 27 augustus tot en met de avond zelf. Elk kanaal
> zeven posts. Zie [`RELEASE.md`](RELEASE.md) voor de volledige kalender.

Loopt hij goed, dan draai je hem opnieuw voor de woensdag erna. Deze week is de
proef, niet het eindpunt.

---

## 2. Het uitgangspunt van de machine

De valkuil bij "een week lang automatisch posten" is dat mensen zeven posts in
één keer in een scheduler zetten en weglopen. Dan ligt je content een week van
tevoren vast: je kunt niet meer reageren op wat er die week gebeurt, en de
laatste post gaat de deur uit terwijl je hem eigenlijk had willen aanpassen.

> **De wachtrij is levend, de aanjager is dom.**

Elke dag start een verse run die pakt wat er op dát moment in `content/` staat.
Meldt zich dinsdag een hovenier aan die precies het verhaal van dag 3 vertelt,
dan zet je dat woensdagochtend nog in de post van die avond.

```
   WACHTRIJ                AANJAGER                    REM
   content/dag-0N.md  →   1× per dag, vaste tijd  →   dag 7 = de avond
   ─────────────────      ──────────────────────      ─────────────
   tekst LinkedIn         leest state.json            (a) teller op 7
   caption Instagram      pakt de post van vandaag    (b) einddatum 9 sep
   beeld-URL              publiceert                  beide onafhankelijk
   status                 logt + zet teller door      één faalt → ander vangt
```

### Twee remmen, los van elkaar
Hier gaat het bij dit soort automatiseringen meestal mis: de stop wordt vergeten
en er staat in week drie nog steeds iets te posten.

| | Rem | Vangt af |
|---|---|---|
| **a** | Teller: run 7 verwijdert de Routine | De normale weg |
| **b** | Harde einddatum in de opdracht zelf: na 2 september publiceert geen enkele run nog iets, wat de teller ook zegt | Teller corrupt, Routine twee keer afgegaan, run 7 mislukt |

De datumcontrole draait vóór de teller. Zo leidt een verkeerd opgehoogde teller
nooit tot een achtste post.

---

## 3. Het beeld — klaar

Veertien bestanden staan in `beeld/`: zeven posters, elk op **1080×1350 (4:5)**
voor de feed en **1080×1920 (9:16)** voor Stories en WhatsApp Status. **18.00 –
21.00 uur** staat in beeld.

Je oorspronkelijke posters waren 9:16. Instagram accepteert via de API alleen
feed-beelden tussen 4:5 en 1.91:1, dus die zouden automatisch gecropt zijn — 285
px van boven en 285 px van onder weg, dwars door de kop en vlak langs het logo.
De 4:5-versies zijn opnieuw opgebouwd in die kortere hoogte, niet gecropt.

Dag 6 (*Morgenavond. Nog plek.*) en dag 7 (*Vanavond. Loop gewoon binnen.*) zijn
er nieuw bij ontworpen.

> **Let op:** dit is een reconstructie in jullie stijl, geen export van je
> Canva-originelen — die had ik niet. De kopletter is Anton, de dichtstbijzijnde
> vrij beschikbare tegenhanger. Leg ze naast je eigen bestanden voordat je ze
> gebruikt. Zie `content/BEELD.md`.

---

## 4. De kanalen — en een eerlijke kanttekening

Er is nog **geen enkele Zapier-koppeling actief.** Niet voor LinkedIn, niet voor
Instagram. Dat is stap 0.

### Instagram
Alleen **Instagram for Business** kan via de API. Vereist een Business- of
Creator-account, gekoppeld aan een **Facebook-pagina**. Beeld is verplicht —
een tekst-only post weigert de API — en dat beeld moet op een publieke, directe
URL staan. Een Drive- of Dropbox-deellink werkt niet: dat zijn viewer-pagina's,
geen bestanden.

### LinkedIn
Werkt met tekst en beeld, persoonlijk profiel of bedrijfspagina. Simpelste
koppeling van de drie.

### Facebook — de derde die je er gratis bij krijgt
Dit is de kanttekening die je moet horen. **Voor jouw doelgroep is LinkedIn het
zwakste van de drie kanalen.** Hoveniers, bakkers en meubelmakers in Almelo
zitten niet op LinkedIn. Ze zitten op Facebook, in lokale groepen, en op
Instagram.

LinkedIn heeft wel nut — voor je geloofwaardigheid, voor doorverwijzers, voor
andere ondernemers die iemand kennen. Maar het is niet waar je aanmeldingen
vandaan komen.

En Facebook kost je niets extra: **die pagina moet je toch al aanmaken voor
Instagram.** Zapier kan er direct op posten. Dezelfde post, drie kanalen, één
koppeling meer.

> **Advies: doe alle drie.** Instagram en Facebook voor de aanmeldingen,
> LinkedIn voor het gezag.

### LinkedIn draait een eigen campagne
LinkedIn heeft een eigen boodschap gekregen — *waarom ben jij eigenlijk ondernemer
geworden?* — met zeven eigen posts, een eigen kalender en een meetbare link. Dat
is een ándere belofte dan de posters doen. Bewuste keuze of nog uit te lijnen:
[`LINKEDIN.md`](LINKEDIN.md) §2.

### En dan WhatsApp — een ander soort kanaal
WhatsApp hoort niet in dit rijtje, want het doet iets anders. Social media trekt
aandacht; **WhatsApp zorgt dat mensen ook werkelijk komen opdagen.** Dat is het
echte risico van een gratis avond: gratis kost niets, dus het kost ook niets om
niet te komen.

Status en Kanalen hebben géén API, dus WhatsApp valt buiten de machine — twee
minuten handwerk per dag, op woensdag vijf. De volledige opzet, inclusief de
kant-en-klare berichten, staat in [`WHATSAPP.md`](WHATSAPP.md).

---

## 5. Kies je niveau

| | Niveau | Wat er gebeurt | Nodig | Risico |
|---|---|---|---|---|
| **1** | Herinnering | De run zet de post klaar en stuurt een seintje. Jij plakt. | Niets | Geen |
| **2** | Half — **aanbevolen start** | LinkedIn en Facebook automatisch, Instagram als concept. | LinkedIn + FB koppeling | Laag |
| **3** | Vol | Alle drie live zonder tussenkomst. | IG Business + FB-pagina + beeld op publieke URL | Er gaat iets live dat je niet hebt gelezen |

Begin op niveau 2 en schaal woensdag op als het bevalt. De wachtrij verandert
er niet van.

---

## 6. De aanloop — zeven dagen

| Dag | Datum | Poster | Wie je aanspreekt |
|---|---|---|---|
| 1 | do 27 aug | *Geen marketingbudget?* | iedereen — de brede haak |
| 2 | vr 28 aug | *Je mooiste werk hangt bij je klant* | schilders, stukadoors, interieurbouw |
| 3 | za 29 aug | *Je tuinen zijn prachtig* | hoveniers, groenbedrijven |
| 4 | zo 30 aug | *Je brood verkoopt zichzelf* | bakkers, slagers, speciaalzaken |
| 5 | ma 31 aug | *Je kasten zijn maatwerk* | meubelmakers, timmerlieden |
| 6 | di 1 sep | *Morgenavond. Nog plek.* | de herinnering |
| 7 | wo 2 sep | *Vanavond. Loop gewoon binnen.* | de avond zelf |

Vijf haken, dan twee uitnodigingen. Dat laatste stuk is niet optioneel: **geen
van je vijf posters zegt wanneer of waar.** Ze prikken alleen. Zonder dag 6 en 7
eindigt de week met vijf mensen die knikken en niemand die komt.

De weekenddagen zijn met opzet gevuld met hovenier en bakker: die scrollen
zaterdag- en zondagavond, niet dinsdagochtend. LinkedIn presteert die twee
dagen minder — daar is Instagram en Facebook je kanaal.

### Tijdstippen
| Platform | Slot | Waarom |
|---|---|---|
| LinkedIn | 08:00–10:00 | vóór of aan het begin van de werkdag |
| Instagram / Facebook | 19:00–21:00 | vakmensen kijken 's avonds, niet tijdens werk |

Die vallen ver uit elkaar, dus het worden **twee Routines**: één om 08:00 voor
LinkedIn, één om 19:00 voor Instagram en Facebook. Op dag 7 gaat die
avondpost eruit vóór de deur opengaat, niet erna.

---

## 7. Twee vormen, één boodschap

**LinkedIn** — tekst draagt. De eerste twee regels bepalen alles: mobiel kapt af
rond 140 tekens met "…meer". Witregels tussen alinea's. Geen externe link in de
post zelf, die drukt je bereik — link in de eerste reactie. Drie tot vijf
hashtags.

**Instagram** — beeld draagt, caption ondersteunt. Eerste regel wordt afgekapt
rond 125 tekens. Vijf tot tien hashtags, mix van groot (#twente) en niche
(#hovenier). Links werken niet in de caption: verwijs naar de bio.

**Facebook** — tussenvorm. Iets langer dan Instagram, en links wérken hier wel.
Zet de aanmeldlink gewoon in de post. Dit is ook het kanaal waar delen in lokale
groepen het echte werk doet.

---

## 8. Afsluiten — en aantoonbaar uit

Elke run legt vast: platform, tijdstip, post-URL, gelukt of niet.

Op **donderdag 10 september** draait er nog één keer iets, eenmalig. Die run zet
de cijfers van de zeven dagen naast elkaar — welke poster, welk vak, welk
kanaal, welk tijdstip — en legt daarnaast de enige vraag die telt: **hoeveel
mensen zaten er woensdagavond?** Dat is wat je meeneemt naar de volgende
woensdag. Daarna verwijdert die run ook zichzelf.

Wil je er eerder tussenuit: zet `harde_stopdatum` op gisteren. Rem B vangt dan
alles af, ook als er ergens nog een Routine blijft staan.

---

## 9. Wat er nog moet gebeuren

| | Wat | Wie |
|---|---|---|
| 1 | ~~Locatie en aanmeldlink~~ — klaar: Moving-In Almelo, `aimelo.nl/aanmelden/2` | ✓ |
| 1b | **Video en stills voor LinkedIn** dag 1, 3, 4, 5 | Jij |
| 2 | ~~Herexport naar 1080×1350~~ — klaar, 14 bestanden in `beeld/` | ✓ |
| 3 | ~~Beeld dag 6 en 7~~ — klaar | ✓ |
| 3b | WhatsApp: zakelijk nummer, Business-app, kanaal, wa.me-link | Jij |
| 4 | Instagram op Business/Creator + Facebook-pagina koppelen | Jij |
| 5 | Zapier koppelen: LinkedIn, Instagram, Facebook Pages | Jij |
| 6 | Beeld op een publieke URL zetten | Ik |
| 7 | Routines aanzetten met einddatum 2 september | Ik |

Punt 1 is de belangrijkste. De tijd staat er nu in, maar zonder locatie en een
knop om op te drukken leveren zeven prachtige posters nog steeds nul
aanmeldingen op.
