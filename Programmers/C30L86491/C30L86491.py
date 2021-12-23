# %%
def solution(sizes):
    cx, cy = 0, 0
    for x, y in sizes:
        nw, nh = cx < x, cy < y
        nwh = nw or nh
        rw, rh = cy < x, cx < y
        rwh = rw or rh
        if nwh and rwh:
            nx, ny = max(cx, x), max(cy, y)
            nsz = nx * ny
            rx, ry = max(cx, y), max(cy, x)
            rsz = rx * ry
            if nsz <= rsz:
                cx, cy = nx, ny
            else:
                cx, cy = rx, ry
    return cx * cy


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
