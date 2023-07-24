from stock import daily_transactions
from dates import get_date, week_date


def daily_revenue():
    """Print the program's date revenue."""
    transactions = daily_transactions(get_date())
    total_revenue = 0
    for row in transactions[1:]:
        product_revenue = int(row['sale_quantity']) * float(row['sale_price'])
        total_revenue += product_revenue
    result = print(
        f'The total revenue of {get_date()} is: '
        f'€ {total_revenue:.2f}.')
    return result


def weekly_revenue(week, year):
    """Return the weekly revenue from a given weeknumber and year."""
    week_revenue = []
    for date in week_date(week, year):
        transactions = daily_transactions(date)
        day_revenue = 0
        for row in transactions[1:]:
            product_revenue = int(row['sale_quantity']) * \
                float(row['sale_price'])
            day_revenue += product_revenue
        week_revenue.append(round(day_revenue, 2))
    return week_revenue


def daily_profit():
    """Print the programs's date profit."""
    transactions = daily_transactions(get_date())
    total_profit = 0
    for row in transactions[1:]:
        product_profit = int(row['sale_quantity']) * \
            (float(row['sale_price']) - float(row['purchase_price']))
        total_profit += product_profit
    result = print(
        f'The total profit of {get_date()} is: '
        f'€ {total_profit:.2f}.')
    return result


def weekly_profit(week, year):
    """Return the weekly profit from a given weeknumber and year."""
    week_profit = []
    for date in week_date(week, year):
        transactions = daily_transactions(date)
        day_profit = 0
        for row in transactions[1:]:
            product_profit = int(row['sale_quantity']) * \
                (float(row['sale_price']) - float(row['purchase_price']))
            day_profit += product_profit
        week_profit.append(round(day_profit, 2))
    return week_profit
