# %%
def dayFrom(d):
    [y, m, d] = d.split(".")
    return int(y) * 28 * 12 + int(m) * 28 + int(d)

def termFrom(d):
    [t, d] = d.split(" ")
    return (t, int(d) * 28)

def validAt(terms, privacy):
    [startAt, t] = privacy.split(" ")
    return dayFrom(startAt) + terms[t]

def solution(today, terms, privacies):
    today = dayFrom(today)
    terms = {e[0]:e[1] for e in map(termFrom, terms)}
    privacies = [{"i":i+1, "v": validAt(terms, e)} for i, e in enumerate(privacies)]
    return list(map(lambda e : e["i"], filter(lambda e : e["v"] <= today,privacies)))

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
