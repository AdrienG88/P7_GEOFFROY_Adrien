import sys
import csv
import time

starting_time = time.time()
MAXIMUM_INVESTMENT = 500


# Calculates total stock value from a list
def calculate_stocks_value(lst):
    stocks_value_list = []
    for stock in lst:
        stocks_value_list.append(stock[1])
    return float(sum(stocks_value_list))


# Calculates profit from bought stocks from a list
def calculate_profit(lst):
    profit_list = []
    for stock in lst:
        profit_list.append(stock[1] * stock[2] / 100)
    return sum(profit_list)


# Generates and tests all stocks combinations from a list, prints results
def generate_all_combinations(lst):

    combinations_list = [[]]
    best_profit = 0

    for stock in lst:

        temp_list = []

        for old_comb in combinations_list:
            new_comb = old_comb.copy()
            new_comb.append(stock)
            temp_list.append(new_comb)
            temp_list.append(old_comb)

        combinations_list = temp_list

    for comb in combinations_list:
        comb_stocks_value = calculate_stocks_value(comb)

        if comb_stocks_value <= MAXIMUM_INVESTMENT:
            tested_profit = calculate_profit(comb)

            if tested_profit > best_profit:
                best_profit = tested_profit
                best_comb = comb

    print("Best stock combination: ")
    for stock in best_comb:
        print(stock)
    print("Total money spent: €", calculate_stocks_value(best_comb))
    print("Total profit within 2 years: €", best_profit)
    print("Execution time", time.time() - starting_time, "secondes")


# Imports data from external file and executes main script
try:
    with open(sys.argv[1], newline='') as csvfile:
        stocks = csv.reader(csvfile, delimiter=',', quotechar='|')
        stocks_list = []
        for row in stocks:
            stocks_list.append(
                [
                    row[0],
                    float(row[1]),
                    float(row[2].replace('%', ''))
                ]
            )

        generate_all_combinations(stocks_list)

except FileNotFoundError:
    print("File not found. Please check filename.")

