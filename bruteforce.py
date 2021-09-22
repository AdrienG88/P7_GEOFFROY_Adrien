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
    if stocks_value_sum <= 200:
        result.append(tmp)
    while len(tmp) > 0:

        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            print(result)
            return n_length_combo(iterable, r-1)

        index[i] += 1

        for j in range(i + 1, r):
            index[j] = index[j - 1] + 1

        # yield tuple(char[i] for i in index)
        tmp = tuple(char[i] for i in index)
        stocks_value_sum = int()
        for stock in range(0, len(tmp)):
            stocks_value_sum += tmp[stock][1]
        if stocks_value_sum <= 200:
            result.append(tmp)


stocks = [
    ("Action1", 20, 0.05),
    ("Action2", 30, 0.10),
    ("Action3", 50, 0.15),
    ("Action4", 70, 0.20),
    ("Action5", 60, 0.17),
    ("Action6", 80, 0.25)
]

stocks_full = [
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

n_length_combo("abcdef", 4)