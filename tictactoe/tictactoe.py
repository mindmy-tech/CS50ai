"""
Tic Tac Toe Player
"""
from random import choice
import math
import copy



X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    data = {X :0, O:0, None:0}
    for row in board:
        for col in row:
            data[col] += 1

    if data[None] % 2 != 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_possible = set()
    for x_index, row in enumerate(board):
        for y_index, col in enumerate(row):
            if col == EMPTY:
                actions_possible.add((x_index, y_index))
    return actions_possible

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyBoard = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("Invalid move")
    copyBoard[action[0]][action[1]] = player(board)
    return copyBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # row check
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # check column
    for col_index in range(3):
        if board[0][col_index] == board[1][col_index] == board[2][col_index] != EMPTY:
            return board[0][col_index]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # checks for winner

    if winner(board) != None:
        return True

    elif actions(board) == set():
        return True

    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # get terminal board
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    raise NameError('Match Pending')


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # player
    if terminal(board):
        return None

    elif board == [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]:
        moves = [(0,0), (0,2), (2,0), (2,2)]
        return choice(moves)

    elif player(board) == X:
        move = []
        for action in actions(board):
            move.append([min_value(result(board, action)), action])
        print(sorted(move))
        return sorted(move, reverse=True)[0][1]

    elif player(board) == O:
        move = []
        for action in actions(board):
            move.append([max_value(result(board, action)), action])
        print(sorted(move))
        return sorted(move)[0][1]
