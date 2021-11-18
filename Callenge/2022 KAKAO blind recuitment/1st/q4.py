# %%
def solution(info, edges):
    graph = {i: [] for i in range(len(info))}
    for (fr, to) in edges:
        graph[fr].append(to)
    #
    answer = 0
    def __recur(visited={0}, sheep=1, wolf=0):
        nonlocal answer
        if sheep <= wolf:
            return
        if sheep > answer:
            answer = sheep
        availables = {n for v in visited for n in graph[v]} - visited
        for nxt in availables:
            __recur({nxt} | visited, sheep - (info[nxt] - 1), wolf + info[nxt])

    __recur()
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [
      0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
