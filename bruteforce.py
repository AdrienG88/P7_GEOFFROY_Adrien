import numpy

global result
result = []


def n_length_combo(iterable, r):
    char = tuple(iterable)
    n = len(char)

    if r > n:
        return

    index = numpy.arange(r)

    # returns the first sequence
    # yield tuple(char[i] for i in index)
    tmp = tuple(char[i] for i in index)
    stocks_value_sum = int()
    for stock in range(0, len(tmp)):
        stocks_value_sum += tmp[stock][1]

    if stocks_value_sum <= 500:
        profit_list = list()
        for j in range(0, len(tmp)):
            profit_list.append(int(tmp[j][1]) * float(tmp[j][2]))
        profit_sum = sum(profit_list)
        profit_sum = round(profit_sum, 2)
        profit = ("PROFIT: ", profit_sum)
        tmp = list(tmp)
        tmp.append(profit)
        tmp = tuple(tmp)
        result.append(tmp)

    while len(tmp) > 6:

        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return n_length_combo(iterable, r-1)

        index[i] += 1

        for j in range(i + 1, r):
            index[j] = index[j - 1] + 1

        # yield tuple(char[i] for i in index)
        tmp = tuple(char[i] for i in index)
        stocks_value_sum = int()
        for stock in range(0, len(tmp)):
            stocks_value_sum += tmp[stock][1]
        if stocks_value_sum <= 500:
            profit_list = list()
            for j in range(0, len(tmp)):
                profit_list.append(int(tmp[j][1]) * float(tmp[j][2]))
            profit_sum = sum(profit_list)
            profit_sum = round(profit_sum, 2)
            profit = ("PROFIT:", profit_sum)
            tmp = list(tmp)
            tmp.append(profit)
            tmp = tuple(tmp)
            result.append(tmp)
            
    with open("bruteforce_output.json", "w") as file:
    file.write(str(result))
    return result

def get_max_profit(result):
    max_profit = None
    for stock_combination in result:
        profit_value = stock_combination[-1][1]

        if max_profit is None or profit_value > max_profit:
            max_profit = profit_value
            best_stock_option = stock_combination[0:-1]

    raw_sum = []
    for stock in best_stock_option:
        raw_sum.append(stock[1])
    invested_money = sum(raw_sum)

    print('Number of combinations:', len(result))
    print('Best buying stock-option:', best_stock_option)
    print('Money invested:', invested_money)
    print('Maximum profit:', max_profit)



stocks = [
    ("Action-1", 20, 0.05),
    ("Action-2", 30, 0.10),
    ("Action-3", 50, 0.15),
    ("Action-4", 70, 0.20),
    ("Action-5", 60, 0.17),
    ("Action-6", 80, 0.25),
    ("Action-7", 22, 0.07),
    ("Action-8", 26, 0.11),
    ("Action-9", 48, 0.13),
    ("Action-10", 34, 0.27),
    ("Action-11", 42, 0.17),
    ("Action-12", 110, 0.09),
    ("Action-13", 38, 0.23),
    ("Action-14", 14, 0.01),
    ("Action-15", 18, 0.03),
    ("Action-16", 8, 0.08),
    ("Action-17", 4, 0.12),
    ("Action-18", 10, 0.14),
    ("Action-19", 24, 0.21),
    ("Action-20", 114, 0.18)
]

get_max_profit(n_length_combo(stocks, 16))
