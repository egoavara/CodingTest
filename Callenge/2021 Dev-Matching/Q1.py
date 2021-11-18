# %%
import re


def snsplit(id):
    for send, e in enumerate(id):
        if e.isnumeric():
            break
    s = id[:send] if id[send].isnumeric() else id
    n = int(id[send:]) if id[send].isnumeric() else None
    return s, n


def solution(registered_list, new_id):
    remap = {}
    for id in registered_list:
        s, n = snsplit(id)
        if s in remap:
            remap[s].add(n)
        else:
            remap[s] = {n}
    ns, nn = snsplit(new_id)

    while ns in remap and nn in remap[ns]:
        if nn is None:
            nn = 1
        else:
            nn += 1
    nn = nn if nn is not None else ''
    return f'{ns}{nn}'


print(solution(["card", "ace13", "ace16",
      "banker", "ace17", "ace14"], "ace15"))
