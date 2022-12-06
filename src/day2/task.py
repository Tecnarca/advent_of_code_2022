import pandas

strategy = pandas.read_csv('input', delimiter=' ', header=None)
strategy[0] = strategy[0].replace({"A": 1, "B": 2, "C": 3})
strategy[1] = strategy[1].replace({"X": 1, "Y": 2, "Z": 3})
is_draw = (strategy[0] == strategy[1])
is_win = (
    ((strategy[0] == 1) & (strategy[1] == 2)) |
    ((strategy[0] == 2) & (strategy[1] == 3)) |
    ((strategy[0] == 3) & (strategy[1] == 1))
)

print(is_draw.sum() * 3 + is_win.sum() * 6 + strategy[1].sum())

strategy[1] = strategy[1].replace({"X": 0, "Y": 3, "Z": 6})

possible_round_scores = {
    1: 3,
    2: 1,
    3: 2,
    4: 1,
    5: 2,
    6: 3,
    7: 2,
    8: 3,
    9: 1
}

print((strategy[1] + (strategy[0] + strategy[1]).replace(possible_round_scores)).sum())