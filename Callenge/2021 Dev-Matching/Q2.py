# %%


def solution(leave, day, holidays):
    DATE = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    holidays = set(holidays)
    first = DATE.index(day)
    for i in range(30):
        if DATE[(first + i) % 7] in ('SAT', 'SUN'):
            holidays.add(i + 1)
    maxh = leave
    for i in range(30):
        currl = leave
        currd = i + 1
        currh = 0
        while (currl > 0 or currd in holidays) and currd <= 30:
            if currd not in holidays:
                currl -= 1
            currd += 1
            currh += 1
        # print(f'{i+1} : {currh}')
        maxh = max(maxh, currh)
    return maxh


print(solution(4, "FRI", [6, 21, 23, 27, 28]))
print(solution(3, "SUN", [2, 6, 17, 29]))
print(solution(30,"MON",[1, 2, 3, 4, 28, 29, 30]))
