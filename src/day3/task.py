def char_to_priority(character: str):
    intercept = 38 if character.isupper() else 96
    return ord(character) - intercept

rucksacks = [line[:-1] for line in open('input')]

first_compartments = [set(rucksack[:len(rucksack)//2]) for rucksack in rucksacks]
second_compartments = [set(rucksack[len(rucksack)//2:]) for rucksack in rucksacks]

intersections = [
    first_compartment.intersection(second_compartment).pop()
    for first_compartment, second_compartment in zip(first_compartments, second_compartments)
]

badges = [
    set(rucksacks[rucksack_index]).intersection(set(rucksacks[rucksack_index + 1])).intersection(set(rucksacks[rucksack_index + 2])).pop()
    for rucksack_index in range(0, 300, 3)
]

print(sum(list(map(char_to_priority, intersections))))
print(sum(list(map(char_to_priority, badges))))