# %%
def solution(n, words):
    used = {words[0]}
    prev = words[0]
    for i, w in enumerate(words[1:]):
        if prev[-1] != w[0] or w in used:
            return [(i + 1) % n + 1, (i + 1) // n + 1]
        used.add(w)
        prev = w
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
