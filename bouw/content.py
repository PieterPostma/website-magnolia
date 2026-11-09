# -*- coding: utf-8 -*-
"""Teksten website Liesbeth Postma – ingekorte versie (circa 30% minder woorden dan het pakket van 4 november 2026)."""

NAAM = "Liesbeth Postma"
TITEL = "Psychosociaal en lichaamsgericht therapeut"
MOTTO = "Leer te voelen – durf te vertrouwen"
STROOM = "Wat gevoeld mag worden, kan weer gaan stromen."
TEL = "06 15 14 83 69"
TEL_RAW = "+31615148369"
MAIL = "info@liesbethpostma.nl"
WEBSITE = "www.liesbethpostma.nl"
VIDEO_ID = "1Cnbb9ZB7BUMy4M89nqGrQoWjhz33OBih"  # Google Drive: Video_LiesbethpraktijkV2.mp4
ADRES = "Dijkstraat 20, Bemmel"
INSTAGRAM = "https://www.instagram.com/liesbeth.postma.therapeut/"
FACEBOOK = "https://www.facebook.com/lpostma1"
LINKEDIN = "https://www.linkedin.com/in/liesbeth-postma-83b19a18a"
KVK = "91541824"
BTW = "NL004902550B95"
AGB_PRAKTIJK = "90096017"
AGB_ZORG = "90120743"
REGISTER = "2023012"

MENU = [
    ("Home", "index.html"),
    ("Waarmee kan ik je helpen?", None, [
        ("Jongvolwassenen & faalangst", "jongvolwassenen.html"),
        ("Als je mentaal vastloopt", "mentaal-vastlopen.html"),
        ("Verlies & verandering", "verlies-en-verandering.html"),
        ("Jezelf verliezen in relaties", "relaties.html"),
        ("—", None),
        ("Familieopstellingen", "familieopstellingen.html"),
        ("Workshops", "workshops.html"),
    ]),
    ("Werkwijze", "werkwijze.html"),
    ("Over mij", "over-mij.html"),
    ("Praktische info", "praktische-informatie.html"),
    ("Blog", "blog.html"),
    ("Contact", "contact.html"),
]

THEMAS = [
    dict(slug="jongvolwassenen", kop="Jongvolwassenen & faalangst",
         kort="Bang om het niet goed genoeg te doen? Faalangst, prestatiedruk en de lat hoog leggen.", foto="natuur-bloemen.jpg"),
    dict(slug="mentaal-vastlopen", kop="Als je mentaal vastloopt",
         kort="Stress, angst, somberheid, burn-out of hooggevoeligheid. Aan de buitenkant gaat het goed, vanbinnen niet.", foto="water-zit.jpg"),
    dict(slug="verlies-en-verandering", kop="Verlies & verandering",
         kort="Rouw om wat er was, om wat je mist of om wat je dacht dat er zou zijn.", foto="natuur-zonsondergang.jpg"),
    dict(slug="relaties", kop="Jezelf verliezen in relaties",
         kort="Pleasegedrag, codependentie, narcistische dynamieken en steeds verder van jezelf af raken.", foto="boom-zit.jpg"),
]

PIJLERS = [
    dict(slug="psychosociale-therapie", kop="Psychosociale therapie",
         kort="Inzicht in je gedachten, gevoelens, ervaringen en terugkerende patronen.",
         tekst="We onderzoeken hoe gedachten, gevoelens, gedrag, ervaringen en relaties elkaar beïnvloeden. Er is ruimte voor je huidige hulpvraag én voor patronen en overtuigingen die in de loop van je leven zijn ontstaan. Inzicht helpt je herkennen wat je belemmert en welke verandering bij jou past.",
         praktijk="We beginnen bij jouw verhaal en verbinden inzichten met concrete keuzes in het dagelijks leven.",
         seo_titel="Wat is psychosociale therapie? | Liesbeth Postma",
         seo="Ontdek hoe psychosociale therapie helpt om inzicht te krijgen in gedachten, gevoelens, ervaringen en patronen die je dagelijks leven beïnvloeden."),
    dict(slug="lichaamsgericht-werken", kop="Lichaamsgericht werken",
         kort="Opnieuw leren luisteren naar de signalen van je lichaam, je gevoelens, behoeften en grenzen.",
         tekst="Soms begrijp je een situatie met je hoofd, maar voel je nog spanning, onrust of verdriet. Met aandacht voor ademhaling, lichaamssignalen, ontspanning, gronding en grenzen onderzoeken we wat je lichaam laat merken. Je bepaalt zelf wat je wilt ervaren of delen; we werken zorgvuldig en in jouw tempo.",
         praktijk="We oefenen met het opmerken van spanning en ontspanning en van je grenzen. Je hoeft nooit meer te doen dan wat op dat moment passend voelt.",
         seo_titel="Lichaamsgericht werken en leren voelen | Liesbeth Postma",
         seo="Leer signalen van je lichaam herkennen en weer contact maken met gevoelens, spanning, behoeften en grenzen tijdens lichaamsgerichte begeleiding."),
    dict(slug="innerlijk-kindwerk", kop="Innerlijk-kindwerk",
         kort="Aandacht voor oude pijn, onvervulde behoeften en beschermingspatronen uit je jeugd.",
         tekst="We verkennen hoe vroege ervaringen en onvervulde behoeften doorwerken in gevoelens, relaties en zelfbeeld. Via gesprek, visualisatie en ervaringsgerichte oefeningen geef je met mildheid aandacht aan jonge, kwetsbare delen in jezelf. Niet om pijn te forceren, maar om meer begrip, veiligheid en keuzevrijheid te ontwikkelen.",
         praktijk="We verkennen de behoeften achter oude reacties, zoals je aanpassen of bang zijn voor afwijzing. Je hoeft geen herinneringen op te roepen die je niet wilt onderzoeken.",
         seo_titel="Innerlijk-kindwerk en oude patronen | Liesbeth Postma",
         seo="Ontdek innerlijk-kindwerk: met aandacht voor vroege ervaringen, onvervulde behoeften en beschermingspatronen groeien in zelfbegrip en vertrouwen."),
    dict(slug="delenwerk", kop="Delenwerk",
         kort="Je innerlijke delen en hun beschermende functies leren herkennen en begrijpen.",
         tekst="Je kunt verschillende kanten in jezelf ervaren: een deel wil verandering, een ander deel beschermt je. Met delenwerk (zoals Voice Dialogue) leer je deze kanten herkennen en hun intenties begrijpen, zonder oordeel. Zo ontstaat ruimte om bewust te reageren in plaats van automatisch oude patronen te volgen.",
         praktijk="We geven woorden aan bijvoorbeeld een kritisch, kwetsbaar of beschermend deel, en onderzoeken hoe het je ooit hielp en wat je nu nodig hebt.",
         seo_titel="Delenwerk en innerlijke delen begrijpen | Liesbeth Postma",
         seo="Met delenwerk onderzoek je de verschillende kanten in jezelf, hun beschermende functies en hoe je meer begrip en keuzevrijheid ontwikkelt."),
    dict(slug="act", kop="ACT – Acceptance and Commitment Therapy",
         kort="Omgaan met moeilijke gedachten en gevoelens en kiezen vanuit wat voor jou belangrijk is.",
         tekst="ACT helpt je om te gaan met moeilijke gedachten en gevoelens zonder er voortdurend tegen te vechten. We onderzoeken wat belangrijk is in jouw leven en vertalen jouw waarden naar haalbare stappen. Vertrouwen betekent niet dat angst volledig weg hoeft te zijn.",
         praktijk="We oefenen met mild omgaan met gedachten en emoties en kijken naar kleine stappen die jouw leven betekenis geven, ook als onzekerheid blijft.",
         seo_titel="ACT therapie: ruimte voor gevoel en waarden | Liesbeth Postma",
         seo="ACT helpt je anders om te gaan met moeilijke gedachten en gevoelens en stappen te zetten die passen bij jouw persoonlijke waarden."),
]

