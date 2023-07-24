import csv
from datetime import datetime
from build_table import make_table, field_names, stock_index, transactions_index
from dates import get_date, date_today


def daily_transactions(date):
    """Retourneert alle transacties VAN DE PROGRAMMA DATUM.
       Return the program's date transactions."""
    with open('transactions.csv', 'r') as csv_file:
        reader = list(csv.DictReader(csv_file, fieldnames=field_names))
        transactions = []
        for row in reader:
            rsd = row['sale_date']
            rpd = row['purchase_date']
            if rsd == 'sale_date':
                transactions.append(row)
            if rsd == '0':
                if rpd == date:
                    transactions.append(row)
            if rsd != 'sale_date' and rsd != '0':
                if rsd == date:
                    transactions.append(row)
        return transactions


def get_transactions_until():
    """Retourneert alle transacties TOT EN MET DE PROGRAMMA DATUM."""
    with open('transactions.csv', 'r') as csv_file:
        reader = list(csv.DictReader(csv_file, fieldnames=field_names))
        transactions = []
        for row in reader:
            rsd = row['sale_date']
            rpd = row['purchase_date']
            if rsd == 'sale_date':
                transactions.append(row)
            if rsd == '0':
                if rpd <= get_date():
                    transactions.append(row)
            if rsd != 'sale_date' and rsd != '0':
                if rsd <= get_date():
                    transactions.append(row)
        return transactions


def stock():
    """Return the program's date stock."""
    transactions = get_transactions_until()
    # Find the indices of the last occurrences of the product names:
    a = [row['product_name'] for row in transactions]
    b = a[::-1]
    lst = [(len(a) - b.index(i) - 1) for i in set(a)]
    sorted_lst = sorted(lst)

    current_stock = [
        row for row in transactions if transactions.index(row) in sorted_lst]
    return current_stock


def show_transactions_on_date():
    """Print a table with the transactions per product x days ago."""
    make_table(daily_transactions(get_date()), transactions_index)


def daily_stock():
    """Print a table with a stock from a given date."""
    make_table(stock(), stock_index)


def message_expired_products(row, date):
    if (date_today() - date).days == 1:
        days = 'day'
    else:
        days = 'days'
    print(f"{row['stock_quantity']} {row['unit']}s of {row['product_name']} "
          f"have been expired for {(date_today() - date).days} {days}.")


def show_expired_products():
    number_expired_products = 0
    for row in stock()[1:]:
        exp_date = datetime.strptime(row['expiration_date'], '%Y-%m-%d')
        if date_today() > exp_date and int(row['stock_quantity']) > 0:
            number_expired_products += 1
            message_expired_products(row, exp_date)
    if number_expired_products == 0:
        print("None of the products in stock are expired.")
