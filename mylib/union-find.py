# %%
"""Union-Find 자료구조"""


def union(ufdt, a, b):
    a = find(ufdt, a)
    b = find(ufdt, b)
    ufdt[a] = b


def find(ufdt, key):
    if key not in ufdt:
        ufdt[key] = key
    if key != ufdt[key]:
        ufdt[key] = find(ufdt, ufdt[key])
    return ufdt[key]


# %%
"""테스트"""
dt = dict()
union(dt, 1, 2)
union(dt, 2, 3)
union(dt, 3, 'A')
print(find(dt, 1))
print(find(dt, 2))
print(find(dt, 3))
print(find(dt, 'A'))
print(find(dt, 4))

# %%
