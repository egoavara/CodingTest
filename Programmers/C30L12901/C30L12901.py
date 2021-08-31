# %%
def solution(a, b):
    weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    month_per_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return weekday[(sum(month_per_day[:a-1])+b - 1 + 5) % 7]

print(solution(1, 1))
print(solution(5, 24))