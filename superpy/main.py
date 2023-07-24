# Imports
import argparse
import dates
import products
import stock
import purchased
import sold
import financial
import plots

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

welcome_to_superpy = "Welcome to Superpy. In this app, you are the supermarket manager. "\
    "You can purchase and sell products, and calculate revenues and profits."

parser = argparse.ArgumentParser(description=welcome_to_superpy)

subparser = parser.add_subparsers(dest='command')

date = subparser.add_parser('date',
                            help='Advance or set back today\'s date. Type date -h for more help.')
purchase = subparser.add_parser('purchase',
                                help='Purchase a product and put the transaction in a database. Type purchase -h for more help.')
sell = subparser.add_parser('sell',
                            help='Sell a product and put the transaction in a database. Type sell -h for more help.')
report = subparser.add_parser('report',
                              help='You can make four different reports and choose from two date indications. Type report -h for more help.')
plot = subparser.add_parser('plot',
                            help='plot a line graph of revenue or profit, by week')


date.add_argument('date_change', type=str,
                  help='Set a new date as the working date by:'
                  ' a entering a date in yyyy-mm-dd format,'
                  ' b entering a the words "today", "yesterday", or "tomorrow"'
                  ' c entering a number of how many days ago, e.g.:'
                  ' "0" (today), "1" (yesterday), "10" (ten days ago), "-1" (tomorrow)')

purchase.add_argument('-n', '--product_name', type=str, required=True,
                      help='Enter the name of the product, e.g. "tagliatelle".')
purchase.add_argument('-p', '--purchase_price', type=float, required=True,
                      help='Enter the purchase price of the product, e.g. "1.22".')
purchase.add_argument('-q', '--purchase_quantity', type=int, required=True,
                      help='Enter how many products you have purchased, e.g. "25".')


sell.add_argument('-n', '--product_name', type=str, required=True,
                  help='Enter which product you have sold, e.g. "bananas".')
sell.add_argument('-p', '--sale_price', type=float, required=True,
                  help='Enter the sale price of the product, e.g. "2.35".')
sell.add_argument('-q', '--sale_quantity', type=int, required=True,
                  help='Enter how many products you have sold, e.g. "25".')

report.add_argument('type', type=str, choices=['products', 'expires', 'stock', 'transactions', 'revenue', 'profit'],
                    help='Choose which type of report you want to create.')

plot.add_argument('-y', '--year', type=int, required=True,
                  help='Enter the year for which you want to see the line graph, e.g. "2023".')
plot.add_argument('-w', '--week', type=int, required=True,
                  help='Enter the number of the week for which you want to see the line graph, e.g. "27".')
plot.add_argument('type', type=str, choices=['revenue', 'profit', 'both'],
                  help='Choose from which source you want to see a line graph of.')

args = parser.parse_args()


if __name__ == "__main__":

    if args.command == 'date':
        if args.date_change == 'today':
            dates.todays_date()
        elif args.date_change == 'yesterday':
            dates.handle_date('1')
        elif args.date_change == 'tomorrow':
            dates.handle_date('-1')
        else:
            dates.handle_date(args.date_change)
    if args.command == 'purchase':
        purchased.purchase_product(
            args.product_name, args.purchase_price, args.purchase_quantity)

    if args.command == 'sell':
        sold.sell_product(
            args.product_name, args.sale_price, args.sale_quantity)

    if args.command == 'report':
        if args.type == 'products':
            print(products.show_all_products())
        if args.type == 'stock':
            stock.daily_stock()
        if args.type == 'expires':
            stock.show_expired_products()
        if args.type == 'transactions':
            stock.show_transactions_on_date()
        if args.type == 'revenue':
            financial.daily_revenue()
        if args.type == 'profit':
            financial.daily_profit()

    if args.command == 'plot':
        plots.plot_line_graph(args.week, args.year, args.type)
