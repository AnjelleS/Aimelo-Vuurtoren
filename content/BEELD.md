# Beeld — wat er moet gebeuren vóór dag 1

## Het probleem

Je vijf posters zijn **1080×1920 (9:16)**. Dat is Stories-formaat.

Instagram accepteert via de API alleen feed-beelden tussen **4:5 en 1.91:1**.
9:16 valt daarbuiten. Instagram croppt hem dan automatisch naar 4:5:

```
1080 × 1920  (jouw poster, 9:16)
  ├─ 285 px  ← WEG, boven      (bovenkant koptekst)
  ├─ 1350 px    blijft over
  └─ 285 px  ← WEG, onder      (het AiMELO-logo zit hier vlakbij)
```

Een automatische crop haalt dus 570 px uit een ontwerp waarin de tekst juist
de volle hoogte gebruikt. Kop bovenaan afgesneden, logo onderaan in gevaar.

## De oplossing

**Exporteer elke poster ook als 1080×1350 (4:5).** Geen crop — een herexport,
waarbij je de tekstblokken opnieuw in de kortere hoogte zet. Dat is tien
minuten werk in Canva en het scheelt je vijf verminkte posts.

## Waar welk formaat heen gaat

| Formaat | Kanaal | Automatisch? |
|---|---|---|
| 1080×1350 (4:5) | Instagram feed | Ja |
| 1080×1350 (4:5) | LinkedIn | Ja — LinkedIn kapt 9:16 ook af |
| 1080×1920 (9:16) | Instagram Stories | Nee, kan niet via de API |

**Gratis extra:** je 9:16-versies zijn niet verspild. Zet ze elke dag met de
hand in je Stories, náást de automatische feed-post. Dertig seconden werk, en
Stories is precies waar lokale ondernemers in Almelo wél kijken.

## Publieke URL

Elk beeld moet op een directe, publieke URL staan voordat het gepubliceerd kan
worden. De map `beeld/` in deze repo werkt daarvoor: bestanden zijn daarna
bereikbaar via `raw.githubusercontent.com`. Een Drive- of Dropbox-deellink
werkt niet — dat zijn viewer-pagina's, geen bestanden.

## Nog te maken

Dag 6 en 7 hebben nog geen beeld. Zelfde stijl, andere boodschap:
- **Dag 6 — "MORGEN"** — de herinnering
- **Dag 7 — "VANAVOND"** — de dag zelf, met tijd en adres in beeld

Die twee zijn niet optioneel: de vijf posters die je hebt zijn allemaal haken,
geen van alle zegt wanneer of waar. Zonder die twee eindigt de week zonder
uitnodiging.
