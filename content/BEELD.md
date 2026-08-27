# Beeld — opgelost

## Wat er is gerenderd

**14 bestanden in `beeld/`** — zeven posters, elk in twee formaten, met
**18.00 – 21.00 uur** in beeld.

| Formaat | Waar het heen gaat | Automatisch? |
|---|---|---|
| `dag-0N-4x5.png` — 1080×1350 | Instagram feed, LinkedIn, Facebook | Ja |
| `dag-0N-9x16.png` — 1080×1920 | Instagram Stories, **WhatsApp Status** | Nee — geen API |

Dag 6 (*Morgenavond. Nog plek.*) en dag 7 (*Vanavond. Loop gewoon binnen.*) zijn
nieuw ontworpen in dezelfde stijl.

## Waarom 4:5 en niet 9:16

Instagram accepteert via de API alleen feed-beelden tussen 4:5 en 1.91:1. De
oorspronkelijke 9:16-posters vielen daarbuiten en zouden automatisch gecropt zijn:
285 px van boven en 285 px van onder weg, dwars door de koptekst en vlak langs het
logo. De 4:5-versies zijn opnieuw opgebouwd in die kortere hoogte, niet gecropt.

De 9:16-versies zijn níet verspild: die gaan naar Stories en WhatsApp Status —
precies waar dat formaat wél thuishoort.

## Belangrijk: dit is een reconstructie

Ik had je Canva-bronbestanden niet. Deze posters zijn nagebouwd in jullie stijl:
cream ondergrond, off-white paneel, donkerblauw `#16293A`, limegroen `#86C63F`,
en **Anton** als kopletter — de dichtstbijzijnde vrij beschikbare tegenhanger van
de zware smalle letter op je originelen.

Vergelijk ze naast je eigen bestanden. Wijkt de letter te veel af, dan is de
schone route: dezelfde teksten en de tijd in Canva zetten en daar exporteren op
1080×1350.

## Tekst of tijd wijzigen

Alles staat in `beeld/bron/posters.py`. Pas de tekst aan en draai opnieuw:

```
python3 beeld/bron/posters.py
```

Beide formaten worden dan opnieuw weggeschreven.

## Nog te doen

Elk beeld moet op een directe, publieke URL staan voordat het gepubliceerd kan
worden. De map `beeld/` in deze repo werkt daarvoor — bestanden zijn bereikbaar
via `raw.githubusercontent.com`. Een Drive- of Dropbox-deellink werkt niet: dat
zijn viewer-pagina's, geen bestanden.
