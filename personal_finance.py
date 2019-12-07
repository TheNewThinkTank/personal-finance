
import datetime
from datetime import datetime as dt
from dateutil.relativedelta import *
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

currency = input('Choose a currency:')
depth = int(input('What is your current depth?'))
saved = int(input('What is your current net savings?'))
monthly_income_pre_tax = int(input('What is your monthly salary?'))
tax_percentage = int(input('What is your tax percentage?'))
net_spendings = int(input('What is your net monthly spendings?'))

year = 2020

monthly_income_post_tax = monthly_income_pre_tax * tax_percentage / 100
negative = depth + net_spendings
monthly_net_savings = int(monthly_income_post_tax - negative)


def generate_data(num_months=12, base=dt.today()):
    x = [base + relativedelta(months=+i) for i in range(num_months)]
    y = saved + monthly_net_savings * np.arange(1, num_months + 1)
    return x, y


x, net_savings = generate_data()


def plot_trendline():
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


def show_data():
    print(f'\n{currency = :>21}')
    print(f'{year = :>25}')
    print(f'{depth = :>24}')
    print(f'{saved = :>24}')
    print(f'{monthly_income_pre_tax = :>7}')
    print(f'{tax_percentage = :>15}')
    print(f'{monthly_net_savings = :>10}\n')
    print('Accumulated savings:')
    for i, j in zip(x, net_savings):
        print(f'{i.date()}: {int(j)}')


def main():
    show_data()
    plot_trendline()


if __name__ == '__main__':
    main()
