with open("puzzle4.txt", "r") as file:
    puzzle_input = file.read().strip().split("\n")

y = len(puzzle_input)
x = len(puzzle_input[0])

dd = list()

for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))


def contains_xmas(row, col, direction):
    delta_row, delta_col = direction
    for index, char in enumerate("XMAS"):
        new_row = row + index * delta_row
        new_col = col + index * delta_col
        if not (0 <= new_row < y and 0 <= new_col < x):
            return False
        if puzzle_input[new_row][new_col] != char:
            return False
    return True


count_xmas = 0

for row in range(y):
    for col in range(x):
        for direction in dd:
            count_xmas += contains_xmas(row, col, direction)

print(count_xmas)
