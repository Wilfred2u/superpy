# Gebruikershandleiding

## Algemeen
Deze handleiding is voor personen die werkzaam zijn in een supermarkt. Wat functionaliteit betreft gaat deze handleiding o.a. over het in- en afboeken van producten, en het weergeven van de omzet en winst. Voor een uitgebreidere uitleg zie onder Functionaliteiten.


## Vereisten
	- argparse (versienummer 1.1)
	- csv (versienummer 1.0)
	- json (versienummer 2.0.9)
	- matplot (versienummer 3.7.1)
	- datetime (geen versienummer)
	- difflib (geen versienummer)
	- math (geen versienummer)
	- pathlib (geen versienummer)
	- random (geen versienummer)


## Functionaliteiten

### date
Beschrijving:
Stelt een nieuwe datum in als de werkdatum. Dit kan op drie manieren:
- door een datum in te voeren, in yyyy-mm-dd formaat;
- door één van de woorden "today", "yesterday", of "tomorrow" in te voeren;
- door een getal in te voeren dat het aantal dagen geleden aangeeft, bijvoorbeeld 0 (vandaag), 1 (gisteren), 10 (tien dagen geleden), -1 (morgen)
Om te kunnen in- of verkopen moet de datum van vandaag de werkdatum zijn. 
Verplicht argument: date_change. Geen optionele argumenten.

Gebruik: main.py date [-h] date_change

Opties:
  -h, --help   show this help message and exit

Voorbeelden:
1. main.py date 2023-07-24
   > The working date has been changed to 2023-07-24.
2. main.py date yesterday
   > The working date has been changed to 2023-07-23.
3. main.py date 4
   > The working date has been changed to 2023-07-20.


### purchase
Beschrijving:
Koopt een product in. De inkooptransactie wordt toegevoegd in de database (transactions.csv).
Verplichte argumenten: product_name, purchase_price en purchase_quantity. Geen optionele argumenten.
Foutafhandeling: De productnaam moet voorkomen in de lijst met producten. Onbekende productnamen worden afgehandeld op basis van overeenkomstigheid.

Gebruik: main.py purchase [-h] -n PRODUCT_NAME -p PURCHASE_PRICE -q PURCHASE_QUANTITY

Opties:
  -h, --help            					show this help message and exit
  -n PRODUCT_NAME, --product_name PRODUCT_NAME			Enter the name of the product, e.g. "tagliatelle".
  -p PURCHASE_PRICE, --purchase_price PURCHASE_PRICE		Enter the purchase price of the product, e.g. "1.22".
  -q PURCHASE_QUANTITY, --purchase_quantity PURCHASE_QUANTITY	Enter how many products you have purchased, e.g. "25".
                        
Voorbeelden:
1. main.py purchase --product_name meatballs --purchase_price 0.74 --purchase_quantity 40
   > Product purchased.
2. main.py -n bier -p 0.59 -q 50
   > "Bier" does not exist.
   > Do you mean brie or beer? beer
   > Product purchased.

### sell
Beschrijving:
Verkoopt een product. De inkooptransactie wordt toegevoegd in de database (transactions.csv).
Verplichte argumenten: product_name, sale_price en sale_quantity. Geen optionele argumenten.
Foutafhandeling: De productnaam moet voorkomen in de database (transactions.csv). Onbekende productnamen stoppen de transactie.

Gebruik: main.py sell [-h] -n PRODUCT_NAME -p SALE_PRICE -q SALE_QUANTITY

Opties:
  -h, --help            				show this help message and exit
  -n PRODUCT_NAME, --product_name PRODUCT_NAME		Enter which product you have sold, e.g. "bananas".
  -p SALE_PRICE, --sale_price SALE_PRICE		Enter the sale price of the product, e.g. "2.35".
  -q SALE_QUANTITY, --sale_quantity SALE_QUANTITY	Enter how many products you have sold, e.g. "25".
                        
Voorbeelden:
1. main.py sell --product_name bell_pepper --sale_price 0.78 --sale_quantity 12
   > Product sold.
2. main.py sell -n pepper -p 1.19 -q 25
   > "Pepper" has the wrong spelling or is not in stock.
   > Please check the stock to see what you can sell.


