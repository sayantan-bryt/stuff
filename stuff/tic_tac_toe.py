import typing

def check(board: typing.List[typing.List[chr]], dimensions: int, player: chr) -> bool:
    n = dimensions
    # is row
    is_row = False
    for i in range(n):
        row = True
        for j in range(n):
            row &= board[i][j] == player
        is_row |= row
    # is col
    is_col = False
    for i in range(n):
        col = True
        for j in range(n):
            col &= board[j][i] == player
        is_col |= col
    # is diag
    is_diag_l, is_diag_r = True, True
    for i in range(n):
        is_diag_l &= board[i][i] == player
        is_diag_r &= board[i][n-i-1] == player

    is_diag = is_diag_l | is_diag_r

    return is_row | is_col | is_diag


def checkCleaned(board: typing.List[typing.List[chr]], dimensions: int, player: chr) -> bool:
    n = dimensions
    is_row = False
    is_col = False
    is_diag_l, is_diag_r = True, True
    for i in range(n):
        row = True
        col = True
        for j in range(n):
            # is row
            row &= board[i][j] == player
            # is col
            col &= board[j][i] == player

        is_row |= row
        is_col |= col

        # is diag
        is_diag_l &= board[i][i] == player
        is_diag_r &= board[i][n-i-1] == player

    is_diag = is_diag_l | is_diag_r

    return is_row | is_col | is_diag