HOME = dict(
    seo_titel="Psychosociaal en lichaamsgericht therapeut | Liesbeth Postma",
    seo="Leer te voelen. Durf te vertrouwen. Psychosociale en lichaamsgerichte begeleiding bij angst, stress, verlies en verandering. Ontdek mijn werkwijze.",
    doelgroep="Voor (jong)volwassenen die mentaal vastlopen of hun weg zoeken bij verlies en verandering.",
    herken=[
        "Je denkt veel na, legt de lat hoog en twijfelt aan jezelf. Misschien ben je bang om fouten te maken of probeer je steeds aan de verwachtingen van anderen te voldoen.",
        "Of je raakt steeds verder van jezelf verwijderd. Grenzen aangeven, gevoelens toelaten of ontdekken wat jij nodig hebt: het valt zwaar.",
        "Misschien speelt er stress, angst, somberheid, een burn-out of een ingrijpend verlies. Of loop je telkens tegen dezelfde patronen aan.",
        "Vaak hebben we al vroeg geleerd om gevoelens weg te stoppen, ons aan te passen of sterk te zijn. Wat ooit beschermde, kan later belemmeren.",
    ],
    herken_slot="Je hoeft niet precies te weten waarom je vastloopt om de eerste stap te zetten.",
    voorwie_intro="Ik begeleid (jong)volwassenen die psychisch of emotioneel vastlopen of hun weg zoeken bij verlies en verandering. Je kunt bij mij terecht met onder andere:",
    voorwie=[
        ("Angst en onzekerheid", "faalangst, perfectionisme, een negatief zelfbeeld."),
        ("Stress en overbelasting", "burn-out, spanning, piekeren, moeite met ontspannen."),
        ("Somberheid en verlies", "depressieve gevoelens, rouw, scheiding, grote veranderingen."),
        ("Jezelf verliezen in relaties", "pleasegedrag, moeite met grenzen, afhankelijkheid."),
        ("Trauma en oude patronen", "onverwerkte ervaringen en overlevingsmechanismen."),
        ("Persoonlijke ontwikkeling", "ontdekken wie je bent, wat je voelt en wat jij nodig hebt."),
    ],
    werkwijze=[
        "In mijn begeleiding staat opnieuw leren voelen en vertrouwen centraal.",
        "Ik combineer psychosociale en lichaamsgerichte therapie met methodieken die je helpen jezelf beter te begrijpen, oude patronen te herkennen en weer verbinding te maken met je gevoel. We kijken niet alleen naar wat je denkt, maar ook naar wat je voelt en ervaart in je lichaam.",
    ],
    werkwijze_slot=[
        "Waar passend gebruik ik ook hypnotherapie, systemisch werk en mindfulness. Samen kijken we wat bij jou past, vanuit rust, veiligheid en vertrouwen.",
    ],
    aanbod=[
        ("Individuele therapie", "Persoonlijke begeleiding bij psychische en emotionele klachten, verlies en persoonlijke ontwikkeling. Met ruimte voor jouw verhaal.", "praktische-informatie.html", "Praktische informatie"),
        ("Familieopstellingen", "Inzicht in familiedynamieken, terugkerende patronen en de invloed daarvan op jouw leven en relaties.", "familieopstellingen.html", "Lees meer"),
        ("Workshops", "Over zelfzorg, rouw, scheiding, verlies en verandering. Met aandacht voor bewustwording, verbinding en groei.", "workshops.html", "Bekijk de workshops"),
    ],
    voorstellen=[
        "Ik ben Liesbeth Postma, gediplomeerd psychosociaal en lichaamsgericht therapeut.",
        "Naast mijn opleidingen neem ik mijn eigen doorleefde ervaring mee. Het leven heeft mij geleerd hoe ingrijpend verlies en verandering zijn, hoe het voelt om jezelf kwijt te raken en opnieuw te ontdekken wat je voelt en nodig hebt.",
        "Die ervaring leerde mij gevoelens niet langer weg te stoppen, maar er met zachtheid naar te luisteren.",
        "Mijn kracht ligt in de combinatie van professionele kennis, doorleefde ervaring en oprechte betrokkenheid.",
        "",
        "Ik begeleid vanuit rust, gelijkwaardigheid en vertrouwen, in jouw tempo.",
    ],
    slot=[
        "Verandering begint vaak bij opnieuw contact maken met jezelf. Door ruimte te geven aan je gevoelens en behoeften kan stap voor stap meer inzicht, rust en vertrouwen ontstaan.",
        "Je hoeft het niet alleen te doen. Je bent van harte welkom.",
    ],
)

PAGINAS = {}

PAGINAS["jongvolwassenen"] = dict(
    kop="Jongvolwassenen & faalangst", sub="Als je bang bent om het niet goed genoeg te doen", foto="natuur-bloemen.jpg",
    seo_titel="Faalangst en onzekerheid bij jongvolwassenen | Liesbeth Postma",
    seo="Last van faalangst, prestatiedruk of onzekerheid? Ontdek begeleiding om patronen te herkennen, grenzen te voelen en meer op jezelf te vertrouwen.",
    blokken=[
        ("p", "Misschien leg je de lat hoog. Je wilt het goed doen, niemand teleurstellen en voldoen aan wat er van je verwacht wordt. Aan de buitenkant lijkt het prima te gaan, maar vanbinnen voel je onzekerheid, spanning of angst om fouten te maken."),
        ("quote", "Doe ik het wel goed? Ben ik wel goed genoeg?"),
        ("h2", "Faalangst en prestatiedruk"),
        ("p", "Faalangst gaat niet alleen over studie of werk. Het gaat ook over de angst om verkeerde keuzes te maken of anderen teleur te stellen. Misschien herken je dat je:"),
        ("ul", ["bang bent om fouten te maken;", "veel van jezelf verwacht en perfectionistisch bent;", "jezelf vergelijkt met anderen;", "moeilijk nee kunt zeggen en veel bevestiging zoekt;", "voortdurend nadenkt over wat je zou moeten doen;", "niet goed meer weet wat jij zelf wilt."]),
        ("p", "Wie lang probeert te voldoen aan verwachtingen, raakt het contact met zichzelf steeds meer kwijt."),
        ("h2", "Van moeten naar voelen wat bij jou past"),
        ("p", "We kijken niet alleen naar hoe je van je faalangst afkomt, maar ook naar wat eronder ligt. Waar heb je geleerd dat je het goed moet doen? Wat gebeurt er in je lichaam als je bang bent om te falen? En wat zou jij kiezen als je minder bang was voor wat anderen vinden?"),
        ("p", "Ik help je je gevoelens, patronen en lichaamssignalen beter te herkennen, onder andere met lichaamsgerichte therapie, innerlijk-kindwerk, delenwerk en ACT. Zo leer je steeds beter voelen wat voor jou belangrijk is."),
        ("h2", "Meer vertrouwen in jezelf"),
        ("p", "Je hoeft niet alles zeker te weten om stappen te zetten. Wanneer je leert luisteren naar jezelf en je grenzen, ontstaat ruimte om te kiezen vanuit vertrouwen in plaats van angst."),
        ("motto",),
        ("cta", "Neem contact op", "contact.html"),
        ("begeleiding",),
    ])

PAGINAS["mentaal-vastlopen"] = dict(
    kop="Als je mentaal vastloopt", sub="Misschien gaat het aan de buitenkant best goed", foto="water-zit.jpg",
    seo_titel="Mentaal vastlopen, stress en burn-out | Liesbeth Postma",
    seo="Loop je vast door stress, angst, somberheid of burn-out? Ontdek psychosociale en lichaamsgerichte begeleiding vanuit rust en vertrouwen.",
    blokken=[
        ("p", "Je doet wat er van je verwacht wordt: studeren, werken, zorgen voor anderen, alle ballen in de lucht houden. Maar vanbinnen voelt het anders. Je piekert, bent moe of gespannen, twijfelt aan jezelf en hebt het gevoel tekort te schieten."),
        ("quote", "Je probeert door te gaan, maar ergens voel je: ik kan of wil dit niet langer op deze manier."),
        ("h2", "Als angst steeds meer ruimte inneemt"),
        ("p", "Angst laat zich op veel manieren zien: als faalangst, onzekerheid, perfectionisme, moeite met kiezen of bang zijn voor wat anderen vinden. Misschien herken je dat je:"),
        ("ul", ["hoge eisen aan jezelf stelt en veel piekert;", "bevestiging bij anderen zoekt;", "moeilijk nee kunt zeggen;", "je grenzen pas merkt wanneer je er al overheen bent;", "niet goed weet wat jíj eigenlijk wilt."]),
        ("p", "Juist als jongvolwassene komt er veel op je af: studie, werk, relaties, sociale media en keuzes over je toekomst. Onder faalangst zit vaak meer dan de angst om iets fout te doen. Misschien heb je geleerd dat je vooral waardering krijgt als je presteert. Dan kan de vraag ‘Wat wil ik eigenlijk?’ ineens heel moeilijk zijn."),
        ("h2", "Stress en burn-out"),
        ("p", "Langdurig doorgaan terwijl je lichaam om rust vraagt, kan leiden tot stress- en burn-outklachten: prikkelbaarheid, slecht slapen, piekeren, emotioneel zijn of juist weinig voelen. Je lichaam werkt je niet tegen; het signaleert dat je te lang over je grenzen bent gegaan."),
        ("p", "Daarom kijken we niet alleen naar hoe je snel weer kunt functioneren, maar ook naar waarom je zo lang bent doorgegaan en welke patronen daarin meespelen."),
        ("h2", "Somberheid en jezelf kwijtraken"),
        ("p", "Soms voel je vooral leegte of somberheid. Dingen die je plezier gaven, doen je minder. Je trekt je terug en hebt het gevoel jezelf ergens te zijn kwijtgeraakt. Soms begint verandering juist bij stilstaan en voelen wat er werkelijk in je leeft."),
        ("h2", "Hooggevoeligheid"),
        ("p", "Ben je gevoelig voor prikkels en stemmingen van anderen, dan komt de wereld intens binnen. Je voelt snel aan wat een ander nodig heeft, maar moeilijker wat jij nodig hebt."),
        ("quote", "Wat is van mij en wat is van de ander? En waar ligt mijn grens?"),
        ("p", "Hooggevoeligheid is geen zwakte. Wanneer je jezelf en je grenzen beter leert kennen, wordt gevoeligheid een kwaliteit."),
        ("h2", "We kijken naar wat er onder ligt"),
        ("p", "We onderzoeken samen wat jouw gevoelens, gedachten en lichaam je proberen te vertellen. Welke patronen heb je ontwikkeld? Waar heb je geleerd jezelf aan te passen? En wat heb jij nodig om je weer veilig genoeg te voelen om jezelf te zijn? Niet iedere sessie is hetzelfde; we kijken wat op dat moment bij jou past."),
        ("h2", "Leer te voelen – durf te vertrouwen"),
        ("p", "Het doel is niet dat je nooit meer bang, onzeker of verdrietig bent. Het gaat erom dat je jezelf beter leert kennen en dragen, je grenzen voelt, keuzes durft te maken die bij jou passen en steeds meer vertrouwt op je eigen gevoel."),
        ("stroom",),
        ("cta2", "Lees meer over mijn werkwijze", "werkwijze.html", "Plan een kennismaking", "contact.html"),
        ("begeleiding",),
    ])

