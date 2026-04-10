import sys, copy

STARTING_PIECES = {
    "a8": "bR",
    "b8": "bN",
    "c8": "bB",
    "d8": "bQ",
    "e8": "bK",
    "f8": "bB",
    "g8": "bN",
    "h8": "bR",
    "a7": "bP",
    "b7": "bP",
    "c7": "bP",
    "d7": "bP",
    "e7": "bP",
    "f7": "bP",
    "g7": "bP",
    "h7": "bP",
    "a1": "wR",
    "b1": "wN",
    "c1": "wB",
    "d1": "wQ",
    "e1": "wK",
    "f1": "wB",
    "g1": "wN",
    "h1": "wR",
    "a2": "wP",
    "b2": "wP",
    "c2": "wP",
    "d2": "wP",
    "e2": "wP",
    "f2": "wP",
    "g2": "wP",
    "h2": "wP",
}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = "||"
BLACK_SQUARE = "  "


def print_chessboard(board):
    squares = []
    is_white_square = True  # The upper left square is white, so it's True
    for y in "87654321":
        for x in "abcdefgh":
            if (
                x + y in board.keys()
            ):  # if x is a and y is 8, it evaluates to a8, and x+y in board.keys() checks if that string
                # exists in the chessboard dictionary passed to this function
                squares.append(
                    board[x + y]
                )  # Will append the particular board key to each square left-right to a8,b8,c8..ln a7,b7,c7...ln depending on what the outer loop is on, and the inner loop is on. So it will append the pieces
                # in the chessboard dictionary to the squares list in order of a8,b8,c8...ln a7,b7,c7...ln a6,b6,c6...ln a5,b5,c5...ln a4,b4,c4...ln a3,b3,c3...ln a2,b2,c2...ln a1,b1,c1...ln
            else:
                if is_white_square:  # checks if True = white, False = black
                    squares.append(
                        WHITE_SQUARE
                    )  # || for white squares, and two spaces for black squares below, which is the opposite of the chessboard template, so that the pieces will be more visible on the white squares, and less visible on the black squares.
                else:
                    squares.append(BLACK_SQUARE)
            is_white_square = (
                not is_white_square
            )  # Alternates the squares color in the 8x8 grid over the left-right up-down keys looped over
        is_white_square = (
            not is_white_square
        )  # The variable needs to be toggled again after finishing a row at the end of the outermost for loop (for future new chessboards/resets). <- Bottom right corner is last, goes back to top left

    print(
        BOARD_TEMPLATE.format(*squares)
    )  # The format() string takes one string argument per {} pair to replace.
    # the * applied to the squares list passes values as individual arguments removed comma, quotes, and brackets (star syntax)
    # # inside {} pairs in the BOARD_TEMPLATE string, so that the pieces and squares will be printed in the correct order on the chessboard template
    # The first {} pair will be replaced by the first item in the squares list, the second {} pair will be replaced by the second item in the squares list, and so on until all {} pairs are replaced by their corresponding items in the squares list.


# When finished, the squares list has 64 strings.


def print_help():
    print("Interactive Chess Board")
    print("by Al Sweigart al@inventwithpython.com")
    print()
    print("Pieces:")
    print("  w - White, b - Black")
    print("  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King")
    print("Commands:")
    print("  move e2 e4 - Moves the piece at e2 to e4.")
    print("  remove e2 - Removes the piece at e2.")
    print("  set e2 wP - Sets square e2 to a white pawn.")
    print("  reset - Reset pieces back to their starting squares.")
    print("  clear - Clear the entire board.")
    print("  fill wP - Fill entire board with white pawns.")
    print("  help - Show this help information.")
    print("  quit - Quits the program.")


# if we were using a graphics library like Pygame to render the chessboard, we could still use this Python dictionary to represent the chessboard configuration.
main_board = copy.copy(
    STARTING_PIECES  # NEW GAME Feature: The original chessboard configuration is stored in the STARTING_PIECES dictionary, and we create a copy of it for the main_board variable
    # This allows us to modify the main_board without affecting the original configuration in STARTING_PIECES, which can be useful for resetting the board or starting new games without having to redefine the starting positions each time.
)  # Call the Dictionary not the List version squares, and a copy in order to reduce errors across the program & most importantly, unique alternations for each chessboard/game, like the original is part of the executable
print_help()
while True:
    print_chessboard(
        main_board
    )  # Run the print_chessboard function to display the current state of the chessboard, below it can be altered by user commands
    #  with 'print_chessboard()' the function being like an executable that runs the code inside it when called with parentheses
    response = input("> ").split()
    # The split() method is used to split the input string into a list of words based on whitespace. For example, if the user inputs "move e2 e4", the response variable will be a list: ["move", "e2", "e4"]
    # This allows us to easily access the command and its arguments separately in the code that follows. squares* from before formats the response to be used in the chessboard template
    # REPL LOOP: The while True loop creates a REPL (Read-Eval-Print Loop) that continuously prompts the user for input, processes the command, and updates the chessboard accordingly until the user decides to quit the program.
    if response[0] == "move":
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == "remove":
        del main_board[response[1]]
    elif response[0] == "set":
        main_board[response[1]] = response[2]
    elif response[0] == "reset":
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == "clear":
        main_board = {}
    elif response[0] == "fill":
        for y in "87654321":
            for x in "abcdefgh":
                main_board[x + y] = response[1]
    elif response[0] == "help":
        print_help()
    elif response[0] == "quit":
        sys.exit()

"""
This is solid, what I've built. If I wanted, I could deploy my own chess game app just like this using Pygame- not too many alterations.
Things like buttons, cybersecuriyt, user accounts, logs of information, and more could be added to make it more interactive and 
user-friendly. I could also add features like a chess engine for single-player mode, or online multiplayer functionality.
The possibilities are endless with this basic structure in place.
You could also add features like saving and loading game states, running Moves Out of A Professional Chess Book with predetermined 
chess positions for Learning, or even implementing a chess AI opponent using algorithms like Minimax or machine learning techniques.
"""
