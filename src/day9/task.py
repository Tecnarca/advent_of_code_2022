import dataclasses
from typing import Tuple, List, Set


@dataclasses.dataclass
class Rope:
    length: int = 1

    def __post_init__(self) -> None:
        self.knots = [Knot() for _ in range(self.length)]

    def move_rope(self, direction):
        self.knots[0].move_rope(direction)
        for rope_index in range(1, len(self.knots)):
            self.knots[rope_index].head = tuple(self.knots[rope_index - 1].tail)
            self.knots[rope_index].move_rope((0, 0))

    def get_visited_of(self, rope_index):
        return self.knots[rope_index].visited

@dataclasses.dataclass
class Knot:
    head: Tuple[int, int] = (0, 0)
    tail: List[int] = dataclasses.field(default_factory=lambda: [0, 0])
    visited: Set[Tuple[int, int]] = dataclasses.field(default_factory=set)
    def move_rope(self, direction: Tuple[int, int]):
        self._move_head(direction)
        self._move_tail()
        self._update_visited_postion()

    def _move_head(self, direction):
        self.head = (self.head[0] + direction[0], self.head[1] + direction[1])

    def _move_tail(self):
        distance_head_to_tail = (self.head[0] - self.tail[0], self.head[1] - self.tail[1])
        absolute_distance = [int(abs(distance)) for distance in distance_head_to_tail]
        if any(distance>1 for distance in absolute_distance):
           self.tail[0] += int(distance_head_to_tail[0]/absolute_distance[0]) if absolute_distance[0] != 0 else 0
           self.tail[1] += int(distance_head_to_tail[1]/absolute_distance[1])  if absolute_distance[1] != 0 else 0


    def _update_visited_postion(self):
        self.visited.add(tuple(self.tail))


letter_to_direction = {"D": (-1, 0), "R": (0, 1), "U": (1, 0), "L": (0, -1)}

def rope_mover(how_many_knots):
    rope = Rope(how_many_knots)
    movements = [line.strip().split(" ") for line in open("input")]
    for movement in movements:
        for _ in range(int(movement[1])):
            rope.move_rope(letter_to_direction[movement[0]])
    print(len(rope.get_visited_of(how_many_knots-1)))

rope_mover(1)
rope_mover(9)
