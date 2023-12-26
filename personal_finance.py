"""_summary_
"""

from datetime import datetime as dt

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from dateutil import relativedelta

currency = input('Choose a currency:')
debt = int(input('What is your current debt?'))
saved = int(input('What is your current net savings?'))
monthly_income_pre_tax = int(input('What is your monthly salary?'))
tax_percentage = int(input('What is your tax percentage?'))
net_spendings = int(input('What is your net monthly spendings?'))

year = 2020

monthly_income_post_tax = monthly_income_pre_tax * tax_percentage / 100
negative = debt + net_spendings
monthly_net_savings = int(monthly_income_post_tax - negative)


def generate_data(num_months=12, base=dt.today()) -> tuple:
    """_summary_

    :param num_months: _description_, defaults to 12
    :type num_months: int, optional
    :param base: _description_, defaults to dt.today()
    :type base: _type_, optional
    :return: _description_
    :rtype: tuple
    """

    x = [base + relativedelta(months=+i) for i in range(num_months)]
    y = saved + monthly_net_savings * np.arange(1, num_months + 1)
    return x, y


def plot_trendline(x, net_savings) -> None:
    """_summary_

    :param x: _description_
    :type x: _type_
    :param net_savings: _description_
    :type net_savings: _type_
    """

    plt.figure(figsize=(8, 6))

    # Set the locator
    locator = mdates.MonthLocator()  # every month
    # Specify the format - %b gives us Jan, Feb...
    fmt = mdates.DateFormatter('%b')

    plt.plot(x, net_savings, 'b-', label='Net savings')
    X = plt.gca().xaxis
    X.set_major_locator(locator)
    X.set_major_formatter(fmt)  # Specify formatter

    plt.ylabel(f'{currency = }')
    plt.title(f'Savings for {year}')
    plt.legend(loc=0)
    plt.grid()
    plt.show()


def show_data(x, net_savings) -> None:
    """_summary_

    :param x: _description_
    :type x: _type_
    :param net_savings: _description_
    :type net_savings: _type_
    """

    print(f'\n{currency = :>21}')
    print(f'{year = :>25}')
    print(f'{debt = :>24}')
    print(f'{saved = :>24}')
    print(f'{monthly_income_pre_tax = :>7}')
    print(f'{tax_percentage = :>15}')
    print(f'{monthly_net_savings = :>10}\n')
    print('Accumulated savings:')
    for i, j in zip(x, net_savings):
        print(f'{i.date()}: {int(j)}')


def main() -> None:
    x, net_savings = generate_data()

    show_data(x, net_savings)
    plot_trendline(x, net_savings)


if __name__ == '__main__':
    main()
