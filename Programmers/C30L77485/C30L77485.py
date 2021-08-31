# %%

def rotate(aar, aac, bbr, bbc, arr):
    w = max(aac, bbc) - min(aac, bbc) + 1
    h = max(aar, bbr) - min(aar, bbr) + 1
    m = arr[aar][aac]
    #
    last = arr[aar][aac + w-1]
    for x in range(w - 1):
        m = min(m, arr[aar][aac + w - 1 - x - 1])
        arr[aar][aac + w - 1 - x] = arr[aar][aac + w - 1 - x - 1]
    #
    tlast = arr[aar + h - 1][aac + w-1]
    for y in range(0, h - 2):
        m = min(m, arr[aar + h - 1 - y - 1][aac + w-1])
        arr[aar + h - 1 - y][aac + w-1] = arr[aar + h - 1 - y - 1][aac + w-1]
    m = min(m, last)
    arr[aar + 1][aac + w-1] = last
    last = tlast
    #
    tlast = arr[aar + h - 1][aac]
    for x in range(0, w - 2):
        m = min(m, arr[aar + h - 1][aac + x+1])
        arr[aar + h - 1][aac + x] = arr[aar + h - 1][aac + x+1]
    m = min(m, last)
    arr[aar + h - 1][aac + w-1 - 1] = last
    last = tlast
    #
    for y in range(0, h - 2):
        m = min(m, arr[aar + y + 1][aac])
        arr[aar + y][aac] = arr[aar + y + 1][aac]
    m = min(m, last)
    arr[aar + h - 1 - 1][aac] = last
    return m


def solution(rows, columns, queries):
    arr = [[1 + x + y * columns for x in range(columns)] for y in range(rows)]
    return [rotate(fx-1, fy-1, tx-1, ty-1, arr) for (fx, fy, tx, ty) in queries]


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	))
print(solution(100, 97, [[1,1,100,97]]))
