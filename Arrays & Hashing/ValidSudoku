# One pass, in addition to checking the rows and columns, we use a key of y // 3, x // 3 to identify squares.
from collections import defaultdict

def isValidSudoku(self, board: List[List[str]]) -> bool:
    row_hashset = defaultdict(set)
    col_hashset = defaultdict(set)
    square_hashset = defaultdict(set)

    for y in range(9):
        for x in range(9):
            if board[y][x] == '.':
                continue
            if(board[y][x] in row_hashset[y]):
                return False
            if(board[y][x] in col_hashset[x]):
                return False
            if(board[y][x] in square_hashset[(y // 3, x // 3)]):
                return False
            row_hashset[y].add(board[y][x])
            col_hashset[x].add(board[y][x])
            square_hashset[(y // 3, x // 3)].add(board[y][x])
    return True
