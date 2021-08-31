# %%
def dfs(table, expected, route, mapper):
    if len(route) == expected:
        return route
    answer = None
    for dst in table[mapper[route[-1]]]:
        if answer is not None:
            return answer
        if dst not in route:
            answer = dfs(table, expected, [*route, dst], mapper)
    # unreachable
    return answer
def solution(tickets):
    mapping = {i: b for i, (_, b) in enumerate(tickets)}
    mapping[-1] = "ICN"
    table = {v:[] for v in mapping.values()}
    for i, (a, _) in enumerate(tickets):
        table[a] = [*table[a], i]
    for k in table:
        table[k] = sorted(table[k], key=lambda a:mapping[a])
    # queue = [[-1]]
    # while queue:
    #     route = queue.pop(0)
    #     if len(route) == 1 + len(tickets):
    #         return list(map(lambda r : mapping[r], route))
    #     for dst in table[mapping[route[-1]]]:
    #         if dst not in route:
    #             queue.append([*route, dst])
    return list(map(lambda e : mapping[e], dfs(table, len(tickets) + 1, [-1], mapping)))


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# a = [['ICN','AAA'], *(a for _ in range(1000) for a in (['AAA', 'ICN'], ['ICN', 'AAA']))]
# print(a)
# print(solution(a))
print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
# print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([]))

# %%
