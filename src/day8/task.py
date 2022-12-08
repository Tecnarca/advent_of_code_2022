import itertools
import numpy

def get_iterator_of_2d_array_except_edges(tree_array):
    return itertools.product(range(1, tree_array.shape[0] - 1), range(1, tree_array.shape[1] - 1))
def solve_part_one(tree_array: numpy.ndarray):
    visible_inside = [
        (
                (tree_array[i, j] > numpy.max(tree_array[i, :j])) |
                (tree_array[i, j] > numpy.max(tree_array[i, j + 1:])) |
                (tree_array[i, j] > numpy.max(tree_array[:i, j])) |
                (tree_array[i, j] > numpy.max(tree_array[i + 1:, j]))
        )
        for i, j in get_iterator_of_2d_array_except_edges(tree_array)
    ]
    return sum(2 * tree_array.shape) - 4 + sum(visible_inside)

def get_visibility_for_side(side_array, tree_height):
    return (
        are_higher.nonzero()[0][0] + 1
        if numpy.any((are_higher := (side_array >= tree_height)))
        else side_array.shape[0]
    )
def solve_part_two(tree_array):
    visibilities = [
        (
            get_visibility_for_side(numpy.flip(tree_array[i, :j]), tree_array[i, j]) *
            get_visibility_for_side(numpy.flip(tree_array[:i, j]), tree_array[i, j]) *
            get_visibility_for_side(tree_array[i + 1:, j], tree_array[i, j]) *
            get_visibility_for_side(tree_array[i, j + 1:], tree_array[i, j])
        )
        for i, j in get_iterator_of_2d_array_except_edges(tree_array)
    ]
    return max(visibilities)



with open("input") as input_file:
    trees_array = numpy.array([list(map(int, list(line.strip()))) for line in input_file])

print(solve_part_one(trees_array))
print(solve_part_two(trees_array))
