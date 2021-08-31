# %%

def solution(n, t, m, timetable):
    timetable = list(map(lambda tstr: int(
        tstr[:2]) * 60 + int(tstr[3:]), timetable))
    timetable.sort()
    start_at = 9 * 60
    bus_boards = [[] for _ in range(n)]
    for i, bus in enumerate(bus_boards):
        bus_at = start_at + t*i
        matched = 0
        for i, v in enumerate(timetable):
            if v > bus_at:
                break
            matched = i+1
        #
        bus.extend(timetable[:min(m, matched)])
        timetable = timetable[min(m, matched):]
    #
    print(bus_boards)
    lboard = max(bus_boards[-1])-1 if len(bus_boards[-1]
                                          ) == m else start_at + t * (n-1)
    return f'{lboard//60:02}:{lboard%60:02}'


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 5, ["08:00", "08:01", "08:02", "08:03",
      "08:03", "09:09", "09:09", "09:09", "09:09", "09:09"]))
print(solution(2, 10, 5, [
    "08:00", "08:01", "08:02", "08:03", "08:03",
    "08:03", "08:03", "08:03", "08:03", "08:03", 
    "08:03", "09:09", "09:09", "09:09", "09:09", 
    "09:09"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
# print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
#       "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
