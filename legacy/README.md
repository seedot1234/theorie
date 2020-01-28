# Legacy
De map Legacy bevat een aantal algoritmes die werken, maar die wij niet gebruiken in het eindproduct. Na al het harde werken doet het ons te veel pijn om de algoritmes weg te gooien, daarom staan de algoritmes bewaard in dit mapje.
* Railhead en longest zijn voorbeelden van greedy algoritmen waarbij we andere keuze-proces regels hebben toegepast.
* In random_k wordt er oplossing gegenereerd vanaf een bepaalde k score (in plaats van vanaf een bepaald p-niveau).
* De greedy_lookahead is gebruikt om de 'juiste' diepte te vinden voor de uiteindelijke greedy lookahead: te oppervlakkig en de scores zijn te laag, maar te lang en de runtime is te lang of de scores verslechteren.
* Bound is gebruikt om de statespace en upper en lower-bound van de doelfunctie te berekenen. 
* Improved_random_p heeft dezelfde werking en functionaliteit als de originele random.py functie uit het mapje /code/. Echter, bij deze verbeterde versie is de structuur van het algoritme aanzienlijk overzichtelijker geworden. Er is met veel verschillende functies gewerkt, alles binnen een Class Object met een run methode. Vanwege tijdsgebrek is deze betere versie niet compitabel met de user-interface, hoewel hij wel helemaal werkt. Vandaar dat, ondanks dat deze versie van het algoritme mooier en 'beter' is, hij in de legacy map staat.
