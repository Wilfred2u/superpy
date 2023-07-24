import csv
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


def todays_date():
    """Write today's date to date.csv."""
    with open('date.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date.today()])
    print(f'The working date has been changed to {get_date()}.')


def write_date(date):
    """Write the handle_date()'s date to date.csv."""
    with open('date.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date.date()])


def handle_date(input):
    """Change the program's date in either one of two ways:
       - by entering a new date;
       - by entering an integer (how many days the date advances or sets back.)
       Output is a date, written in date.csv."""
    try:
        try:
            input_date = datetime.strptime(input, '%Y-%m-%d')
            write_date(input_date)
            print(f'The working date has been changed to {get_date()}.')
        except ValueError:
            with open('date.csv', 'r'):
                input_date = datetime.today() - timedelta(int(input))
                write_date(input_date)
                print(f'The working date has been changed to {get_date()}.')
    except ValueError:
        print(f"Please enter a date, e.g. '2023-08-25',"
              "\nor one of the following words: 'today', 'yesterday', 'tomorrow',"
              "\nor an integer, e.g. '2', '0' or '-1'.")


def get_date():
    """Return the program's date."""
    with open('date.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            return ''.join(row)


def date_today():
    """Return today's date in datetime.datetime format."""
    date_today = date.today().strftime("%Y-%m-%d")
    formatted_date = datetime.strptime(date_today, "%Y-%m-%d")
    return formatted_date


def string_date_today():
    """Return today's date in string format."""
    date_today = date.today()
    return date_today


def get_expiration_date(num_days):
    todays_date = date.today()
    expiration_date = todays_date + timedelta(days=num_days)
    return expiration_date


def week_date(week, year):
    """Return a list with dates from a given weeknumber and year."""
    week_dates = []
    for x in range(1, 8):
        date_date = date(year, 1, (x+1)) + \
            relativedelta(weeks=+(week-1))
        string_date = date_date.strftime("%Y-%m-%d")
        week_dates.append(string_date)
    return week_dates
