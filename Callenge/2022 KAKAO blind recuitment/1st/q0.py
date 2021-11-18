# %%
def solution(id_list, report, k):
    id_report = {id: set() for id in id_list}
    id_reported = {id: set() for id in id_list}
    for r in report:
        a, b = r.split(" ")
        id_report[a].add(b)
        id_reported[b].add(a)

    banned = {id for id, bans in id_reported.items() if len(bans) >= k}
    return [len(id_report[id] & banned) for id in id_list]


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
