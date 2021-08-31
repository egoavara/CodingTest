# %%
import copy
from collections import deque
import math
import itertools as it


def solution(begin, target, words):
    if target not in words:
        return 0
    words = set(it.chain(words, [begin]))
    table = {w: set() for w in words}
    for a, b in it.combinations(words, 2):
        if sum((1 if ac != bc else 0) for ac, bc in zip(a, b)) == 1:
            table[a].add(b)
            table[b].add(a)
    distances = {w: math.inf for w in words}
    queue = [(begin, 0)]
    while queue:
        word, depth = queue.pop(0)
        if depth < distances[word]:
            distances[word] = depth
            queue.extend(map(lambda e: (e, depth + 1), table[word]))
    return distances[target]


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("ddd", "aaa", ["bdd", "ddb", "dda", "xdd", "daa", "aaa"]))

# %%


def solution(begin, target, words):

    deq = deque()
    deq.append((begin, 0, "-"))

    alphabet = sorted("qwertyuiopasdfghjklzxcvbnm")

    newwords = copy.deepcopy(words)

    while(len(deq) > 0):

        current, index, parent = deq.popleft()
        print(current, index, parent, newwords, )

        if(current == target):
            return index
        if(index >= len(words)):
            continue

        for string in range(len(current)):

            for alpha in alphabet:
                newstr = current[:string]+alpha+current[string+1:]
                for aa in newwords:
                    if newstr == aa:
                        print("NEW : ", newstr, "-", index + 1)
                        newwords.remove(newstr)
                        deq.append((newstr, index+1, current))

    return 0


print(solution("dddddddd", "bbbbbbbb", [
      "dddddddb", "ddddddab", "dddddbab", "ddddbbab", "dddbbbab","ddbbbbab","dbbbbbab","dddddbbb", "ddddddbb", "dddddbbb", "ddddbbbb", "dddbbbbb", "ddbbbbbb", "dbbbbbbb", "bbbbbbbb"]))
