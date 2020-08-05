# tic-tac-toe
Entry level python assignment from JetBrains Academy

## About

Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

## Learning outcomes

After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch, using functions, handling errors, and processing user input.

# Objectives per stage

## Stage 1

**To start things off, the program needs to be able to print any state of the field. You’ll write a serious multi-line program using a lot of prints.**

Your first task in this project is to print any state of the field in the console output. Do not forget to show the moves for both players.

## Stage 2

Now it’s time to analyze user input and print the state of the field depending on it. You’ll learn to address specific positions in a string to achieve the required outcome

In this stage, you should write a program that:

1. Reads 9 symbols from the input and writes an appropriate 3x3 field. Elements of the field can contain only `'X'`, `'O'` and `'_'` symbols.
2. Sets the field to a specific format, i.e. field should start and end with `---------`, all lines in between should start and end with `'|'` symbol and everything in the middle should be separated with a single space.

## Stage 3

Now we’re going to write a fully-functioning multi-line program that responds to the user’s actions and analyzes the state of the field. Not only will it tell you who is winning, but it will also determine if the situation on a given field is theoretically possible!

In this stage, your program should:

1. Fill the field from the input and print it as in the previous stage.
2. Find the state in which the game is at the moment and print it. Possible states:

`"Game not finished"` - when no side has a three in a row but the field has empty cells;

`"Draw"` - when no side has a three in a row and the field has no empty cells;

`"X wins"` - when the field has three X in a row;

`"O wins"` - when the field has three O in a row;

`"Impossible"` - when the field has three X in a row as well as three O in a row. Or the field has a lot more X's that O's or vice versa (if the difference is 2 or more, should be 1 or 0). For this stage, consider that the game can be started both as X's or as O's.

Also, you can use `' '` or `'_'` to print empty cells - it's up to you.

## Stage 4

Tic-tac-toe is not all about analysis – a game is meant to be played! Write a program that can change the state of the field, as your first real step toward a fully-functioning game application!

The program should work in the following way:

1. Get the 3x3 field from the input as in the previous stages.
2. Output this 3x3 field with cells before the user's move.
3. Then ask the user about his next move.
4. Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input)
5. Analyze user input and show messages in the following situations:

    - `"This cell is occupied! Choose another one!"` - if the cell is not empty;

    - `"You should enter numbers!"` - if the user enters other symbols;

    - `"Coordinates should be from 1 to 3!"` - if the user goes beyond the field.

6. Then output the table including the user's most recent move.


The program should also check user input. If the user input is unsuitable, the program should ask him to enter coordinates again.

    In addition to that added an ability to check whether the input contained 2 entries.
## Stage 5

Finally! Thanks to this app, you can always challenge a friend to play a quick game of Tic-Tac-Toe!

# References

JetBrains Academy: https://hyperskill.org/

Tic-Tac-Toe project link: https://hyperskill.org/projects/73?track=2