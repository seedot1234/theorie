# RailNL 
De NS heeft hulp nodig bij het maken van een nieuwe lijnvoering. De lijnvoering bestaat uit de trajecten waar de treinen gedurende de dag overheen rijden. Een traject is een route van sporen en stations waarover de treinen rijden. 
Voor Noord- en Zuid-Holland mogen we gebruik maken van maximaal zeven trajecten binnen een tijdsframe van twee uur. Daarbij moeten alle verbindingen tussen de stations bereden worden. 
Voor heel Nederland mogen we maximaal twintig trajecten gebruiken binnen een tijdsframe van drie uur. Voor Nederland hoeven niet alle verbindingen bereden worden, maar moet de kwaliteit van de lijnvoering zo hoog mogelijk zijn. 
De kwaliteit van de lijnvoering wordt berekend aan de hand van de volgende formule: 
**K = p * 10000 - (T * 100 + Min)**
- **K**: de kwaliteit van de lijnvoering 
- **p**: de fractie van de bereden verbindingen
- **T**: het aantal trajecten 
- **Min**: het aantal minuten van alle trajecten samen

Dit programma dient ervoor om het bovenstaande probleem op te lossen. Via verschillende algortimen is er geprobeerd om de K-score zo hoog mogelijk te krijgen. Meer informatie over de werking van deze algoritmen kan gevonden worden in de README in de /code/ map.

## Aan de slag
### Vereisten
Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle packages die nodig zijn om de code succesvol te runnen. De packages zijn gemakkelijk te installeren via pip door de volgende instructies te volgen:

```
pip install -r requirements.txt
```
### Gebruik
De code kan worden gerund door het volgende aan te roepen:
```
python main.py
```
Vervolgens wordt u door het volgede keuzemenu geleid:
* Over welke probleemgrootte wilt u een algortime runnen?
  * Holland: een probleem met 21 stations en 28 connecties.
  * Nederland: een probleem met 61 stations en 89 connecties.
* Welk algoritme wilt u gebruiken bij het maken van trajecten in het probleem?
  * Random: random algoritme. Kiest een random beginstation kiest vanuit daar random connecties.
  * Unused: greedy algoritme. Kiest een random beginstation en kiest vanuit daar een random ongebruikte connectie.
  * Shortest: greedy algortime. Kiest een random beginstation en kiest vanuit daar de kortste ongebruikte connectie.
  * Greedy lookahead: greedy algoritme dat twee diep vooruit kijkt. Baseert zich op de K score die behaald wordt bij ieder mogelijk kind twee diep vanaf het huidige station.
* Hoe vaak wilt u het algoritme runnen?
* Keuzes over statistieken:
  * U krijgt altijd algemene statistieken te zien over uw algoritme
  * Wanneer u het algortime 1x runt, kunt u ervoor kiezen om een visualisatie te laten maken van de oplossing
  * Wanneer u het algoritme meerdere keren runt kunt u ervoor kiezen om een boxplot en/of een histrogram te laten maken van de oplossing.
  
Wanneer u het algortime 1x runt, krijgt u ook nog de optie om een interatief algortime af te spelen over de gegenereerde oplossing:
* Zo ja, welk iteratief algortime wilt u gebruiken?
  * Hillclimber: een hillclimber algoritme dat uit de oplossing random één route kiest en hier dan één van de vier mogelijke mutaties op doet. Deze nieuwe staat wordt geaccepteerd indien de K-score is verbeterd.
  * Simulated Annealing: doet dezelfde mutaties als de hillclimber, maar heeft een acceptatiekans die varieert gedurende het iteratieproces.
* Hoeveel iteraties wilt u het iteratief algoritme laten runnen?
Vervolgens krijgt u dezelfde statistieken als eerder te zien, maar dan na het runnen van de hillclimber of simulated annealing.

### Structuur
De onderstaande lijst beschrijft de belangrijkste mappen en files in het proejct, en waar u ze kan vinden:
- **/code**: bevat vrijwel alle code van dit project
    - **/code/algorithms**: bevat de code voor de algoritmes
    - **/code/classes**: bevat de benodigde classes voor deze case
    - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de databestanden met de stations en diens connecties voor Holland en Nederland
- **/interface**: bevat de code om een user interface te creëren
- **/legacy**: bevat de algoritmes die niet meer gebruikt worden voor de case, maar die wij niet willen verwijderen


## Auteurs
- Susan van den Broek
- Sarah-Jane van Els
- Linza Hitijahubessy
