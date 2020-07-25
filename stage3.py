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


def impossible(field):  # to check if the game is impossible
    x = 0
    y = 0
    x_row = 0
    o_row = 0
    x_column = 0
    o_column = 0

    x_count = sum(n.count('X') for n in field)
    o_count = sum(n.count('O') for n in field)

    while y in range(3):  # if any row has 3 in a row
        if field[y][0] == field[y][1] == field[y][2] == 'X':
            x_row = True
        if field[y][0] == field[y][1] == field[y][2] == 'O':
            o_row = True
        y += 1

    while x in range(3):  # if any column has 3 in a row
        if field[0][x] == field[1][x] == field[2][x] == 'X':
            x_column = True
        if field[0][x] == field[1][x] == field[2][x] == 'O':
            o_column = True
        x += 1

    if x_row == True and o_row == True:  # if field contains both x and o rows
        return True

    if x_column == True and o_column == True:  # if field contains both x and o columns
        return True

    if x_count - o_count > 1:  # if difference between amount of x and o more than 1
        return True

    if o_count - x_count > 1:  # if difference between amount of o and x more than 1
        return True

    return False


def not_finished(field):    # to check if the game is not finished
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


def game_field(x_o_string):  # create 3x3 matrix from a string
    x_o_string = list(x_o_string)
    x_o_field = []
    n = 0
    while n < len(x_o_string):
        x_o_field.append(x_o_string[n:n + 3])
        n += 3
    return x_o_field


x_o_string = input("Enter cells: ")
x_o_field = game_field(x_o_string)

print("---------")
print("| {} {} {} |".format(x_o_field[0][0], x_o_field[0][1], x_o_field[0][2]))
print("| {} {} {} |".format(x_o_field[1][0], x_o_field[1][1], x_o_field[1][2]))
print("| {} {} {} |".format(x_o_field[2][0], x_o_field[2][1], x_o_field[2][2]))
print("---------")

if impossible(x_o_field):
    print("Impossible")
elif draw(x_o_field):
    print("Draw")
elif x_wins(x_o_field):
    print("X wins")
elif o_wins(x_o_field):
    print("O wins")
elif not_finished(x_o_field):
    print("Game not finished")