PAGINAS["verlies-en-verandering"] = dict(
    kop="Verlies & verandering", sub="Begeleiding bij rouw, verlies en grote veranderingen", foto="natuur-zonsondergang.jpg",
    seo_titel="Begeleiding bij rouw, verlies en verandering | Liesbeth Postma",
    seo="Een scheiding, overlijden of verlies van werk of thuis kan diep raken. Ontdek persoonlijke begeleiding bij rouw, verlies en grote veranderingen.",
    blokken=[
        ("p", "Verlies gaat niet alleen over het overlijden van iemand van wie je houdt. Ook een scheiding, verlies van gezondheid, werk, een thuis of toekomstbeeld kan een rouwproces veroorzaken. Rouw om wat er was, om wat je mist of om wat je dacht dat er zou zijn."),
        ("p", "Je kunt verdriet, angst, boosheid, onrust of leegte ervaren, veel piekeren, slecht slapen of het gevoel hebben jezelf te zijn kwijtgeraakt."),
        ("h2", "Therapie bij rouw en verlies"),
        ("p", "Ik begeleid mensen die vastlopen na rouw, verlies of een ingrijpende verandering. Ik kijk niet alleen naar je gedachten en gevoelens, maar ook naar wat je lichaam meedraagt. Soms raakt een verlies aan ouder verdriet, aan angst om verlaten te worden of eerdere afwijzing. Samen onderzoeken we wat jij nodig hebt om het verlies een plek te geven en opnieuw vertrouwen te ervaren."),
        ("h2", "Verder na verlies"),
        ("quote", "Verdergaan betekent niet vergeten."),
        ("p", "Langzaam mag er naast verdriet weer ruimte ontstaan voor rust, verbinding, betekenis en vertrouwen."),
        ("motto",),
        ("cta", "Neem contact op", "contact.html"),
        ("begeleiding",),
    ])

PAGINAS["relaties"] = dict(
    kop="Jezelf verliezen in relaties", sub="Wanneer je steeds verder van jezelf af komt te staan", foto="boom-zit.jpg",
    seo_titel="Narcisme, codependentie en jezelf verliezen in relaties | Liesbeth Postma",
    seo="Raak je jezelf kwijt in een narcistische relatie, codependentie of emotionele afhankelijkheid? Ontdek begeleiding bij grenzen, patronen en zelfvertrouwen.",
    blokken=[
        ("p", "Misschien pas je je gemakkelijk aan de ander aan. Je voelt sterk aan wat iemand nodig heeft, maar staat zelden stil bij wat jij voelt. Je wilt de verbinding behouden en conflicten voorkomen, en gaat daardoor steeds vaker over je eigen grenzen heen."),
        ("h2", "Patronen in relaties"),
        ("p", "Vaak zijn deze patronen vroeg ontstaan: je leerde je aan te passen, voor anderen te zorgen of bevestiging buiten jezelf te zoeken. Wat ooit hielp om je veilig te voelen, zit je nu in de weg. Zonder oordeel onderzoeken we wat eronder ligt. Wat gebeurt er als je bang bent iemand kwijt te raken? Waar voel je jouw grens? Wat is van jou en wat draag je voor een ander?"),
        ("h2", "Narcisme, narcistische relaties en emotionele afhankelijkheid"),
        ("p", "Misschien herken je een relatie waarin jouw gevoelens en behoeften steeds minder ruimte krijgen. Je twijfelt aan jezelf en bent voortdurend bezig met de stemming van de ander. Soms spelen manipulatie, kleineren, schuldgevoel, gaslighting of wisselende nabijheid en afstand een rol."),
        ("p", "Woorden als narcisme of narcistische relatie kunnen herkenning geven, maar niet elk kwetsend gedrag betekent een persoonlijkheidsstoornis. Een diagnose van de ander is niet nodig om serieus te nemen wat een relatie met jou doet."),
        ("h2", "Codependentie en pleasegedrag"),
        ("p", "Bij codependentie raak je gericht op de behoeften en goedkeuring van de ander. Je voelt je verantwoordelijk voor diens welzijn, stelt moeilijk grenzen of blijft hopen dat de relatie verandert, ook als je jezelf daarin verliest. We onderzoeken hoe deze patronen zijn ontstaan en hoe je weer op je eigen gevoel en grenzen kunt vertrouwen."),
        ("h2", "Herstellen na een ongezonde relatie"),
        ("p", "Ook na een relatiebreuk kun je worstelen met verdriet, twijfel, schuldgevoel of de neiging om weer contact te zoeken. We werken aan het herkennen van relationele patronen, het verwerken van verlies en het stap voor stap versterken van zelfvertrouwen en autonomie."),
        ("h2", "Van afhankelijkheid naar vertrouwen in jezelf"),
        ("p", "Het doel is niet om afstand te nemen van verbinding, maar om jezelf binnen die verbinding niet meer kwijt te raken. Ik combineer waar passend psychosociale therapie, lichaamsgericht werken, innerlijk-kindwerk, delenwerk en ACT. Zorgvuldig, vanuit jouw motivatie en in jouw tempo."),
        ("motto",),
        ("cta", "Neem contact op", "contact.html"),
        ("begeleiding",),
    ])

PAGINAS["werkwijze"] = dict(
    kop="Mijn werkwijze", sub="Begeleiding die aansluit bij jou", foto="natuur-boom.jpg",
    seo_titel="Mijn werkwijze: voelen, begrijpen en vertrouwen | Liesbeth Postma",
    seo="Lees hoe psychosociale therapie, lichaamsgericht werken, innerlijk-kindwerk, delenwerk en ACT samenkomen in mijn persoonlijke begeleiding.",
    blokken=[
        ("p", "Ik kijk naar jou als geheel: naar wat je denkt en voelt, naar je lichaam, je ervaringen en de patronen die je meedraagt. Soms begrijp je met je hoofd waar iets vandaan komt, terwijl er vanbinnen nog iets geraakt wordt. Daarom werken we niet alleen met woorden, maar ook met wat je lichaam aangeeft."),
        ("h2", "Psychosociaal, lichaamsgericht en systemisch"),
        ("p", "Ik combineer psychosociale therapie, lichaamsgerichte hypnotherapie en systemisch werk, aangevuld met regressie, innerlijk-kindwerk, familieopstellingen, ACT, EFT, Transactionele Analyse en delenwerk waar dat past. Bij systemisch werk kijken we ook naar je gezin van herkomst en patronen die al langer worden doorgegeven."),
        ("pijlers",),
        ("h2", "Verandering is een proces"),
        ("p", "Je hoeft niet alles in één keer te begrijpen of te veranderen. Stap voor stap ontstaat ruimte om te voelen, patronen te herkennen, los te laten wat niet langer helpt en te ontdekken wat bij jou past."),
        ("quote", "Geen vast stappenplan, maar begeleiding die aansluit bij jou, jouw verhaal en jouw tempo."),
        ("h2", "Eigen regie"),
        ("p", "Verandering begint bij jouw bereidheid om naar jezelf te kijken. Ik bied begeleiding, inzicht en een veilige plek; jij bepaalt de stappen en het tempo. Je hoeft het niet alleen te doen, maar jouw proces blijft van jou."),
        ("h2", "Wat kan de begeleiding je brengen?"),
        ("ul", ["Meer rust en ruimte in je hoofd en lichaam.", "Jezelf beter begrijpen en oude patronen herkennen.", "Gevoelens toelaten in plaats van wegdrukken.", "Je behoeften en grenzen herkennen en aangeven.", "Minder afhankelijk zijn van goedkeuring van anderen.", "Met meer mildheid naar jezelf kijken.", "Meer zelfvertrouwen en innerlijke veiligheid.", "Verlies en verandering een plek geven.", "Keuzes maken die passen bij wie jij werkelijk bent."]),
        ("p", "Het gaat er niet om dat je nooit meer angst of verdriet voelt. Het gaat erom dat je ermee leert omgaan zonder jezelf te verliezen."),
        ("quote", "Van overleven naar leven."),
        ("motto",),
        ("cta", "Neem contact op", "contact.html"),
    ])

