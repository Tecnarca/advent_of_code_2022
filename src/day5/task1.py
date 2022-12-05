import re

def parse_stack(stacks_strings, column):
    letter_index = 4 * column + 1
    return [
        stack_content_line[letter_index]
        for stack_content_line in stacks_strings
        if stack_content_line[letter_index] != ' '
    ]

def parse_operation(stacks_string):
    parsed = list(map(int, re.findall(r"\d+", stacks_string)))
    parsed[1] -= 1
    parsed[2] -= 1
    return parsed


with open("input") as input_file:
    all_lines = input_file.readlines()

stack_columns = [parse_stack(all_lines[:8], column) for column in range(9)]
move_operations = [parse_operation(move_operation) for move_operation in all_lines[10:]]

for operation in move_operations:
    boxes = stack_columns[operation[1]][:operation[0]]
    boxes.reverse()
    stack_columns[operation[1]] = stack_columns[operation[1]][operation[0]:]
    stack_columns[operation[2]] = boxes + stack_columns[operation[2]]

print("".join(list(zip(*stack_columns))[0]))