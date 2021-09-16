# %%
def solution(a, s):
    n = len(a)
    i = 1
    cl = [i for i in range(n)]
    c = []
    #
    result = 0

    def __inner(out, n, b, i=0):
        c = []
        while i != n:
            x = b[i]
            y = b[i-1] if i > 0 else None
            if y is None:
                i += 1
            if x == y:
                __inner(out, n, b, i=i+1)
                __inner(out, n, b, i=i)

            else:
                i += 1

        out[0] += 1

    return answer
