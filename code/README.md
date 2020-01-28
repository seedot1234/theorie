# code 

In deze map staat alle geschreven code. De code is verdeeld onder twee mappen:
* algorithms: hierin staan de algoritmen die geschreven zijn voor het oplossen van de RailNL case.
Deze algoritmen zijn:
  * random.py: een algoritme dat een random oplossing genereert binnen de constraints van het probleem.
  * shortest.py: greedy algoritme dat zich in het greedy keuzeproces baseert op de korste ongebruikte connectie mogelijk.
  * unused.py: greedy algortime dat zich in het greedy keuzeproces baseert op ongebruikte connecties boven al eerder gebruikte connecties.
  * greedy_lookahead.py: een greedy algoritme dat twee 'kinderen'/stappen diep vooruit kijkt. Het algoritme baseert zich op de K-score.
  * hill.py: hillclimber algoritme dat een oplossing van een van de hierboven genoemde algoritmen als input krijgt. Van deze oplossing kiest de hillclimber per iteratie een random route. Bij die random route wordt een random gekozen mutatie uitgevoerd. De score van de nieuwe en de oude oplossing worden vergeleken. De mutatie wordt geaccepteerd als de K-score is verbeterd. De vier mogelijke mutaties zijn: verwijder de eerste connectie, verwijder de laatste connectie, voeg een connectie toe aan het begin en voeg een connectie toe aan het eind.
  * annealing.py: simulated annealing algoritme dat zich baseert op de hierboven beschreven hillclimber. Het koelingsschema is exponentieel en de begintemperatuur is 35.
* classes: hierin staat de datastructuur uitgeschreven. De verschillende onderdelen van de RailNL case worden opgeslagen als objecten.
Deze onderdelen zijn:
  * station.py: de Station klasse. Hierin worden de namen en locaties van stations opgeslagen. Ook houdt het bij welke stations verbonden zijn met een gegeven station.
  * connection.py: de Connection klasse slaat alle connecties op zoals deze gegeven zijn in de csv-bestanden van de case. Het houdt bij van welk naar welk station een connectie loopt en hoe lang een trein over dat stuk spoor doet.
  * route.py: een Route bestaat uit een opeenvolging van connecties en dus ook een opeenvolging van stations. Meerdere routes samen vormen een oplossing.
  * solution.py: Oplossingen bestaan uit meerdere routes. Van een oplossing kan een K-score en alle daarbij horende elementen (T, MIN, p) berekend worden.