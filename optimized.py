import sys
import csv
import time
from math import ceil

starting_time = time.time()

# Maximum value of added stock values
MAX_INVESTMENT = 500

# Integer that defines how many decimal places are considered in input stock values.
# Improves result accuracy but at the expense of temporal complexity!
decimal_acc = 0


# Calculates total stock value from a list
def calculate_stocks_value(lst):
    stocks_value_list = []
    for s in lst:
        stocks_value_list.append(s[1])
    return sum(stocks_value_list)


# Generates matrix and gets best combination
def knapsack(lst):

    maxi = MAX_INVESTMENT * (10 ** decimal_acc)

    matrix = [[0 for x in range(maxi + 1)] for x in range(len(lst) + 1)]

    for i in range(1, len(lst) + 1):
        for j in range(1, maxi + 1):
            if lst[i-1][1] <= j:
                matrix[i][j] = max(
                    lst[i-1][2] + matrix[i-1][j-lst[i-1][1]],
                    matrix[i-1][j]
                )
            else:
                matrix[i][j] = matrix[i-1][j]

    m = maxi
    n = len(lst)
    best_comb = []

    while m >= 0 and n >= 0:
        elt = lst[n-1]
        if matrix[n][m] == matrix[n-1][m-elt[1]] + elt[2]:
            best_comb.append(elt)
            m -= elt[1]

        n -= 1

    print("Best combination: ")
    for c in best_comb:
        print(c[0])
    print("Price: ", (calculate_stocks_value(best_comb)) / (10 ** decimal_acc), "€")
    print("Profit: ", (matrix[len(lst)][maxi]), "€ after 2 years.")
    print("Elapsed time: ", time.time()-starting_time, "seconds")


# Converts parameter file for processing, executes main script
try:
    with open(sys.argv[1], newline='') as csvfile:
        stocks = csv.reader(csvfile, delimiter=',', quotechar='|')
        stocks_list = []
        for row in stocks:
            if float(row[1]) <= 0:
                pass
            else:
                stocks_list.append(
                    [
                        row[0],
                        int(ceil(float(row[1])*(10 ** decimal_acc))),
                        float(float(row[1]) * float(row[2].replace('%', '')) / 100)
                    ]
                )

        knapsack(stocks_list)

except FileNotFoundError:
    print("File not found. Please check filename.")
