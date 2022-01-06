# Yunjian Lu
# AI assignment 3 Minimax

import copy

GAME_INCOMPLETE = 0
GAME_DRAW = 1
GAME_X = 2
GAME_O = 3
EMPTY = 0
# This function tests if a specific player wins. Possibilities:
#     Three rows    [X X X] or [O O O]
#     Three cols    [X X X] or [O O O]
#     Two diagonals [X X X] or [O O O]
# param  board: the state of the current board

X = 1
O = -1


# return GAME_INCOMPLETE, GAME_DRAW, GAME_X, or GAME_O
def evaluate_game(board):
    win_states = [[board[0][0], board[0][1], board[0][2]],
                  [board[1][0], board[1][1], board[1][2]],
                  [board[2][0], board[2][1], board[2][2]],
                  [board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[2][0], board[1][1], board[0][2]]]

    if [X, X, X] in win_states:
        return GAME_X
    if [O, O, O] in win_states:
        return GAME_O
    for row in board:
        for i in row:
            if i != EMPTY:
                return GAME_INCOMPLETE
    return GAME_DRAW;


# Outputs the current game state to the console
# param  board: the state of the current board
def print_board(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board[row])):
            if board[row][col] == X:
                line = line + ' X '
            elif board[row][col] == O:
                line = line + ' O '
            else:
                line = line + "   "
            if col < 2:
                line = line + "|"
        print(line)
        if row < 2:
            print("-----------")
    print("****************")
    print()


# to get the first available spot for O
def O_move(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return (row, col)
    print("ERROR! No Valid Move!")


# a helper method to get the first available spot for X. This method is used to get all possible moves
def X_move(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return (row, col)
    print("ERROR! No Valid Move!")


# A method that returns the best move for player X based on O's first available first move
def XXmove(board):
    # set the b_score to lowest score a player can get
    b_score = -15
    best_i, best_j = X_move(board)

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                # Copy the board, test all possible moves, and pick the move that leads to a maximum score
                test_board = copy.deepcopy(board)
                depth = 0

                cur_i, cur_j = X_move(test_board)
                test_board[row][col] = X
                winner = evaluate_game(test_board)
                cur_score = 0
                # list all the complete moves
                while winner == GAME_INCOMPLETE:
                    cur_i, cur_j = O_move(test_board)
                    test_board[cur_i][cur_j] = O
                    winner = evaluate_game(test_board)
                    if winner != GAME_INCOMPLETE:
                        break

                    depth += 1
                    cur_i, cur_j = X_move(test_board)
                    test_board[cur_j][cur_j] = X
                    winner = evaluate_game(test_board)
                    if winner != GAME_INCOMPLETE:
                        break
                # calculates the score of each complete game
                if winner == GAME_DRAW:
                    cur_score = -5 - depth
                elif winner == GAME_X:
                    cur_score = 10 - depth
                else:
                    cur_score = -10 - depth
                # Store the best move that gets highers score for x
                if cur_score > b_score:
                    b_score = cur_score
                    best_i, best_j = cur_i, cur_j

                # print_board(test_board)
                # print("depth",  depth, "cur_score", cur_score)
                # print("best score",b_score ," best move: ", best_i, best_j)
    return best_i, best_j


boards=[]
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

board2 = [[O, X, X],
         [O, O, X],
         [EMPTY, EMPTY, EMPTY]]
board3 = [[O, X, X],
         [O, O, X],
         [EMPTY, EMPTY, EMPTY]]


board4 = [[O, X, X],
         [O, O, X],
         [EMPTY, EMPTY, EMPTY]]
board6 = [[O, X, X],
         [O, O, X],
         [EMPTY, EMPTY, EMPTY]]


game_winner = GAME_INCOMPLETE

while game_winner == GAME_INCOMPLETE:
    i, j = XXmove(board)
    board[i][j] = X
    print_board(board)
    game_winner = evaluate_game(board)
    if game_winner != GAME_INCOMPLETE:
        break;
    i, j = O_move(board)
    board[i][j] = O
    print_board(board)
    game_winner = evaluate_game(board)

# Game is complete, announce winner
if game_winner == GAME_DRAW:
    print("Game was a Draw!")
elif game_winner == GAME_X:
    print("X Wins!!!")
else:
    print("O Wins!!!")
