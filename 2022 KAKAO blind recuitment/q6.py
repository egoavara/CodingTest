# %%
def solution(board, aloc, bloc):
    # 진행 불가능한 경우
    if aloc[0] == bloc[0] and aloc[1] == bloc[1]:
        return 0
    #
    fboard = [e for line in board for e in line]
    w = len(board[0])
    h = len(board)

    def __raw_p(x, y):
        return x + y * w
    answer = -1

    def __recur(fbd, ax, ay, bx, by, depth=0):
        nonlocal answer
        is_a_turn = depth % 2 == 0
        cx = 0
        cy = 0
        if is_a_turn:
            cx = ax
            cy = ay
        else:
            cx = bx
            cy = by
        #
        availables = []
        if cx > 0 and fbd[__raw_p(cx-1, cy)] == 1:
            availables.append((cx-1, cy))
        if cx < w-1 and fbd[__raw_p(cx+1, cy)] == 1:
            availables.append((cx+1, cy))
        if cy > 0 and fbd[__raw_p(cx, cy-1)] == 1:
            availables.append((cx, cy-1))
        if cy < h-1 and fbd[__raw_p(cx, cy+1)] == 1:
            availables.append((cx, cy+1))
        # 종료 조건
        if len(availables) == 0:
            return 'B' if is_a_turn else 'A'
        # 분기

        who = '-'
        for nx, ny in availables:
            nfbd = fbd.copy()
            nfbd[__raw_p(nx, ny)] = 'A' if is_a_turn else 'B'
            if is_a_turn:
                if __recur(nfbd, nx, ny, bx, by, depth+1) == 'A':
                    print(f"\nA WIN")
                    print(nfbd, fboard)
                    cnt = sum(1 for e in nfbd if e == 'A' or e == 'B')
                    who = 'A'
                    if answer == -1 or answer > cnt:
                        answer = cnt
            else:
                if __recur(nfbd, ax, ay, nx, ny, depth+1) == 'B':
                    print(f"\nB WIN")
                    print(nfbd, fboard)
                    cnt = sum(1 for e in nfbd if e == 'A' or e == 'B')
                    who = 'B'
                    if answer == -1 or answer > cnt:
                        answer = cnt
        return who
    nfboard = fboard.copy()
    nfboard[__raw_p(aloc[1], aloc[0])] = 'A'
    nfboard[__raw_p(bloc[1], bloc[0])] = 'B'
    #
    __recur(nfboard, aloc[1], aloc[0], bloc[1], bloc[0])
    return answer


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
