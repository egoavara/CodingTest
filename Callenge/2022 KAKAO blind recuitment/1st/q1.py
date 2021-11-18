# %%
def isprime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(n, k):
    enc = []
    while n != 0:
        enc.append(n % k)
        n = n // k
    curr = enc[-1]
    answer = 0
    for v in enc[-2::-1]:
        if v == 0:
            if curr != 0:
                if isprime(curr):    
                    answer += 1
                curr = 0

        else:
            curr = curr * 10 + v
    if enc[0] != 0:
        if curr != 0:
            if isprime(curr):    
                answer += 1
            curr = 0
    #
    return answer


print(solution(437674, 3))
# print(solution(1000000, 3))
# print(solution(11001100, 10))
# print(print(isprime(211)))
# print(solution(110011, 10))
