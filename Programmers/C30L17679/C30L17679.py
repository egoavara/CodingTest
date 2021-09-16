# %%
import numpy as np
import itertools as it

def solution(m, n, board):
    board = [
        [e for e in l] for l in board
    ]
    def __drop():
        for x in range(n):
            dp = -1
            for y in range(m-1, -1, -1):
                if dp == -1 and board[y][x] == '_':
                    dp = y
                elif dp != -1 and board[y][x] != '_':   
                    board[dp][x] = board[y][x]
                    board[y][x] = '_'
                    dp -=1
    def __recur():
        changed = []
        for y, x in it.product(range(m-1), range(n-1)):
            if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1] != '_':
                changed.append((x, y))
        if len(changed) > 0:
            for x, y in changed:
                board[y][x] = '_'
                board[y][x+1] = '_'
                board[y+1][x] = '_'
                board[y+1][x+1] = '_'
            __drop()
            __recur()
    __recur()
    
    return sum(1 for line in board for e in line if e == '_')


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