### report
Beschrijving:
Genereert verschillende dingen:
- een lijst met alle beschikbare supermarktproducten;
- één of meerdere strings met de mededeling welke producten er eventueel over datum zijn, en hoeveel dagen;
- een tabel met de supermarktvoorraad van de werkdatum;
- een tabel met alle transacties van de werkdatum
- een string met de omzet van de werkdatum;
- een string met de winst van de werkdatum.
Verandert de werkdatum, dan verandert de report-output ook.
Verplichte argumenten: één van de volgende: products, expires, stock, transactions, revenue, profit. Geen optionele argumenten.

Gebruik: main.py report [-h] {products,expires,stock,transactions,revenue,profit}

Opties:
  -h, --help            					show this help message and exit
  {products,expires,stock,transactions,revenue,profit}		Choose which type of report you want to create.

Voorbeelden:
1. main.py report products
   > Een lijst met alle beschikbare producten.
2. main.py report expires
   > 10 packs of raspberries have been expired for 5 days.
3. main.py report stock
   > +======+===============+==============+================+============+=================+================+=======+
     |  Id  | Product Group | Product Name | Purchase Price | Sale Price | Expiration Date | Stock Quantity | Unit  |
     +======+===============+==============+================+============+=================+================+=======+
     | 5638 | vegetables    | bell_pepper  | €         1.00 | €     0.00 |   2023-07-31    |            100 | pack  |
     +------+---------------+--------------+----------------+------------+-----------------+----------------+-------+
     | 7981 | alcoholics    | beer         | €         6.49 | €     0.00 |   2023-12-18    |            100 | crate |
     +------+---------------+--------------+----------------+------------+-----------------+----------------+-------+
     | 9065 | rice          | long_grain   | €         2.71 | €     0.00 |   2024-10-14    |             40 | pack  |
     +------+---------------+--------------+----------------+------------+-----------------+----------------+-------+
     | 1460 | soup          | mushroomsoup | €         0.63 | €     0.00 |   2023-08-31    |             25 | pack  |
     +------+---------------+--------------+----------------+------------+-----------------+----------------+-------+
     | 5283 | drugstore     | tooth_paste  | €         0.49 | €     0.00 |   2024-07-18    |             80 | tube  |
     +======+===============+==============+================+============+=================+================+=======+
4. main.py report transactions
   > +==============+===============+===================+============+===============+=================+================+=======+
     | Product Name | Purchase Date | Purchase Quantity | Sale Date  | Sale Quantity | Expiration Date | Stock Quantity | Unit  |
     +==============+===============+===================+============+===============+=================+================+=======+
     | tooth_paste  |  2023-07-24   |                80 |          0 |             0 |   2024-07-18    |             80 | tube  |
     +--------------+---------------+-------------------+------------+---------------+-----------------+----------------+-------+
     | beer         |  2023-07-21   |                 0 | 2023-07-24 |            38 |   2023-12-18    |             62 | crate |
     +--------------+---------------+-------------------+------------+---------------+-----------------+----------------+-------+
     | tooth_paste  |  2023-07-24   |                 0 | 2023-07-24 |             6 |   2024-07-18    |             74 | tube  |
     +==============+===============+===================+============+===============+=================+================+=======+
5. main.py report revenue
   > The total revenue of 2023-07-24 is: € 592.36.
6. main.py report profit
   > The total profit of 2023-07-24 is: € 342.80.


### plot
Beschrijving:
Genereert een grafiek met de omzet, winst of beide, per opgegeven week.
Verplichte argumenten: één van de volgende: revenue, profit, both. Daarnaast year en week. Geen optionele argumenten.

Gebruik: main.py plot [-h] -y YEAR -w WEEK {revenue,profit,both}

Opties:
{revenue,profit,both}		Choose from which source you want to see a line graph of.
  -h, --help            	show this help message and exit
  -y YEAR, --year YEAR  	Enter the year for which you want to see the line graph, e.g. "2023".
  -w WEEK, --week WEEK  	Enter the number of the week for which you want to see the line graph, e.g. "27".

Voorbeelden:
1. main.py plot profit --year 2023 --week 29
2. main.py plot both -y 2023 -w 20