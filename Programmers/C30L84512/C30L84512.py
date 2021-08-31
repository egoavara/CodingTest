# %%

import itertools as it


def solution(word):
    csets = "AEIOU"
    answer = 0
    for i, c in enumerate(word):
        avs = csets[:csets.find(c)]
        prev = answer
        answer += len(avs) * sum(5 ** r for r in range(5 - i)) + 1
        print(
            f"> '{word[:i]}[{avs}]' => {answer - prev}, acc({answer}), {[r for r in range(5 - i)]}")
    # print(avs)
    # answer += len(avs)
    return answer


# print(solution("A"))
# print(solution("AAAAE"))
# print(solution("AAAE"))
print(solution("I"))
# print(solution("EIO"))
# print(solution("EI"))
# print(5 ** 4)
# %%

# 단축 코드
def solution(word):
    return sum((len("AEIOU"[:"AEIOU".find(c)]) * sum(5 ** r for r in range(5 - i)) + 1) for i, c in enumerate(word))
# %%
# 초단축 코드

solution = lambda word : sum((len("AEIOU"[:"AEIOU".find(c)]) * sum(5 ** r for r in range(5 - i)) + 1) for i, c in enumerate(word))
# %%
table = sorted(it.chain(*((map(lambda x: "".join(x), it.product("AEIOU", repeat=i+1)) for i in range(5)))))
print(table.index("I") + 1)
# print(table)
