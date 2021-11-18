# %%

def solution(n, info):
    # 점수 계산 공식
    def calc_diff(apeach, lion):
        ascore = 0
        lscore = 0
        for i, (a, l) in enumerate(zip(apeach, lion)):
            if a == l == 0:
                continue
            if a >= l:
                ascore += 10 - i
            elif a < l:
                lscore += 10 - i
        return lscore - ascore
    # 더 쉬운 승리법

    def easier(a, b):
        for ea, eb in zip(reversed(a), reversed(b)):
            if ea > eb:
                return a
            elif eb > ea:
                return b
        #
        return a
    answer = [-1]
    score_diff = 0
    #
    def search(curr, i):
        nonlocal answer
        nonlocal score_diff
        left = n - sum(curr)
        if i == 11:
            if left != 0:
                return
            curr[10] += left
            curr_diff = calc_diff(info, curr)
            if curr_diff == 0:
                return
            if curr_diff > score_diff:
                print("더 큰 점수")
                print(curr)
                print(curr_diff)
                score_diff = curr_diff
                answer = curr
            elif curr_diff == score_diff:
                print("같은 점수")
                print(answer)
                print(curr)
                print(curr_diff)
                answer = easier(answer, curr)
            return
        for hit in reversed(range(left + 1)):
            branch = curr.copy()
            branch[i] = hit
            search(branch, i+1)
    search([0 for _ in range(11)], 0)
    return answer


# print(solution(2, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]))
