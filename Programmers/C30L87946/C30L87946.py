# %%
import itertools as it


def solution(k, dungeons):
    answer = 0
    for order in it.permutations(range(len(dungeons)), len(dungeons)):
        c = k
        passed = 0
        for i in order:
            if c >= dungeons[i][0]:
                c -= dungeons[i][1]
                passed += 1
            else:
                break
        answer = max(passed, answer)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
