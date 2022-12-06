from csv import reader

def string_interval_to_set_range(section):
    parsed_integers = list(map(int, section.split("-")))
    return set(range(parsed_integers[0], parsed_integers[1]+1))

def compare_ranges(first_range, second_range):
    return first_range.issubset(second_range) or second_range.issubset(first_range)

def overlap_size(first_range, second_range):
    return bool(len(first_range.intersection(second_range)))

set_ranges = [list(map(string_interval_to_set_range, row)) for row in reader(open("input"))]

print(sum(compare_ranges(*set_range) for set_range in set_ranges))
print(sum(overlap_size(*set_range) for set_range in set_ranges))