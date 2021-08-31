# %%

def solution(n):
    def tri_cnt(n):
        return n * (n+1) // 2

    def recur(out, n, start_at=1, depth=0):
        if n <= 0:
            return
        beg = tri_cnt(depth * 2) + depth
        out[beg] = start_at
        beg += 2 * (depth) + 1
        stride = 0
        curr = start_at + 1
        diff = 3 * n - 5
        for i in range(n - 2):
            out[beg] = curr
            out[beg + 1 + stride] = diff + curr
            curr += 1
            diff -= 2
            beg += 2 * (depth + 1) + stride
            stride += 1
        if n > 1:
            for i in range(n):
                out[beg] = curr + i
                beg += 1
        recur(out, n - 3, start_at=start_at + 3 * (n - 1), depth=depth + 1)
    answer = [0 for _ in range(tri_cnt(n))]
    recur(answer, n)
    return answer

def test(a, b):
    for i, (ae, be) in enumerate(zip(a, b)):
        if ae != be:
            print(f'diff at {i} , real = {ae}, expected = {be}')
    print("end")
print(solution(6))

test(solution(6), [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11])
