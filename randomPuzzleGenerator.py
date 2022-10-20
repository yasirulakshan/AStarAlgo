import random
from copy import deepcopy


def findDash(arr):
    length = len(arr)
    dashed = []
    for i in range(length):
        for j in range(length):
            if arr[i][j] == "-":
                dashed.append([i, j])
    return dashed


def move_left(puzzle, blank_location):
    if blank_location[1] != 0:
        puzzle_left_copy = deepcopy(puzzle)
        move = "(" + puzzle_left_copy[blank_location[0]][
            blank_location[1] - 1] + ",right)"
        puzzle_left_copy[blank_location[0]][blank_location[1]] = puzzle_left_copy[blank_location[0]][
            blank_location[1] - 1]
        puzzle_left_copy[blank_location[0]][blank_location[1] - 1] = "-"
        return [puzzle_left_copy, move]


# moving the blank right
def move_right(puzzle, blank_location):
    if blank_location[1] != len(puzzle[0]) - 1:
        puzzle_right_copy = deepcopy(puzzle)
        move = "(" + puzzle_right_copy[blank_location[0]][
            blank_location[1] + 1] + ",left)"
        puzzle_right_copy[blank_location[0]][blank_location[1]] = puzzle_right_copy[blank_location[0]][
            blank_location[1] + 1]
        puzzle_right_copy[blank_location[0]][blank_location[1] + 1] = "-"
        return [puzzle_right_copy, move]


# moving the blank up
def move_up(puzzle, blank_location):
    if blank_location[0] != 0:
        puzzle_up_copy = deepcopy(puzzle)
        move = "(" + puzzle_up_copy[blank_location[0] - 1][blank_location[1]] + ",down)"
        puzzle_up_copy[blank_location[0]][blank_location[1]] = puzzle_up_copy[blank_location[0] - 1][blank_location[1]]
        puzzle_up_copy[blank_location[0] - 1][blank_location[1]] = "-"
        return [puzzle_up_copy, move]


# moving the blank down
def move_down(puzzle, blank_location):
    if blank_location[0] != len(puzzle) - 1:
        puzzle_down_copy = deepcopy(puzzle)
        move = "(" + puzzle_down_copy[blank_location[0] + 1][
            blank_location[1]] + ",up)"
        puzzle_down_copy[blank_location[0]][blank_location[1]] = puzzle_down_copy[blank_location[0] + 1][
            blank_location[1]]
        puzzle_down_copy[blank_location[0] + 1][blank_location[1]] = "-"
        return [puzzle_down_copy, move]


# function to generate a random n puzzle with m blanks
def generate_random_puzzle(size, blanks):
    puzzle = [str(i) for i in range(1, size * size - blanks + 1)]  # adding numbers to list
    puzzle += ["-" for i in range(blanks)]  # adding blanks to list
    random.shuffle(puzzle)  # shuffling the puzzle to get a random starter puzzle

    # converting to 2d starter puzzle
    puzzle_2d = []
    for i in range(size):
        puzzle_2d.append(puzzle[i * size:(i + 1) * size])

    # generating the goal puzzle
    goal = random_move(puzzle_2d)

    # checking for starter and goal is equal. Then generating goal puzzle again.
    while puzzle_2d == goal:
        goal = random_move(puzzle_2d)

    return puzzle_2d, goal


# moving a given function n number of  random moves.
def random_move(puzzle):
    moves = random.randint(1, 30)  # generating random number of moves
    goal = deepcopy(puzzle)  # getting deepcopy of the given starter puzzle

    # moving n times
    for i in range(moves):
        blank_locations = findDash(goal)
        moving_blank = blank_locations[random.randint(0, len(blank_locations) - 1)]  # getting random blank to move
        move_type = random.randint(0, 3)  # getting random move(left, right, up, down)

        if move_type == 0:
            move = move_left(goal, moving_blank)
            if move:
                goal = move[0]

        elif move_type == 1:
            move = move_right(goal, moving_blank)
            if move:
                goal = move[0]

        elif move_type == 2:
            move = move_up(goal, moving_blank)
            if move:
                goal = move[0]

        else:
            move = move_up(goal, moving_blank)
            if move:
                goal = move[0]

    return goal


def puzzle_write(filename, puzzle, start=True):
    if start:
        file = open("start/" + filename, "w")
    else:
        file = open("end/" + filename, "w")

    for row in puzzle:
        file.write(" ".join(row) + "\n")
    file.close()


counter = 0

# generating 60 5x5 puzzles
for i in range(60):
    counter += 1
    start, goal = generate_random_puzzle(5, 2)
    filename = str(counter) + ".txt"
    puzzle_write(filename, start)
    puzzle_write(filename, goal, False)

# generating 20 7x7 puzzles
for i in range(20):
    counter += 1
    start, goal = generate_random_puzzle(7, 2)
    filename = str(counter) + ".txt"
    puzzle_write(filename, start)
    puzzle_write(filename, goal, False)

# generating 15 14x14 puzzles
for i in range(15):
    counter += 1
    start, goal = generate_random_puzzle(14, 2)
    filename = str(counter) + ".txt"
    puzzle_write(filename, start)
    puzzle_write(filename, goal, False)

# generating 3 17x17 puzzles
for i in range(4):
    counter += 1
    start, goal = generate_random_puzzle(17, 2)
    filename = str(counter) + ".txt"
    puzzle_write(filename, start)
    puzzle_write(filename, goal, False)

# generating 2 20x20 puzzles
for i in range(1):
    counter += 1
    start, goal = generate_random_puzzle(20, 2)
    filename = str(counter) + ".txt"
    puzzle_write(filename, start)
    puzzle_write(filename, goal, False)
