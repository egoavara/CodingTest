# %%
import re
import itertools as it

def solution(user_id, banned_id):
    return len(set(
        tuple(sorted(s))
        for s in map(lambda e: set(e), it.product(
            *(map(lambda e: e[0], it.combinations(ids, 1)) for ids in (set(uid for uid in user_id if re.compile("^" + bid.replace("*", ".") + "$").match(uid)) for bid in banned_id))
        )) 
        if len(s) == len(banned_id)
    ))


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "abc1**"]
))

print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["*rodo", "*rodo", "******"]
))
print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"]
))
