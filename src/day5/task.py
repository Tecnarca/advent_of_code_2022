import re
import copy

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

def make_moves_and_get_tops(stack_columns, move_operations, reverse=True):
    for how_many, from_stack, to_stack in move_operations:
        boxes = stack_columns[from_stack][:how_many]
        if reverse:
            boxes.reverse()
        stack_columns[from_stack] = stack_columns[from_stack][how_many:]
        stack_columns[to_stack] = boxes + stack_columns[to_stack]
    return "".join(list(zip(*stack_columns))[0])


all_lines = open("input").readlines()

stack_columns = [parse_stack(all_lines[:8], column) for column in range(9)]
move_operations = [parse_operation(move_operation) for move_operation in all_lines[10:]]

print(make_moves_and_get_tops(copy.copy(stack_columns), move_operations, reverse=True))
print(make_moves_and_get_tops(stack_columns, move_operations, reverse=False))