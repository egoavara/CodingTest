# %%
def solution(s):
    answer = len(s)
    for i in range(len(s) // 2, 0, -1):
        build = ''
        l = 0
        current = s[0:i]
        repeat = 0
        for from_at in range(0, len(s), i):
            if current == s[from_at:from_at + i]:
                repeat += 1
            else:
                build += current if repeat == 1 else str(repeat) + current
                l += len(current) if repeat == 1 else len(str(repeat)
                                                          ) + len(current)
                current = s[from_at:from_at + i]
                repeat = 1
        build += current if repeat == 1 else str(repeat) + current
        l += len(current) if repeat == 1 else len(str(repeat)) + \
            len(current)
        print(
            f'build[i={i}, {len(s) % i}] : {build}, len(build) : {len(build)}, l : {l}')
        answer = min(answer, l)
    return answer


questions = [
    ("aaaaaaaaaaaaaaabbbbbbbbbbc",),
    ("aabbaccc",),
    ("ababcdcdababcdcd",),
    ("abcabcdede",),
    ("abcabcabcabcdededededede",),
    ("xababcdcdababcdcd",),
]
for q in questions:
    print(f'solution("{q}") = {solution(*q)}')
# %%
