# %%
def solution(scores):
    mapping = { 10 : 'A', 9 : 'A', 8 : 'B', 7 : 'C', 6 : 'D', 5 : 'D'}
    scores = [list(each) for each in zip(*scores)]
    for i in range(len(scores)):
        mx = max(scores[i])
        mn = min(scores[i])
        if sum(filter(lambda e : e == mx, scores[i])) == mx and mx == scores[i][i]:
            scores[i][i] = None    
        if sum(filter(lambda e : e == mn, scores[i])) == mn and mn == scores[i][i]:
            scores[i][i] = None    
    return "".join(
        mapping.setdefault(
            int((sum(_ for _ in each if _ is not None) / sum(1 for _ in each if _ is not None)) // 10),
            'F'
        ) for each in scores
    )


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
      47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
