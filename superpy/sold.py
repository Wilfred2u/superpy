import csv
from random import randint
from build_table import field_names
from dates import get_date, string_date_today
from products import show_all_products

product_list = show_all_products()


def create_id():
    """Generate a unique id for every row in the csv-files."""
    id = randint(1000, 9999)
    return id


def calc_stock_quantity(row, quantity):
    stock_quantity = int(row['stock_quantity']) - quantity
    return str(stock_quantity)


def message_no_todays_date():
    print(f'\nThe program\'s date ({get_date()}) is not today\'s date ({string_date_today()}), so you can\'t sell anything.'
          f'\nPlease type "date 0" to set the program\'s date to today\'s date.')


def message_no_match(product_name):
    print(
        f'\n"{product_name.title()}" has the wrong spelling or is not in stock.'
        f'\nPlease check the stock to see what you can sell.')


def message_no_sale(quantity, row):
    print(f'\nYou try to tell {quantity} {row["unit"]}s of {row["product_name"]}, '
          f'while there are only {row["stock_quantity"]} in stock. '
          f'So that\'s not possible.')


def sell_product(product_name, sale_price, sale_quantity):
    """Buy a product and put the transaction in transactions.csv"""
    if str(string_date_today()) != get_date():
        return message_no_todays_date()

    with open('transactions.csv', 'r') as csv_file:
        reader = list(csv.DictReader(csv_file, fieldnames=field_names))
        product = {}

        match = [row for row in reader if row['product_name'] ==
                 product_name]
        if match == []:
            return message_no_match(product_name)

        rows_with_product = [
            row for row in reader if product_name == row['product_name']]
        row = rows_with_product[-1]

        if sale_quantity > int(row['stock_quantity']):
            return message_no_sale(sale_quantity, row)

        product['id'] = create_id()
        product['product_group'] = row['product_group']
        product['product_name'] = product_name
        product['purchase_price'] = row['purchase_price']
        product['purchase_date'] = row['purchase_date']
        product['purchase_quantity'] = str(0)
        product['sale_price'] = sale_price
        product['sale_date'] = get_date()
        product['sale_quantity'] = sale_quantity
        product['expiration_date'] = row['expiration_date']
        product['stock_quantity'] = calc_stock_quantity(
            row, sale_quantity)
        product['unit'] = row['unit']
    sold_product = [product]
    with open('transactions.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writerows(sold_product)
        csv_file.close()
        print('Product sold.')
