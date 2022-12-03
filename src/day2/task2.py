import pandas

strategy = pandas.read_csv('input', delimiter=' ', header=None)

strategy[0] = strategy[0].replace({"A": 1, "B": 2, "C": 3})
strategy[1] = strategy[1].replace({"X": 0, "Y": 3, "Z": 6})

possible_round_scores = {
    1: 3,
    4: 1,
    7: 2,
    2: 1,
    5: 2,
    8: 3,
    3: 2,
    6: 3,
    9: 1
}

strategy[2] = (strategy[0] + strategy[1]).replace(possible_round_scores)

print((strategy[1]+strategy[2]).sum())

