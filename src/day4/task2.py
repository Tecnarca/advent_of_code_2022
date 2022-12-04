from csv import reader

def string_interval_to_set_range(section):
    parsed_integers = list(map(int, section.split("-")))
    return set(range(parsed_integers[0], parsed_integers[1]+1))

def overlap_size(first_range, second_range):
    return bool(len(first_range.intersection(second_range)))

with open("input") as csv_file:
    set_ranges = [list(map(string_interval_to_set_range, row)) for row in reader(csv_file)]

is_subset_list = [overlap_size(*set_range) for set_range in set_ranges]

print(sum(is_subset_list))