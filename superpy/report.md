Drie technische elementen in mijn implementatie.

 **1. Het csv-bestand zien als een soort blockchange, waarin alle transacties plaatsvinden.**
Naarmate ik vorderde met deze opdracht, veranderde ook mijn inzicht in hoe ik de data moest bijhouden. Ik heb gekozen voor één csv-bestand, waarin alles wordt af- en bijgeboekt. Zo kan je goed zien wat er met een product gebeurt, vanaf het moment van inkoop tot en met het afboeken van het laatste artikel. Het leek mij overzichtelijker (en makkelijker), dan het werken met twee aparte csv-bestanden.

**2.Het filteren van de data voor het outputten van een voorraadstand.**
Dit vond ik het moeilijkste aan de hele opdracht. De consequentie van alle transacties in één bestand zetten, is dat het best lastig wordt de actuele voorraadstand (of die van x dagen geleden) te laten zien, zeker als producten worden verkocht en je daardoor meerdere regels van hetzelfde product (met verschillende voorraadstanden) in het csv-bestand hebt staan.
Mijn oplossing was om de indexen te zoeken van de laatste keer dat elk product in het csv-bestand voorkwam, en deze in een for loop te zetten. Misschien is er een betere oplossing, maar dit werkt goed.

**3. Het automatisch meeschalen van de breedte van de kolommen met de breedste inputwaarde.**
Het is met mijn Superpy mogelijk om te zien wat de voorraadstand is, ook per dag. Type bijvoorbeeld: `python3 main.py report stock --date 2023-07-13` en de output is een tabel met de voorraad van 13 juli 2023. Elke kolom van de tabel schaalt mee met de inhoud. Zit er een product in de voorraad met een lange naam, bijv.  ‘semi-skimmed_milk', dan is de breedte van die kolom aangepast aan de lengte van het woord ‘semi-skimmed_milk'. Dit gebeurt met de functie `set_column_widths(cols, index)`.
Ook worden de tabelranden automatisch langer, door de functie `make_line(cols, index, dash)`.