PAGINAS["over-mij"] = dict(
    kop="Over mij", sub="Ik ben Liesbeth", foto="wilg-lach.jpg",
    seo_titel="Over Liesbeth Postma | Psychosociaal en lichaamsgericht therapeut",
    seo="Maak kennis met Liesbeth Postma: moeder van twee kinderen en therapeut. Professionele kennis, doorleefde ervaring en begeleiding vanuit rust en vertrouwen.",
    blokken=[
        ("p", "Ik ben Liesbeth Postma, moeder van twee prachtige kinderen en psychosociaal en lichaamsgericht therapeut. In mijn werk kijk ik niet alleen naar klachten, maar naar de mens als geheel: wat je hebt meegemaakt, welke patronen je hebt ontwikkeld en wat je lichaam je vertelt. Die manier van kijken komt uit mijn opleidingen én uit mijn eigen levenservaring."),
        ("h2", "Ook ik weet wat het betekent om vast te lopen"),
        ("p", "Mijn eigen leven heeft mij geleerd wat verlies, verandering en opnieuw beginnen betekenen. Ik weet hoe het is om lang door te gaan, jezelf kwijt te raken en uiteindelijk niet meer te kunnen. Door te vertragen en ruimte te maken voor wat mijn lichaam mij vertelde, leerde ik steeds meer op mezelf te vertrouwen."),
        ("quote", "Niet omdat jouw verhaal hetzelfde is als het mijne, maar omdat ik weet hoe belangrijk het is dat iemand naast je blijft staan zonder direct te willen oplossen wat je voelt."),
        ("h2", "Een plek waar je mag zijn wie je bent"),
        ("p", "Gelijkwaardigheid, respect en vertrouwen staan voorop. Je hoeft bij mij niet eerst beter, sterker of anders te worden. We onderzoeken samen wat er speelt en wat jij nodig hebt om weer beweging te ervaren. Mijn begeleiding is psychosociaal, lichaamsgericht en systemisch, altijd afgestemd op jou."),
        ("h2", "Professionele kennis en doorleefde ervaring"),
        ("p", "Ik ben gediplomeerd psychosociaal en lichaamsgericht therapeut en blijf mij ontwikkelen door trainingen en bijscholing. Ik geloof dat verandering van binnenuit begint: bij de bereidheid om naar jezelf te kijken en te investeren in je eigen groei."),
        ("quote", "Leren voelen en vertrouwen ontwikkelen is een weg die je zelf bewandelt. Ik loop graag een stukje met je mee."),
        ("stroom",),
        ("reviews",),
        ("cta2", "Maak kennis met mijn werkwijze", "werkwijze.html", "Neem contact op", "contact.html"),
    ])

TARIEVEN = [
    ("Intakegesprek", "60 minuten", "€ 80", "We nemen de tijd om kennis te maken, je hulpvraag te verhelderen en richting te geven aan de verandering die je wenst."),
    ("Vervolgsessie", "90 minuten", "€ 120", "Ruimte om verder de diepte in te gaan en te werken aan jouw hulpvraag."),
    ("Bundel", "5 sessies", "€ 555", "Gericht werken aan verandering en je sessies inzetten wanneer jij ze nodig hebt."),
]

PAGINAS["praktische-informatie"] = dict(
    kop="Praktische informatie", sub="Een afspraak bij Liesbeth Postma", foto="natuur-meer.jpg",
    seo_titel="Praktische informatie en tarieven | Liesbeth Postma",
    seo="Lees alles over de intake, sessies, tarieven en praktische afspraken bij Liesbeth Postma, psychosociaal en lichaamsgericht therapeut.",
    blokken=[
        ("p", "Wil je onderzoeken of mijn begeleiding bij jou past? Tijdens het intakegesprek maken we kennis, verhelderen we je hulpvraag en stemmen we de begeleiding af op wat jij nodig hebt."),
        ("h2", "Tarieven"),
        ("tarieven",),
        ("p", "Alle tarieven zijn inclusief btw. Soms vergoedt een werkgever (een deel van) de kosten, bijvoorbeeld bij preventie, herstel of re-integratie. Vraag het na bij je werkgever of bedrijfsarts."),
        ("quote", "Zie het als een investering in jezelf. Je bent het waard."),
        ("h2", "Vergoeding door de zorgverzekering"),
        ("p", "Mijn sessies worden niet vergoed vanuit de zorgverzekering. De kosten en het verloop van de begeleiding bespreken we vooraf, zodat je een bewuste keuze kunt maken."),
        ("h2", "Locatie"),
        ("box", "Tijdelijke praktijklocatie", ["Dijkstraat 20, Bemmel", "Vanuit deze locatie begeleid ik cliënten uit onder andere Bemmel, Elst, Overbetuwe, Lingewaard, Arnhem en Nijmegen."]),
        ("h2", "Afspraak maken"),
        ("p", "Voel je dat het tijd is om iets te veranderen? Neem gerust contact op. Samen kijken we of mijn manier van werken bij jou past."),
        ("motto",),
        ("cta", "Neem contact op", "contact.html"),
    ])

PAGINAS["contact"] = dict(
    kop="Contact & kennismaken", sub="Misschien voel je dat het tijd is", foto="portret-lach.jpg",
    seo_titel="Contact en kennismaken | Liesbeth Postma",
    seo="Wil je ontdekken of mijn begeleiding bij je past? Neem contact op met Liesbeth Postma voor een telefonisch kennismakingsgesprek.",
    blokken=[
        ("p", "Je hoeft niet precies te weten wat er moet veranderen. Misschien voel je alleen dat je niet langer op dezelfde manier verder wilt. Dat kleine gevoel van binnen – ik wil iets anders – kan al genoeg zijn om de eerste stap te zetten."),
        ("h2", "Je bent welkom"),
        ("p", "Je hoeft niet binnen te komen met een compleet verhaal. We beginnen waar jij bent. Tijdens onze eerste ontmoeting kijken we rustig naar wat er speelt en waar je naar verlangt. Belangrijk is dat jij kunt voelen of ik de juiste persoon ben om een stukje met je mee te lopen."),
        ("h2", "Neem gerust contact op"),
        ("p", "Een kennismakingsgesprek vindt telefonisch plaats."),
        ("contact",),
        ("quote", "Je hoeft de hele weg nog niet te kennen. Alleen de eerste stap."),
        ("motto",),
    ])

PAGINAS["familieopstellingen"] = dict(
    kop="Familieopstellingen", sub="Inzicht in wat je met je meedraagt", foto="natuur-boom.jpg",
    seo_titel="Familieopstellingen en patronen herkennen | Liesbeth Postma",
    seo="Ontdek hoe familieopstellingen je kunnen helpen om patronen, relaties en familiedynamieken met meer inzicht en begrip te bekijken.",
    blokken=[
        ("p", "Soms kom je steeds in dezelfde patronen terecht, in je gezin, relaties of in hoe je naar jezelf kijkt. Een familieopstelling helpt om anders te kijken naar jouw plek in het familiesysteem, naar loyaliteit en naar verantwoordelijkheden die je ongemerkt bent gaan dragen."),
        ("h2", "Ruimte voor bewustwording"),
        ("p", "Een opstelling biedt nieuwe perspectieven, zonder dat er één vast antwoord hoeft te zijn. Je blijft vrij om te voelen wat voor jou klopt, met aandacht voor jouw grenzen en tempo."),
        ("h2", "Leer te voelen – durf te vertrouwen"),
        ("p", "Door te zien wat van jou is en wat je van anderen bent gaan dragen, ontstaat ruimte voor nieuwe keuzes."),
        ("cta", "Neem contact op over familieopstellingen", "contact.html"),
    ])

