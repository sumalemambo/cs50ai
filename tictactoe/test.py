X = "X"
O = "O"
EMPTY = None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, len(board)):
        j = 0
        while j < len(board[0]):
            if (board[i][j] is EMPTY) or (board[i][j] != board[i][0]):
                break
            j += 1
        if j == len(board[0]):
            return board[i][0]
    for j in range(0, len(board[0])):
        i = 0
        while i < len(board):
            if (board[i][j] is EMPTY) or (board[i][j] != board[0][j]):
                break
            i += 1
        if i == len(board):
            return board[0][j]
    # Assume square board
    diagonal = 0
    anti_diagonal = 0
    for i in range(0, len(board)):
        if (board[i][i] is not EMPTY) and (board[i][i] == board[0][0]):
            diagonal += 1
        if (board[i][len(board) - i - 1] is not EMPTY) and (board[i][len(board) - i - 1] == board[0][len(board) - 1]):
            anti_diagonal += 1
    if diagonal == len(board):
        return board[0][0]
    if anti_diagonal == len(board):
        return board[0][len(board) - 1]
    return None

board = [["X", "X", "O"],
            ["O", "O", EMPTY],
            ["X", "X", "X"]]

print(winner(board))