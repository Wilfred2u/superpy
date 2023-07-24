import csv
import json
import difflib
from pathlib import Path
from random import randint
from build_table import field_names
from dates import get_expiration_date, string_date_today, get_date
from products import show_all_products

product_list = show_all_products()


def create_id():
    """Generate a unique id for every row in the csv-files."""
    id = randint(1000, 9999)
    return id


def get_attributes(product_name):
    """Get some standard product values."""
    path = Path('products.json')
    contents = path.read_text()
    products = json.loads(contents)

    product_attributes = []
    for row in products:
        if product_name == row['product_name']:
            product_attributes.append(row['product_group'])
            product_attributes.append(
                get_expiration_date(int(row['best_before_days'])))
            product_attributes.append(row['unit'])
            return product_attributes


def calc_stock_quantity(row, quantity):
    stock_quantity = int(row['stock_quantity']) + quantity
    return str(stock_quantity)


def message_no_todays_date():
    print(f'The program\'s date is not today\'s date, so you can\'t purchase anything.'
          f'\nPlease set the program\'s date to today\'s date.')


def message_no_match():
    print(f'Sorry, the product you want to purchase is not known. '
          f'Type "report products" to find the product you want to purchase.')


def handle_mismatch(product_name, purchase_price, purchase_quantity):
    matches = difflib.get_close_matches(
        product_name, product_list, cutoff=.75)
    print(
        f'"{product_name.title()}" does not exist.')

    if len(matches) == 0:
        return message_no_match()
    elif len(matches) == 1:
        match = input(f'Do you mean {" or ".join(matches)}? (yes/no) ')
        if match.lower() == "yes":
            match = ''.join(matches)
            purchase_product(match, purchase_price, purchase_quantity)
        elif match == "no":
            return message_no_match()
    elif len(matches) > 1:
        match = input(f'Do you mean {" or ".join(matches)}? ')
        purchase_product(match, purchase_price, purchase_quantity)


def purchase_product(product_name, purchase_price, purchase_quantity):
    """Buy a product and put it in transactions.csv"""
    if str(string_date_today()) != get_date():
        return message_no_todays_date()

    with open('transactions.csv', 'r') as csv_file:
        reader = list(csv.DictReader(csv_file, fieldnames=field_names))
        product = {}

    rows_with_product = [
        row for row in reader if product_name == row['product_name']]
    if rows_with_product:
        row = rows_with_product[-1]
    else:
        row = []

    match = [product for product in show_all_products() if product ==
             product_name]
    if match == []:
        handle_mismatch(product_name, purchase_price, purchase_quantity)
    else:
        product['id'] = create_id()
        product['product_group'] = get_attributes(product_name)[0]
        product['product_name'] = product_name
        product['purchase_price'] = purchase_price
        product['purchase_date'] = string_date_today()
        product['purchase_quantity'] = purchase_quantity
        product['sale_price'] = 0
        product['sale_date'] = 0
        product['sale_quantity'] = 0
        product['expiration_date'] = get_attributes(product_name)[1]

        if row:
            product['stock_quantity'] = calc_stock_quantity(
                row, purchase_quantity)
        else:
            product['stock_quantity'] = purchase_quantity
        product['unit'] = get_attributes(product_name)[2]
        purchased_product = [product]

        with open('transactions.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writerows(purchased_product)
            csv_file.close()
        print('Product purchased.')
