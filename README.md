# Website Liesbeth Postma – drie voorstellen

Open `index.html` in de hoofdmap voor een keuzepagina, of direct:

| Versie | Sfeer | Bijzonderheden |
|---|---|---|
| `versie-1/` Bloesem | Licht en luchtig, blush → lavendel | Boogportret in de hero, magnolia groeit naast de vijf pijlers terwijl je scrolt, bloesemblaadjes dwarrelen aan het eind |
| `versie-2/` Verloop | Editorial en warm, diepe mauve hero | Cirkelportret (knipoog naar de inspiratiesite), bewegende strook met kernwoorden, thema's met meebewegende foto, tellers |
| `versie-3/` Water | Fotografisch, lichtblauw en salie met oudroze | Volledig beeld als opening, verhalende scrollsectie waarin de boom groeit terwijl de pijlers één voor één verschijnen |

Elke versie bevat alle pagina's uit het websitepakket:
home, de vier hulpvragen, werkwijze (+ vijf pijlerpagina's), over mij, praktische informatie, contact (met formulier), blog (+ eerste artikel), familieopstellingen, workshops, privacy en algemene voorwaarden.

## Lokaal bekijken

```bash
python -m http.server 8765
```

Daarna naar http://localhost:8765/ gaan.

## Aanpassen

De sites worden gegenereerd uit `bouw/`:

- `bouw/content.py` – alle teksten, menu, tarieven, contactgegevens, SEO-titels
- `bouw/common.py` – menu, footer, subpagina-opmaak, basis-CSS en JS
- `bouw/boom.py` – de groeiende magnolia (SVG + animatie)
- `bouw/v1.py`, `v2.py`, `v3.py` – huisstijl en homepage per versie

Na een wijziging: `python bouw/build.py`.

## Nog in te vullen vóór publicatie

- Persoonlijke video op de homepage: speelt via Google Drive (bestand-ID in `bouw/content.py`, `VIDEO_ID`). Werkt pas als het Drive-bestand op 'Iedereen met de link' staat; het bestand is 526 MB en past daarom niet in de repo. Alternatief: upload naar YouTube (verborgen) of Vimeo en pas de speler-URL aan in `bouw/v2.py`.
- Oude blogs van de vorige website (de nieuwe blog staat al bovenaan)
- Definitief e-mailadres en contactformulier-afhandeling (nu `mailto:`)
- Privacyverklaring en algemene voorwaarden (nu kaderpagina's)
- Controle van tarieven, adres en btw-vermelding (zoals het tekstpakket vraagt)