PAGINAS["workshops"] = dict(
    kop="Workshops", sub="Goed voor jezelf zorgen bij verlies en verandering", foto="natuur-heide.jpg",
    seo_titel="Workshops zelfzorg, rouw en verandering | Liesbeth Postma",
    seo="Workshops over goed voor jezelf zorgen na een scheiding, verlies of verandering. Met ruimte voor bewustwording, verbinding en groei.",
    blokken=[
        ("p", "Een scheiding, het overlijden van een dierbare, verlies van werk of een andere grote verandering zet je leven op zijn kop. Juist dan is het moeilijk stil te staan bij wat jij nodig hebt. In mijn workshops is ruimte voor herkenning, gevoelens en praktische oefeningen. Je hoeft niets te delen wat je niet wilt."),
        ("h2", "Thema's"),
        ("ul", ["Rouw en ruimte geven aan verdriet.", "Grenzen herkennen en aangeven.", "Jezelf niet verliezen in zorg voor anderen.", "Zelfzorg en veerkracht.", "Opnieuw vertrouwen opbouwen en je eigen weg vinden."]),
        ("h2", "Een veilige plek om stil te staan"),
        ("p", "We werken in een kleine, rustige groep met respect voor ieders verhaal. De nadruk ligt op aandacht, eigen regie en kleine stappen die bij jou passen."),
        ("box", "Data en locatie", ["Data, locatie en praktische informatie worden per workshop bekendgemaakt. Wil je op de hoogte blijven? Laat het me weten."]),
        ("cta", "Informeer naar workshops", "contact.html"),
    ])

BLOG = dict(
    kop="Blog", sub="Over voelen, vertrouwen en persoonlijke groei",
    seo_titel="Blog over voelen, vertrouwen en persoonlijke groei | Liesbeth Postma",
    seo="Lees mijn blogs over persoonlijke ontwikkeling, relaties, verlies, verandering, voelen en vertrouwen. Eerdere verhalen én nieuwe inzichten.",
    intro=["Hier deel ik mijn gedachten, inzichten en ervaringen over voelen, vertrouwen, persoonlijke ontwikkeling, relaties, verlies en verandering. Je vindt hier mijn eerdere blogs én nieuwe artikelen."],
)

OUD = "Dit artikel verscheen eerder op de website van Praktijk De Magnolia, de vorige naam van mijn praktijk."

