with open('input') as input_file:
    rucksacks = [line[:-1] for line in input_file]

first_compartments = [set(rucksack[:len(rucksack)//2]) for rucksack in rucksacks]
second_compartments = [set(rucksack[len(rucksack)//2:]) for rucksack in rucksacks]

intersections = [
    first_compartment.intersection(second_compartment).pop()
    for first_compartment, second_compartment in zip(first_compartments, second_compartments)
]

def char_to_priority(character: str):
    intercept = 38 if character.isupper() else 96
    return ord(character) - intercept

priorities = list(map(char_to_priority, intersections))

print(sum(priorities))