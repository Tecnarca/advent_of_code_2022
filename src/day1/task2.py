from csv import reader

with open("input") as csv_file:
    sums = [sum(map(int, row)) for row in reader(csv_file)]

print(sum(sorted(sums, reverse=True)[:3]))
