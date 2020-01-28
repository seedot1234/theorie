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
Vervolgens krijgt u instructies te zien die u verder door het programma helpen. 

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