"""
Tic Tac Toe Player
"""
import copy
import math

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
    count = 0
    for row in board:
        for row_element in row:
            if row_element is X:
                count += 1
            elif row_element is O:
                count -= 1
    if count == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] is EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise NameError("Non valid action")
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(0, len(board)):
        if board[i][0] is not EMPTY:
            j = 1
            while j < len(board[0]):
                if board[i][j] is not board[i][0]:
                    break
                j += 1
            if j == len(board[0]):
                return board[i][0]
    # Check columns
    for j in range(0, len(board[0])):
        if board[0][j] is not EMPTY:
            i = 1
            while i < len(board):
                if board[i][j] is not board[0][j]:
                    break
                i += 1
            if i == len(board):
                return board[0][j]
    # Assuming square board, check diagonal
    diagonal = 0
    anti_diagonal = 0
    for i in range(0, len(board)):
        if (board[i][i] is not EMPTY) and (board[i][i] is board[0][0]):
            diagonal += 1
        if (board[i][len(board) - i - 1] is not EMPTY) and (board[i][len(board) - i - 1] is board[0][len(board) - 1]):
            anti_diagonal += 1
    if diagonal == len(board):
        return board[0][0]
    if anti_diagonal == len(board):
        return board[0][len(board) - 1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for row_element in row:
            if row_element is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player is X:
        return 1
    elif winner_player is O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) is X:
        v = -math.inf
        for action in actions(board):
            val = min_value(result(board, action))
            if v < val:
                v = val
                best_action = action
        return best_action
    v = math.inf
    for action in actions(board):
        val = max_value(result(board, action))
        if v > val:
            v = val
            best_action = action
    return best_action


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
