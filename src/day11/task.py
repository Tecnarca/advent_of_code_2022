import dataclasses
from typing import List, Callable, Tuple
import math
from functools import reduce
import operator

@dataclasses.dataclass
class Monkey:
    number: int
    worry_levels: List[int]
    operation: Callable[[int], int]
    test: Callable[[int],bool]
    to_monkey: int
    else_monkey: int
    modulo_condition: int

    def get_throws(self, part_one=True, max_modulo=0) -> List[Tuple[int, int]]:
        throws = []
        for item in self.worry_levels:
            worry_level = int(self.operation(item)/3) if part_one else self.operation(item)%max_modulo
            to_monkey = self.to_monkey if self.test(worry_level) else self.else_monkey
            throws.append((to_monkey, worry_level))
        self.worry_levels = []
        return throws

math_signs = {
    "*": (lambda x, y: x*y),
    "+": (lambda x, y: x+y),
    "-": (lambda x, y: x-y),
    "/": (lambda x, y: x/y)
}

def make_monkey_from_text(text_lines):
    monkey_number = int(text_lines[0].split("Monkey ")[-1][:-1])
    monkey_items = list(map(int, text_lines[1].replace(",", "").split(" ")[2:]))
    math_sign = math_signs[text_lines[2].split(" ")[-2]]
    if (value := text_lines[2].split(" ")[-1])!="old":
        operation = (lambda x: math_sign(x, int(value)))
    else:
        operation = (lambda x: math_sign(x, x))
    modulo_condition = int(text_lines[3].split(" ")[-1])
    test_condition = (lambda x: (x%modulo_condition)==0)
    if_true = int(text_lines[4].split(" ")[-1])
    if_false = int(text_lines[5].split(" ")[-1])
    return Monkey(monkey_number, monkey_items, operation, test_condition, if_true, if_false, modulo_condition)

def lcm(numbers: List[int]):
    return abs(reduce(operator.mul, numbers)) // reduce(math.gcd, numbers)

def get_monkey_business(monkeys, rounds, part_one=True):
    monkey_throws = [0] * len(monkeys)
    max_modulo = lcm([monkey.modulo_condition for monkey in monkeys])
    for _ in range(rounds):
        for index, monkey in enumerate(monkeys):
            throws = monkey.get_throws(part_one, max_modulo)
            monkey_throws[index] += len(throws)
            for monkey_index, stress in throws:
                monkeys[monkey_index].worry_levels.append(stress)
    active_monkeys = sorted(monkey_throws, reverse=True)
    return active_monkeys[0] * active_monkeys[1]


lines = [line.strip() for line in open("input")]
monkeys = [make_monkey_from_text(lines[i:i+6]) for i, line in enumerate(lines) if line.startswith("Monkey")]
new_monkeys = [make_monkey_from_text(lines[i:i+6]) for i, line in enumerate(lines) if line.startswith("Monkey")]

print(get_monkey_business(monkeys, 20))
print(get_monkey_business(new_monkeys, 10000, part_one=False))