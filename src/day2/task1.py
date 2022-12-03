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

draw_score = is_draw.sum() * 3
win_score = is_win.sum() * 6
print(draw_score + win_score + strategy[1].sum())