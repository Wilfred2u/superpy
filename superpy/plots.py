import matplotlib.pyplot as plt
from dates import week_date
from financial import weekly_revenue, weekly_profit


def plot_line_graph(week, year, type):
    input_values = week_date(week, year)
    revenue_values = weekly_revenue(week, year)
    profit_values = weekly_profit(week, year)

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()

    if type == 'revenue':
        ax.plot(input_values, revenue_values, color=(0.2, 0.4, 0), linewidth=3)
    elif type == 'profit':
        ax.plot(input_values, profit_values, color=(0.2, 0.4, 0), linewidth=3)
    elif type == ('both'):
        ax.plot(input_values, revenue_values,
                color='darkblue', label='revenue')
        ax.plot(input_values, profit_values,
                color='darkgray', label='profit')

    if type == 'both':
        ax.set_title(
            f'Daily revenue and profit, week {week}-{year}.', fontsize=24)
        ax.set_xlabel('Date', fontsize=14)
        ax.set_ylabel(f'Revenue and profit', fontsize=14)
    else:
        ax.set_title(f'Daily {type}, week {week}-{year}.', fontsize=24)
        ax.set_xlabel('Date', fontsize=14)
        ax.set_ylabel(f'{type.title()}', fontsize=14)
    ax.tick_params(labelsize=14)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    plt.legend()
    plt.show()
