def draw(field):  # to check for draw
    x = 0
    y = 0

    if any('_' in n for n in field):  # if contains empty cells
        return False

    while y in range(3):  # if any row has 3 in a row
        if field[y][0] == field[y][1] == field[y][2]:
            return False
        y += 1

    while x in range(3):  # if any column has 3 in a row
        if field[0][x] == field[1][x] == field[2][x]:
            return False
        x += 1

    if field[0][0] == field[1][1] == field[2][2]:  # if field has top-left-to-bottom-right X/O
        return False

    if field[0][2] == field[1][1] == field[2][0]:  # if field has top-right-to-bottom-left X/O
        return False

    return True


def x_wins(field):  # to check if x wins
    x = 0
    y = 0

    while y in range(3):  # if any row has 3 X in a row
        if field[y][0] == field[y][1] == field[y][2] == 'X':
            return True
        y += 1

    while x in range(3):  # if any column has 3 O in a row
        if field[0][x] == field[1][x] == field[2][x] == 'X':
            return True
        x += 1

    if field[0][0] == field[1][1] == field[2][2] == 'X':  # if field has top-left-to-bottom-right X
        return True

    if field[0][2] == field[1][1] == field[2][0] == 'X':  # if field has top-right-to-bottom-left X
        return True

    return False


def o_wins(field):  # to check if x wins
    x = 0
    y = 0

    while y in range(3):  # if any row has 3 X in a row
        if field[y][0] == field[y][1] == field[y][2] == 'O':
            return True
        y += 1

    while x in range(3):  # if any column has 3 O in a row
        if field[0][x] == field[1][x] == field[2][x] == 'O':
            return True
        x += 1

    if field[0][0] == field[1][1] == field[2][2] == 'O':  # if field has top-left-to-bottom-right X
        return True

    if field[0][2] == field[1][1] == field[2][0] == 'O':  # if field has top-right-to-bottom-left X
        return True

    return False


def not_finished(field):  # to check if the game is not finished
    x = 0
    y = 0

    if any('_' in n for n in field):  # if contains empty cells
        return True

    while y in range(3):  # if any row has 3 in a row
        if field[y][0] == field[y][1] == field[y][2]:
            return False
        y += 1

    while x in range(3):  # if any column has 3 in a row
        if field[0][x] == field[1][x] == field[2][x]:
            return False
        x += 1

    if field[0][0] == field[1][1] == field[2][2]:  # if field has top-left-to-bottom-right X/O
        return False

    if field[0][2] == field[1][1] == field[2][0]:  # if field has top-right-to-bottom-left X/O
        return False

    return True


def game_field(string):  # create 3x3 matrix from a string
    string = list(string)
    field = []
    n = 0

    while n < len(string):
        field.append(string[n:n + 3])
        n += 3
    return field


def print_field(field):  # print field from field matrix
    print("---------")
    print("| {} {} {} |".format(field[0][0], field[0][1], field[0][2]))
    print("| {} {} {} |".format(field[1][0], field[1][1], field[1][2]))
    print("| {} {} {} |".format(field[2][0], field[2][1], field[2][2]))
    print("---------")


def finishing_condition(field):  # check whether the game is finished and print the condition

    if draw(field):
        return True
    elif x_wins(field):
        return True
    elif o_wins(field):
        return True
    elif not_finished(field):
        return False


def coordinates_to_matrix(x, y, field):  # convert input numbers to coordinates
    x = int(x)
    y = int(y)
    x_matrix = abs(y - 3)
    y_matrix = abs(x - 1)
    return field[x_matrix][y_matrix]


def input_correctness_check(coordinate):  # checks if coordinate is correct, return False if there is a mistake

    coordinate = str(coordinate)
    coordinate = coordinate.lower()
    contains_letters = coordinate.islower()  # writes True to contains_letters if the string contains letters
    if contains_letters:
        print("You should enter numbers!")
        return False
    if int(coordinate) > 3 or int(coordinate) < 1:
        print("Coordinates should be from 1 to 3!")
        return False

    return True


def input_character(character, field):
    coordinates = input("Enter the coordinates:").split(" ")

    while len(coordinates) != 2:
        print("You should enter two numbers!")
        coordinates = input("Enter the coordinates:").split()

    while not input_correctness_check(coordinates[0]):
        coordinates = input("Enter the coordinates:").split()

    while not input_correctness_check(coordinates[1]):
        coordinates = input("Enter the coordinates:").split()

    while coordinates_to_matrix(coordinates[0], coordinates[1], field) != '_':
        print("This cell is occupied! Choose another one!")
        coordinates = input("Enter the coordinates:").split()

    x_matrix = abs(int(coordinates[1]) - 3)
    y_matrix = abs(int(coordinates[0]) - 1)

    field[x_matrix][y_matrix] = character


x_o_string = '_________'
x_o_field = game_field(x_o_string)
print_field(x_o_field)

while not finishing_condition(x_o_field):
    input_character('X', x_o_field)
    print_field(x_o_field)

    if finishing_condition(x_o_field):
        break

    input_character('O', x_o_field)
    print_field(x_o_field)

if draw(x_o_field):
    print("Draw")
elif x_wins(x_o_field):
    print("X wins")
elif o_wins(x_o_field):
    print("O wins")

