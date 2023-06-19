"""
Tic Tac Toe Player
"""

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
    data = {}
    for row in board:
        for col in row:
            if col in data:
                data[col] += 1
            else:
                data[col] = 1

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
                actions_possible.add(x_index, y_index)
    return actions_possible

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyBoard = copy.deepcopy(board)
    if copyBoard[action[0]][action[1]] != EMPTY:
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
    
    raise None


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


## temp for testing 

if __name__ == "__main__":
    print(player(initial_state()))