ARTIKELEN = [
    dict(slug="van-de-magnolia-naar-liesbeth-postma",
         titel="Een nieuwe naam, dichter bij mezelf", onder="Van Praktijk De Magnolia naar Liesbeth Postma",
         datum="4 november 2026", foto="portret-deur.jpg",
         seo_titel="Van Praktijk De Magnolia naar Liesbeth Postma | Blog",
         seo="Waarom Praktijk De Magnolia verdergaat als Liesbeth Postma: een nieuwe naam, een zachter logo en dezelfde essentie.",
         intro="Soms komt er een moment waarop je voelt dat iets mag veranderen. Niet omdat het oude niet meer goed is, maar omdat je zelf bent gegroeid.",
         blokken=[
            ("p", "Soms komt er een moment in je leven waarop je voelt dat iets mag veranderen. Niet omdat het oude niet meer goed is, maar omdat je zelf bent gegroeid. Dat moment is voor mij aangebroken."),
            ("p", "Met liefde en dankbaarheid neem ik afscheid van de naam Praktijk De Magnolia en ga ik verder onder mijn eigen naam: Liesbeth Postma – Psychosociaal en lichaamsgericht therapeut."),
            ("p", "De afgelopen jaren hebben mij veel geleerd over verlies, verandering, loslaten en opnieuw beginnen. Maar vooral over trouw blijven aan jezelf. Ik heb geleerd op eigen benen te staan, verantwoordelijkheid te nemen voor mijn leven en te vertrouwen op wie ik ben."),
            ("quote", "En misschien wel het belangrijkste: dat ik, gewoon als Liesbeth, precies goed ben zoals ik ben."),
            ("h2", "Een boom met een verhaal"),
            ("p", "Ook mijn logo heeft een zachtere uitstraling gekregen. De boom blijft, net als het hart dat hem omringt. De boom staat voor persoonlijke groei, veerkracht en verbinding met jezelf. De wortels staan voor stevig geaard zijn, een basis van waaruit je kunt groeien. Het hart staat voor liefde, zachtheid en verbinding."),
            ("quote", "Zacht in uitstraling, stevig in basis."),
            ("p", "Kracht betekent voor mij niet dat je altijd sterk moet zijn. Juist door ruimte te geven aan je kwetsbaarheid en je gevoelens kan nieuwe kracht ontstaan."),
            ("h2", "Vanuit mijn eigen kracht"),
            ("p", "Ook als therapeut kies ik steeds bewuster mijn eigen weg: vanuit professionele kennis, doorleefde ervaring en begeleiding vanuit rust, gelijkwaardigheid en vertrouwen. Ik geloof dat verandering begint bij jezelf. Niet om iemand anders te worden, maar om steeds meer jezelf te mogen zijn."),
            ("p", "Mijn praktijk blijft een plek waar je welkom bent met jouw verhaal. Naast individuele therapie bied ik ook familieopstellingen en workshops rondom zelfzorg, rouw en verandering."),
            ("h2", "Leer te voelen – durf te vertrouwen"),
            ("p", "De naam verandert, maar de essentie van mijn werk blijft hetzelfde. Met mijn eigen naam, een vernieuwd logo en een heldere visie zet ik een volgende stap. Een stap die voelt als thuiskomen bij mezelf."),
            ("p", "Lieve groet,<br><strong>Liesbeth Postma</strong><br><em>Psychosociaal en lichaamsgericht therapeut</em>"),
         ]),
    dict(slug="wat-zingeving-voor-mij-betekent",
         titel="Wat zingeving voor mij betekent", onder="Voelen wat klopt, ook als het leven niet vanzelf gaat",
         datum="3 november 2025", foto="natuur-bloemen.jpg",
         seo_titel="Wat zingeving voor mij betekent | Blog Liesbeth Postma",
         seo="Wat geeft je leven zin in een periode waarin het niet vanzelf gaat? Over voelen wat klopt, verbinding en groei.",
         intro="De laatste tijd stel ik mezelf steeds vaker de vraag: wie of wat geeft mijn leven zin? Juist in een periode waarin het leven niet vanzelf gaat.",
         blokken=[
            ("p", "De laatste tijd stel ik mezelf steeds vaker de vraag: wie of wat geeft mijn leven zin? Wat is zingeving in een periode waarin het leven niet vanzelf gaat? Waar haal ik voldoening uit, juist als dingen tegenzitten?"),
            ("p", "Het zijn vragen die mij bezighouden, maar die ik ook vaak hoor van de mensen die ik begeleid. We kennen allemaal momenten waarop het leven schuurt, waarin oude zekerheden wankelen en we onszelf opnieuw moeten uitvinden. Juist dan komt die diepe vraag naar boven: wat geeft mijn leven betekenis?"),
            ("h2", "Zingeving is voelen wat voor mij klopt"),
            ("p", "Zingeving is niet iets wat ik kan bedenken met mijn hoofd, maar iets wat ik voel. Ik ervaar het wanneer ik dingen doe waar mijn energie van gaat stromen. Dat kan in kleine momenten zitten: een goed gesprek, iemand écht zien, of simpelweg aanwezig zijn zonder iets te hoeven veranderen. Maar ook in goed voor mezelf zorgen, van een huis een thuis maken en werk doen waarin ik mijn kwaliteiten kwijt kan."),
            ("p", "De mensen om mij heen spelen daarin een belangrijke rol. Ik voel zin in het leven wanneer ik in verbinding ben met mensen bij wie gelijkwaardigheid en wederkerigheid aanwezig zijn. Relaties waarin geven en ontvangen in balans zijn."),
            ("h2", "Zingeving in moeilijke tijden"),
            ("p", "Tegenslagen horen bij het leven. Soms haalt het je onderuit, soms zet het alles in een nieuw perspectief. Juist dan besef ik hoe belangrijk het is om trouw te blijven aan wat voor mij betekenis heeft. Zingeving is dan niet het vinden van antwoorden, maar het aangaan van wat er is: emoties toelaten, luisteren naar mijn lichaam, durven stilstaan in plaats van doorgaan."),
            ("p", "In mijn werk zie ik hoe waardevol het is om ook in moeilijke tijden te blijven voelen wat klopt. Het lichaam weet vaak beter dan het hoofd waar onze richting ligt. Wanneer we die verbinding herstellen, ontstaat er ruimte voor rust, inzicht en nieuwe betekenis."),
            ("h2", "De zin van groei"),
            ("p", "Zingeving is voor mij een voortdurend proces. Het beweegt mee met het leven. Soms is het helder en licht, soms troebel en verwarrend, maar altijd aanwezig. Elke ervaring, hoe pijnlijk of mooi ook, draagt bij aan mijn groei als mens én als therapeut."),
            ("quote", "Zingeving is niet één antwoord, maar een manier van leven. Een keuze om te blijven luisteren naar wat klopt."),
            ("p", f"<small>{OUD}</small>"),
         ]),
    dict(slug="trauma-expertise-centrum",
         titel="Samenwerking tussen reguliere en complementaire zorg", onder="Aangesloten bij het Trauma Expertise Centrum",
         datum="30 augustus 2025", foto="natuur-bomen.jpg",
         seo_titel="Aangesloten bij het Trauma Expertise Centrum | Blog Liesbeth Postma",
         seo="Waarom ik als RBCZ-therapeut ben aangesloten bij het Trauma Expertise Centrum: kortere wegen naar hulp bij trauma.",
         intro="Als RBCZ-professional heb ik mijn praktijk aangesloten bij het Trauma Expertise Centrum, een initiatief dat cliënten met een hulpvraag rond trauma en zorgaanbieders bij elkaar brengt.",
         blokken=[
            ("p", "Als RBCZ-professional heb ik mijn praktijk aangesloten bij het Trauma Expertise Centrum. De stichting brengt cliënten met een hulpvraag op het gebied van trauma en zorgaanbieders bij elkaar. Het initiatief is ontstaan als antwoord op de lange wachtlijsten in de reguliere zorg (GGZ). Mensen die hulp nodig hebben, worden nu vaak van het kastje naar de muur gestuurd omdat een heldere routing ontbreekt. Dat komt de mentale en fysieke gezondheid niet ten goede."),
            ("p", "Externe factoren zoals het verlies van een baan, een burn-out of een scheiding kunnen klachten veroorzaken of triggeren. Het is belangrijk te beseffen dat trauma niet de gebeurtenis zelf is, maar wat er in iemand gebeurt door die situatie. Gabor Maté, arts en trauma-expert, spreekt over “naar binnen keren en leren voelen”. Contact maken met onze innerlijke wereld is essentieel om echt te kunnen helen."),
            ("quote", "Een mooie stap richting een sterke samenwerking tussen de reguliere en complementaire zorg."),
            ("p", "Ik ben blij en dankbaar dat ik als therapeut deel mag uitmaken van dit initiatief. Ben jij op zoek naar een professionele therapeut? Of ben je huisarts, bedrijfsarts of verwijzer? Neem gerust <a href='../contact.html'>contact</a> op."),
            ("p", f"<small>{OUD}</small>"),
         ]),
    dict(slug="herstel-je-balans",
         titel="Herstel je balans", onder="Psychosociale en lichaamsgerichte hypnotherapie",
         datum="11 augustus 2025", foto="natuur-water.jpg",
         seo_titel="Herstel je balans met psychosociale en lichaamsgerichte hypnotherapie | Blog",
         seo="Hoe psychosociale en lichaamsgerichte hypnotherapie helpt om in tijden van crisis opnieuw verbinding te maken met je energie, veerkracht en balans.",
         intro="In tijden van crisis of ontregeling kan het voelen alsof je jezelf even kwijt bent. Hoe je opnieuw verbinding maakt met je energie, veerkracht en innerlijke balans.",
         blokken=[
            ("p", "Als psychosociaal en lichaamsgericht therapeut begeleid ik volwassenen en jongvolwassenen die vastlopen in het dagelijks leven. Ook mensen met een sterk ontwikkelde hooggevoeligheid (HSP) vinden bij mij de ruimte die zij nodig hebben."),
            ("p", "In tijden van crisis of ontregeling kan het voelen alsof je jezelf even kwijt bent. Therapie helpt je om opnieuw verbinding te maken met je energie, veerkracht en innerlijke balans. We werken aan zelfinzicht, het versterken van je zelfbeeld en het leren omgaan met emoties, zodat je weer grip krijgt op je leven."),
            ("h2", "Een vertrouwde omgeving waarin jij jezelf mag zijn"),
            ("quote", "In je leven maak je situaties mee die je vormen. Je leert manieren om te overleven, zodat je niet hoeft te voelen. Ik bied je een veilige bedding waarin je weer mag voelen, mag delen en mag zijn."),
            ("p", "Mensen met hooggevoeligheid ervaren de wereld intenser. Ze voelen emoties van anderen sterk aan en verliezen daardoor soms het contact met hun eigen behoeften. Zeker bij vroegkinderlijk trauma kan dit leiden tot overlevingsgedrag, zoals pleasen of jezelf wegcijferen."),
            ("p", "Met lichaamsgerichte therapie leer je opnieuw luisteren naar wat jouw lichaam te vertellen heeft. We onderzoeken welke spanningen en onverwerkte ervaringen je lichaam nog vasthoudt. Want trauma leeft niet alleen in je hoofd, het nestelt zich ook in je lijf."),
            ("h2", "Je energie weer laten stromen"),
            ("quote", "Wat je hoofd probeert te verklaren, is wat je lichaam niet heeft kunnen verwerken."),
            ("p", "Vastzittende energie kan je het gevoel geven gevangen te zitten tussen je verlangens en je realiteit. Door deze blokkades los te laten kan je levensenergie weer vrij stromen. Je komt opnieuw in contact met jouw behoeften, jouw kracht en jouw rust."),
            ("h2", "De oplossing zit al in jezelf"),
            ("p", "Hypnotherapie helpt je de regie over je leven terug te nemen. Tijdens een sessie richt je je aandacht rustig op je ademhaling en keer je naar binnen. Je lichaam ontspant en je komt in een diepe staat van rust, vergelijkbaar met dagdromen. In die innerlijke focus ontstaat ruimte om te werken aan wat je meebrengt. Jij behoudt altijd de regie; ik begeleid je binnen een veilig kader."),
            ("h2", "Mijn werkwijze"),
            ("p", "Ik werk intuïtief en afgestemd op jou. Geen mens is hetzelfde, dus geen traject is gelijk. Samen zetten we kleine, haalbare stappen in een veilige en oordeelloze omgeving, zodat je oude patronen kunt doorbreken."),
            ("p", f"<small>{OUD}</small>"),
         ]),
    dict(slug="doorgaan-als-het-moeilijk-wordt",
         titel="Doorgaan als het moeilijk wordt", onder="Na een burn-out, verlies, rouw of scheiding",
         datum="5 maart 2024", foto="natuur-zonsondergang.jpg",
         seo_titel="Doorgaan als het moeilijk wordt | Blog Liesbeth Postma",
         seo="Hoe ga je door na een burn-out, verlies van je baan, rouw of een scheiding? Over verbinding met jezelf en stap voor stap weer voelen.",
         intro="Hoe ga ik door na een burn-out, verlies van mijn baan, rouw of een scheiding? Een vraag die ik mijzelf stelde en die ik vaak hoor in mijn praktijk.",
         blokken=[
            ("p", "Hoe ga ik door na een burn-out, verlies van mijn baan, rouw of een scheiding? Het is een van de vele vragen die ik mijzelf stelde. Inmiddels hoor ik de vraag ook vaak in mijn praktijk."),
            ("ul", ["Het liefst wil je op je bed blijven liggen.", "Geen zin vandaag. Alles is toch al verloren.", "Het roept depressieve gevoelens op.", "Je raakt de verbinding met jezelf kwijt en vindt jezelf niets meer waard.", "Doorgaan is dan ontzettend zwaar en lukt niet meer in je eentje."]),
            ("p", "Boosheid die in je zit kan een emotionele blokkade vormen. Als je je gevoelens niet op een gezonde manier kunt uiten, krijg je na een tijdje fysieke en mentale klachten. In therapie ga je terug naar het eerste moment waarop je dit eerder voelde, zodat je kunt uiten wat toen niet mogelijk was. Je hebt jezelf beschermd, maar bent daarmee ook de verbinding met jezelf verloren. Door opnieuw te leren voelen, kunnen die blokkades langzaam worden opgeheven."),
            ("quote", "De pijn is niet jouw schuld, maar de heling ervan is wel jouw verantwoordelijkheid."),
            ("p", "Doorgaan als het moeilijk wordt gaat stap voor stap en heeft tijd nodig. Tijd met jezelf, tijd om goed voor jezelf te zorgen, tijd om te voelen waar jij weer voldoening in kunt vinden. Het wordt moeilijk als er geen doel meer is. Toch zijn er in ieders leven lichtpuntjes. Als je weer leert voelen, kom je langzaam in je eigen kracht te staan."),
            ("p", f"<small>{OUD}</small>"),
         ]),
    dict(slug="jouw-plek-in-het-familiesysteem",
         titel="Jouw plek in het familiesysteem", onder="Over afwijzing, loyaliteit en de onderstroom",
         datum="31 juli 2023", foto="natuur-boom.jpg",
         seo_titel="Jouw plek in het familiesysteem | Blog Liesbeth Postma",
         seo="Hoe ons familiesysteem een diepe imprint achterlaat en waarom we steeds in oude patronen terugvallen. Over systemisch kijken.",
         intro="Je afgewezen voelen doet pijn. Het ondermijnt je zelfvertrouwen en kan leiden tot een diepe angst voor toekomstige afwijzing. Hoe komt dat?",
         blokken=[
            ("p", "Je afgewezen voelen doet pijn. Het ondermijnt je zelfvertrouwen en doet je twijfelen aan je eigenwaarde. Of je het nu vaak hebt meegemaakt of maar een paar keer, het kan leiden tot een diepe angst voor toekomstige afwijzing. Die angst kan je ervan weerhouden om zelfs maar te proberen je dromen te verwezenlijken."),
            ("p", "Hoe komt dit? Ons familiesysteem laat een diepe imprint achter. De dynamieken in dat systeem, onze loyaliteit en de werking van de zogenaamde onderstroom beïnvloeden ons dagelijks functioneren. Die onderstroom zorgt ervoor dat we steeds opnieuw terugvallen in oude patronen en onbewuste verstrengeling met onze familie. Dat zie je terug in zich herhalend gedrag en zich herhalende situaties."),
            ("quote", "Je krijgt zicht op wat van jou is en wat je meedraagt vanuit je familiesysteem."),
            ("p", "Ik kijk ook systemisch. Wat je van anderen bent gaan dragen, kun je tijdens de sessies teruggeven aan degene bij wie het hoort. Nieuwsgierig uit welk familiesysteem jij komt? Lees meer over <a href='../familieopstellingen.html'>familieopstellingen</a>."),
            ("p", f"<small>{OUD}</small>"),
         ]),
    dict(slug="inzicht-in-je-burn-out",
         titel="Krijg inzicht in de reden van je burn-out", onder="Klachten herkennen en begrijpen hoe het zover kwam",
         datum="29 juli 2023", foto="natuur-meer.jpg",
         seo_titel="Inzicht in de reden van je burn-out | Blog Liesbeth Postma",
         seo="Welke klachten horen bij stress en burn-out, wat is het verschil met een depressie en waarom inzicht het begin van herstel is.",
         intro="Bij stress of burn-out kun je last hebben van uiteenlopende klachten. Inzicht krijgen in hoe het zover is gekomen, is het begin van herstel.",
         blokken=[
            ("h2", "Klachten bij stress of burn-out"),
            ("ul", ["Moeheid en slaapproblemen", "Piekeren, concentratieproblemen, vergeetachtigheid", "Emotionele labiliteit en prikkelbaarheid", "Niet tegen drukte of herrie kunnen, onrust", "Lichamelijke klachten zoals hoofdpijn, maagpijn of spierpijn", "Somberheid en geen zin meer in leuke dingen"]),
            ("p", "Ook kun je je machteloos voelen of het gevoel hebben de controle te verliezen. Bij een burn-out duren de klachten langer dan zes maanden. Je bent uitgeput en je batterij laadt ondanks leefstijladviezen niet meer op."),
            ("h2", "Is het een depressie?"),
            ("p", "De klachten lijken soms op elkaar. Bij een burn-out staat vermoeidheid op de voorgrond, bij een depressie een somber gevoel. Beleef je ook geen plezier meer aan alledaagse dingen, dan zou het een depressie kunnen zijn. Burn-out is geen officiële diagnose, wat ertoe kan leiden dat je je niet serieus genomen voelt."),
            ("h2", "Inzicht"),
            ("p", "Je zit thuis en weet het niet meer. Inzicht krijgen in hoe het zover is gekomen, is het begin. Wat lag eraan ten grondslag? Waardoor hield je je zo lang staande? Vervolgens: voelen, ervaren en bewust worden, zodat er verandering kan plaatsvinden."),
            ("quote", "Ik was vooral bezig met pleasegedrag. In therapie voelde ik waar dat vandaan kwam."),
            ("p", "Wil jij ook inzicht in wat er onder je burn-out ligt? Ben je klaar met alleen praten en analyseren? Lees meer over <a href='../mentaal-vastlopen.html'>mentaal vastlopen</a>."),
            ("p", f"<small>{OUD}</small>"),
         ]),
    dict(slug="vroegkinderlijk-trauma",
         titel="Hoe vroegkinderlijk trauma invloed heeft op je toekomst", onder="Triggers, overlevingsmechanismen en de moed om te voelen",
         datum="15 mei 2023", foto="natuur-wilg.jpg",
         seo_titel="Hoe vroegkinderlijk trauma invloed heeft op je toekomst | Blog",
         seo="Over triggers, overtuigingen als ‘ik ben niet goed genoeg’ en hoe trauma van generatie op generatie overgaat tot iemand het durft te voelen.",
         intro="‘Wat ik ook doe, ik doe het nooit goed genoeg.’ Zulke gedachten zijn vaak triggers als gevolg van trauma dat je diep hebt weggestopt.",
         blokken=[
            ("quote", "Trauma, je bent gek als je het niet hebt."),
            ("p", "Dit is de titel van het boek van Christine Pannebakker en Robert Bridgeman. ‘Wat bedoelde hij nu weer?’ ‘Wat ik ook doe, ik doe het nooit goed genoeg.’ ‘Een ander weet veel meer dan ik.’ Het zijn voorbeelden van triggers als gevolg van trauma: iets wat je diep hebt weggestopt om het niet meer te hoeven voelen. Toch komt het omhoog, vaak in relaties."),
            ("p", "Trauma gaat over van generatie op generatie. Je bent je er niet van bewust totdat je je bewust wordt van wie je bent. Als jij de moed hebt om te durven voelen, kun je het stoppen voor je kinderen en de generaties daarna."),
            ("p", "Zelf kreeg ik steeds meer inzicht dat een groot deel van mijn problemen voortkwam uit trauma. Om dat op te lossen moest ik door heel wat lagen van emoties heen. Niet de gemakkelijkste weg, maar wel de enige om te begrijpen waarom ik steeds op dezelfde problemen stuitte."),
            ("h2", "Vroegkinderlijk trauma"),
            ("p", "Als je zelfinzicht krijgt, voel je wat een ander met zijn gedrag met jou doet. Die ander is een spiegel. In die spiegel kijken doet pijn: het is pijn van vroeger, toen je nog te jong was om het te voelen. Je ontwikkelde een overlevingsmechanisme dat je nu niet meer dient. We zijn geneigd de ander de schuld te geven om bij de pijn weg te blijven, maar daarmee blijf je vastzitten."),
            ("p", "Wil jij je bewust worden van je overlevingsmechanismen? Lees meer over <a href='../werkwijze/innerlijk-kindwerk.html'>innerlijk-kindwerk</a>."),
            ("p", f"<small>{OUD}</small>"),
         ]),
]


