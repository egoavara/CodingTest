# %%
DP = {'a' : True, 'b' : False, 'aa' : False, 'ba' : True, 'ab' : False, 'bb':False}
USED = {}


TABLE = {"aa": "b", "ba": "a", "ab": "b", "bb": "b"}

def solv(data: str) -> bool:
    if data == 'a':
        return True
    if data == 'b':
        return False

    result = False
    for i in range(len(data)-1):
        left = data[:i]
        param = data[i:i+2]
        calc = TABLE[param]
        right = data[i+2:]
        ndat = left + calc + right
        if solv(ndat):
            result = True
            break
    return result



CNT = 0


def solv_dp(data: str) -> bool:
    if data in DP:
        USED[data] = USED[data] + 1 if data in USED else 1
        return DP[data]

    result = False
    for i in range(len(data)-1):
        left = data[:i]
        calc = TABLE[data[i:i+2]]
        right = data[i+2:]
        ndat = left + calc + right
        if solv_dp(ndat):
            result = True
            break

    DP[data] = result
    return result

# F(5) = F(4) + F(3)
# F(4) = F(3) + F(2)
# F(5) = 2 + 1 + F(3)
# F(3) = F(2) + F(1) = 2
# F(2), F(1) = 1
# print(solv("aba"))
# print(solv("aaba"))
# print(solv("aab"))
# 
print(solv_dp("abaaaab"))
print(USED)
# print(solv_dp("aaba"))
# print(solv_dp("aab"))

