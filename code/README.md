# Code 

In deze map staat alle geschreven code. De code is verdeeld onder drie mappen:

### Algorithms
Hierin staan de algoritmen die geschreven zijn voor het oplossen van de RailNL case.
Deze algoritmen zijn:
  * **random.py**: een algoritme dat een random oplossing genereert binnen de constraints van het probleem.
  * **shortest.py**: greedy algoritme dat zich in het greedy keuzeproces baseert op de korste ongebruikte connectie mogelijk.
  * **unused.py**: greedy algortime dat zich in het greedy keuzeproces baseert op ongebruikte connecties boven al eerder gebruikte connecties.
  * **greedy_lookahead.py**: een greedy algoritme dat twee 'kinderen'/stappen diep vooruit kijkt. Het algoritme baseert zich op de K-score.
  * **hill.py**: hillclimber algoritme dat een oplossing van een van de hierboven genoemde algoritmen als input krijgt. Van deze oplossing kiest de hillclimber per iteratie een random route. Bij die random route wordt een random gekozen mutatie uitgevoerd. De score van de nieuwe en de oude oplossing worden vergeleken. De mutatie wordt geaccepteerd als de K-score is verbeterd. De vier mogelijke mutaties zijn: verwijder de eerste connectie, verwijder de laatste connectie, voeg een connectie toe aan het begin en voeg een connectie toe aan het eind.
  * **annealing.py**: simulated annealing algoritme dat zich baseert op de hierboven beschreven hillclimber. Het koelingsschema is exponentieel en de begintemperatuur is 35.
  De oplossingen die in de iterative algoritmen (hillclimber, simulated annealing) gebruikt worden, worden eerst gepreprocessed:
  * **trim.py**: deze recursieve functie wordt gebruikt om oplossingen die in de iteratieve algoritmen gaan op te schonen. De iteratieve algoritmen kunnen namelijk alleen aan het eind en het begin van een route aanpassingen doen. Trim.py lost dit probleem op door dubbele elkaar opvolgende stationparen te verwijderen. (van D-A-B-A-B-C wordt D-A-B-C gemaakt). Ook worden er hier routes zonder connecties erin verwijderd.

### Classes
Hierin staat de datastructuur uitgeschreven. De verschillende onderdelen van de RailNL case worden opgeslagen als objecten.
Deze onderdelen zijn:
  * **station.py**: de Station klasse. Hierin worden de namen en locaties van stations opgeslagen. Ook houdt het bij welke stations verbonden zijn met een gegeven station.
  * **connection.py**: de Connection klasse slaat alle connecties op zoals deze gegeven zijn in de csv-bestanden van de case. Het houdt bij van welk naar welk station een connectie loopt en hoe lang een trein over dat stuk spoor doet.
  * **route.py**: een Route bestaat uit een opeenvolging van connecties en dus ook een opeenvolging van stations. Meerdere routes samen vormen een oplossing.
  * **solution.py**: Oplossingen bestaan uit meerdere routes. Van een oplossing kan een K-score en alle daarbij horende elementen (T, MIN, p) berekend worden.
  Tenslotte vind je in classes ook de functies die de objecten initialiseren vanuit een csv file:
  * **load_data.py**: Deze functies zorgen ervoor dat er daadwerkelijk station en connection objecten aangemaakt worden aan de hand van data uit csv-files. Alle overige objecten zijn combinaties van (delen van) station en connection.

### Visualisation
Hierin staan de verschillende manieren van visualeren geschreven. De verschillende manieren zijn
* **descriptives.py**: hier staan drie functies. Descriptive schrijft resultaten naar een csv file zodat dat kan worden gebruikt in berekeningen. Boxplot maakt een boxplot van de opgegeven resultaten. Histogram maakt een histogram van de opgegeven resultaten.
* **style.py**: hierin worden verschillende javascript onderdelen aangepast. Dit wordt gebruikt in visualise om de gegenereerde kaart aan te passen. 
* **visualise.py**: in visualise staat een functie om een kaart te generen van Nederland. In de kaart staan alle stations aangegeven en daartussen worden de trajecten getekend. 
