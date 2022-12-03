with open('input') as input_file:
    rucksacks = [line[:-1] for line in input_file]

def char_to_priority(character: str) -> int:
    intercept = 38 if character.isupper() else 96
    return ord(character) - intercept

badges = [
    set(rucksacks[rucksack_index]).intersection(set(rucksacks[rucksack_index + 1])).intersection(set(rucksacks[rucksack_index + 2])).pop()
    for rucksack_index in range(0, 300, 3)
]

priorities = list(map(char_to_priority, badges))
print(sum(priorities))