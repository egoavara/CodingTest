# %%

def is_valid(s, offset=0):
    matching = {']': '[', '}': '{', ')': '('}
    stack = []
    for i in range(len(s)):
        c = s[(offset + i) % len(s)]
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        else:
            if len(stack) > 0 and stack[-1] == matching[c]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def solution(s):
    return sum((
        1 for i in range(len(s)) if is_valid(s, i)
    ))


print(solution(r"[](){}"))
print(solution(r"}]()[{"))
print(solution(r"[)(]"))
print(solution(r"}}}"))
