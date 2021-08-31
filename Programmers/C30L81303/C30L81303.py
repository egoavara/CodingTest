# %%
import timeit


def solution(n, k, cmd):
    cursor = k
    exists = [True for i in range(n)]
    history = []
    for c in cmd:
        if c[0] == 'U':
            delta = int(c[2:])
            while delta > 0:
                if exists[cursor - 1]:
                    cursor -= 1
                    delta -= 1
                else:
                    cursor -= 1
        elif c[0] == 'D':
            delta = int(c[2:])
            while delta > 0:
                if exists[cursor + 1]:
                    cursor += 1
                    delta -= 1
                else:
                    cursor += 1
        elif c[0] == 'C':
            history.append(cursor)
            exists[cursor] = False
            next = cursor + 1
            while next < n and not exists[next]:
                next += 1
            if next == n:
                next = cursor - 1
                while not exists[next]:
                    next -= 1
            cursor = next
        elif c[0] == 'Z':
            exists[history.pop()] = True
    return ''.join((('O' if exists[i] else 'X') for i in range(n)))


def solution_linked(n, k, cmd):
    cursor = k
    exists = [True for i in range(n)]
    links = [[i-1, i+1] for i in range(n)]
    history = []
    for c in cmd:
        if c[0] == 'U':
            delta = int(c[2:])
            for _ in range(delta):
                cursor = links[cursor][0]
        elif c[0] == 'D':
            delta = int(c[2:])
            for _ in range(delta):
                cursor = links[cursor][1]
        elif c[0] == 'C':
            exists[cursor] = False
            pv, nx = links[cursor]
            if pv >= 0:
                links[pv][1] = nx
            if nx < n:
                links[nx][0] = pv
            history.append(cursor)
            if nx != n:
                cursor = nx
            else:
                cursor = pv
        elif c[0] == 'Z':
            restored = history.pop()
            exists[restored] = True
            pv, nx = links[restored]
            if pv >= 0:
                links[pv][1] = restored
            if nx < n:
                links[nx][0] = restored

    return ''.join((('O' if exists[i] else 'X') for i in range(n)))


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution_linked(
    8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))

print(
    f'timeit: {(timeit.timeit(lambda: solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]), number=100000) *1000): 10f}ms')
print(
    f'timeit: {(timeit.timeit(lambda: solution_linked(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]), number=100000) *1000): 10f}ms')
# print(solution(8, 2, ["D 2", "C", "U 3", "C",
#       "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
