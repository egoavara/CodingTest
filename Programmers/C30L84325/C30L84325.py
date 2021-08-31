# %%

def solution(table, languages, preference):
    table = {(ts := t.split(" "))[0]: ts[1:] for t in table}
    preference = {l: p for l, p in zip(languages, preference)}
    return max(
        map(
            lambda kl:
            (
                kl[0],
                sum(map(lambda ir: (
                    5-ir[0]) * preference.get(ir[1], 0), enumerate(kl[1])))
            ),
            sorted(table.items(), key=lambda kv:kv[0])
        ),
        key=lambda ns: ns[1]
    )[0]


print(solution([
    "SI JAVA JAVASCRIPT SQL PYTHON C#",
    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
    "GAME C++ C# JAVASCRIPT C JAVA"],
    ["PYTHON", "C++", "SQL"],
    [7, 5, 5]
))
