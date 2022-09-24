# %%
def solution(numbers):
    availables = {"010", "011", "110", "111", "11", "01"}
    def calc(num):
        b= bin(num)[2:]
        start = 0
        end = min(3, len(b))
        while start < end:
            if b[start:end] not in availables:
                return 0
            if end < len(b) and b[end] != "1":
                return 0
            start = min(end + 1, len(b))
            end = min(start + 3, len(b))
        return 1
    return list(map(calc, numbers))
# print(solution([7, 5]))
print(solution([2 ** 7 + 2 ** 6 + 2 ** 5 + 2 ** 4 + 2 ** 3 + 2 ** 1]))