# ---------- reviews (overgenomen van magnolia-elst.nl) ----------
REVIEWS = [
    ("Lisa, Arnhem", "Een persoonsgerichte en brede aanpak",
     "Na mijn burn-out wist ik niet goed welke weg ik in moest slaan. Samen met Liesbeth heb ik hier een duidelijke invulling aan kunnen geven. Met een persoonsgerichte en brede aanpak heeft Liesbeth mij tot inzicht gebracht. Als therapeut is Liesbeth liefdevol maar ook duidelijk: ze kijkt naar wat je nodig hebt en gaat daar samen met jou mee aan de slag."),
    ("Wikke, Zevenaar", "Liefdevolle stappen voor mezelf",
     "Al jaren leefde ik in een soort sneltrein zonder echt te luisteren naar mijn gevoel en te investeren in mezelf. Ik zocht iemand die mij begreep. Liesbeth kon met empathie naar mij luisteren, waardoor ik mij op mijn gemak voelde. Door haar therapie heb ik liefdevolle stappen voor mezelf kunnen zetten en had ik de moed en energie om op mijn gevoel af te gaan."),
    ("Marianne, Arnhem", "Puzzelstukjes vielen op hun plek",
     "Ik vond het een leerzame en verhelderende periode. De puzzelstukjes vielen op hun plek. Ik voelde me op mijn gemak en prettig bij Liesbeth, daardoor hebben we snel stappen kunnen zetten. De oefeningen zijn praktisch en hebben echt geholpen om tot inzichten te komen en om emoties te doorleven en te accepteren. Niet altijd even fijn, maar wel nodig om verder te komen. En dat is gelukt."),
    ("Truus, Gennep", "Ik voel mij meer waard",
     "Omdat ik moeite had met loslaten ben ik bij Liesbeth terechtgekomen. Verschillende thema's kwamen aan de orde door haar tactische doorvragen. Wat ik tijdens de sessies zag, ben ik op doek gaan schilderen om het nog dieper te verwerken. Nog nooit zo mooi huiswerk gehad. Na vier sessies voel ik me meer waard, mag ik er zijn en durf ik gemakkelijker dingen te ondernemen en veranderingen aan te gaan."),
]

# ---------- juridische teksten (overgenomen van magnolia-elst.nl, naam en adres geactualiseerd) ----------
VOORWAARDEN = [
    ("p", f"<strong>{NAAM}</strong> – {TITEL}<br>{ADRES}<br>KvK {KVK}"),
    ("p", "Algemene bepalingen behorend bij de behandelingsovereenkomst tussen de therapeut (Liesbeth Postma) en de cliënt / de cliënten."),
    ("h2", "Behandelingsovereenkomst"),
    ("p", "Indien de cliënt na het eerste kennismakingsgesprek een nieuwe datum heeft afgesproken voor een vervolggesprek, is er sprake van een behandelingsovereenkomst. Deze behandelingsovereenkomst wordt op schrift vastgelegd."),
    ("p", "De behandelingsovereenkomst is tweeledig:"),
    ("ul", ["De therapeut en de cliënt gaan een relatie met elkaar aan voor een bepaalde periode in de verhouding therapeut – cliënt.",
            "De behandeling heeft betrekking op de door de cliënt aangedragen hulpvraag en behandeldoelen. Deze kunnen lopende het traject worden bijgesteld of gespecificeerd."]),
    ("h2", "Beëindiging van de overeenkomst"),
    ("p", "De overeenkomst kan op de volgende manieren of door de volgende omstandigheden worden beëindigd:"),
    ("ul", ["Therapeut en cliënt bepalen in gezamenlijk overleg dat er geen sessies meer nodig zijn.",
            "De cliënt geeft mondeling, schriftelijk of via e-mail aan geen sessies meer te willen afspreken.",
            "De therapeut geeft mondeling, schriftelijk of via e-mail aan geen sessies meer te zullen geven.",
            "De cliënt houdt zich herhaaldelijk niet aan de algemene bepalingen uit deze behandelingsovereenkomst of aan afspraken die gedurende de sessies zijn gemaakt tussen cliënt en therapeut.",
            "De therapeut is van mening dat zij, gezien de problematiek van de cliënt en haar eigen competentie, niet bekwaam is om de cliënt te begeleiden. Dit is in ieder geval aan de orde als de problematiek direct verband houdt met contra-indicaties."]),
    ("p", "De overeenkomst eindigt van rechtswege indien er geen sessie is afgesproken voor een termijn van langer dan drie maanden na de laatst gehouden sessie, tenzij uitdrukkelijk anders afgesproken tussen therapeut en cliënt."),
    ("h2", "Tarief en betaling"),
    ("p", "Bij het aangaan van de overeenkomst wordt voor een te houden sessie een bedrag per sessie afgesproken. Dit is opgenomen in de behandelovereenkomst. De cliënt ontvangt een factuur en dient deze binnen 14 dagen over te maken."),
    ("h2", "Afzeggen van een afspraak"),
    ("p", "Bij verhindering dient een afgesproken sessie 48 uur (twee werkdagen) van tevoren te worden afgemeld. De therapeut brengt de kosten voor een gemiste sessie in rekening indien de cliënt zich niet tijdig heeft afgemeld, ongeacht de reden van afmelding. Dit geldt ook als de cliënt, om welke reden dan ook, niet komt op de afgesproken dag en tijd."),
    ("h2", "Dossier"),
    ("p", "De therapeut houdt een dossier bij met aantekeningen van de gehouden sessies en andere relevante documenten, dat op verzoek door de cliënt kan worden ingezien. Het dossier (of een deel daarvan) wordt dan gekopieerd; dit is kosteloos, met uitzondering van buitensporige verzoeken. Het dossier wordt conform de wettelijke bewaartermijn 20 jaar bewaard. Verder bestaat er inzagerecht voor nabestaanden. Het zwaartepunt ligt op het samen beslissen over de behandeling (zie PR 520 Hantering dossier voor de RBCZ-sectoren)."),
    ("h2", "Geheimhouding"),
    ("p", "De therapeut houdt zich aan haar geheimhoudingsplicht. Gegevens van de cliënt worden alleen met diens uitdrukkelijke goedkeuring aan derden (artsen en andere therapeuten) overhandigd of medegedeeld."),
    ("p", "Indien de cliënt, diens huisarts of een andere behandelaar een schriftelijke rapportage verlangt van het behandelingstraject, wordt hiervoor een factuur gestuurd aan de cliënt. Deze factuur behelst maximaal een uur arbeid tegen het in de overeenkomst afgesproken uurtarief."),
    ("h2", "Beroepsorganisatie en klachten"),
    ("p", "De therapeut is aangesloten bij de beroepsorganisatie Nederlandse Beroepsvereniging voor Hypnotherapeuten (NBVH). De regels van deze beroepsorganisatie zijn op de therapeut van toepassing. De cliënt kan zich met klachten over de therapeut bij deze beroepsorganisatie melden. De therapeut is daarnaast geregistreerd in het HBO Register Beroepsbeoefenaren Complementaire Zorg (RBCZ)."),
    ("h2", "In de praktijk"),
    ("p", "De cliënt gedraagt zich als een gast en houdt zich aan de regels van de gastvrouw (de therapeut). Er wordt tijdens een sessie niet gerookt en geen alcohol gedronken. De kosten van vernieling van eigendommen van de therapeut door de cliënt worden op de cliënt verhaald. Van iedere vorm van mishandeling van de therapeut zal te allen tijde aangifte bij de politie worden gedaan."),
    ("h2", "Aansprakelijkheid"),
    ("p", "Liesbeth Postma is niet aansprakelijk voor eventuele nadelige gevolgen die zijn ontstaan doordat de cliënt onjuiste of onvolledige informatie heeft verstrekt, dan wel doordat de cliënt voor hem/haar bekende en beschikbare informatie uit medische dossiers van arts, specialist of andere behandelaar niet heeft verstrekt."),
    ("p", f"De cliënt heeft de privacyverklaring gelezen die vermeld staat op de website {WEBSITE} en stemt in met deze privacyverklaring."),
    ("p", f"Liesbeth Postma is niet aansprakelijk voor schade die is ontstaan aan eigendommen van de cliënt door parkeren op of het betreden van het terrein aan de {ADRES.replace(', ', ' te ')}, noch voor andere schade ontstaan door het betreden van de praktijk en het gebruik van het toilet."),
]

PRIVACY = [
    ("h2", "Jouw privacy"),
    ("p", "Voor een goede behandeling is het noodzakelijk dat ik, als jouw behandelend therapeut, een dossier aanleg. Dit is ook een wettelijke plicht, opgelegd door de WGBO. Jouw dossier bevat aantekeningen over je gezondheidstoestand en gegevens over de uitgevoerde onderzoeken en behandelingen."),
    ("p", "Ook worden in het dossier gegevens opgenomen die voor jouw behandeling noodzakelijk zijn en die ik, na jouw expliciete toestemming, heb opgevraagd bij een andere zorgverlener, bijvoorbeeld de huisarts."),
    ("p", "Ik doe mijn best om je privacy te waarborgen. Dit betekent onder meer dat ik:"),
    ("ul", ["zorgvuldig omga met je persoonlijke en medische gegevens;",
            "ervoor zorg dat onbevoegden geen toegang hebben tot jouw gegevens."]),
    ("p", "Als jouw behandelend therapeut heb ik als enige toegang tot de gegevens in je dossier. Ik heb een wettelijke geheimhoudingsplicht (beroepsgeheim)."),
    ("h2", "Waarvoor je gegevens nog meer gebruikt kunnen worden"),
    ("ul", ["Om andere zorgverleners te informeren, bijvoorbeeld als de therapie is afgerond of bij een verwijzing naar een andere behandelaar. Dit gebeurt alleen met jouw expliciete toestemming.",
            "Voor waarneming tijdens mijn afwezigheid.",
            "Voor geanonimiseerd gebruik tijdens intercollegiale toetsing.",
            "Een klein deel van de gegevens uit je dossier wordt gebruikt voor de financiële administratie, zodat ik of mijn administrateur een factuur kan opstellen."]),
    ("p", "Als ik om een andere reden gebruik wil maken van jouw gegevens, informeer ik je eerst en vraag ik expliciet je toestemming."),
    ("p", "De gegevens in het cliëntendossier blijven, zoals de Wet op de geneeskundige behandelingsovereenkomst vereist, 20 jaar bewaard."),
    ("h2", "Privacy op de zorgnota"),
    ("p", "Op de zorgnota die je ontvangt staan de gegevens die door de zorgverzekeraar gevraagd worden, zodat je deze nota kunt declareren bij jouw zorgverzekeraar:"),
    ("ul", ["je naam, adres en woonplaats;", "je geboortedatum;", "de datum van de behandeling;",
            "een korte omschrijving van de behandeling, zoals 'behandeling hypnotherapie' of 'psychosociaal consult';",
            "de kosten van het consult."]),
    ("h2", "Vragen"),
    ("p", f"Vragen over privacy? Mail naar <a href='mailto:{MAIL}'>{MAIL}</a>."),
]
