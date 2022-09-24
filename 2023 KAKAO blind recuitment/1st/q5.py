# %%


def solution(commands):
    def union(ufdt, a, b):
        a = find(ufdt, a)
        b = find(ufdt, b)
        ufdt[min(a, b)] = max(a, b)
    def find(ufdt, key):
        if key not in ufdt:
            ufdt[key] = key
        if key != ufdt[key]:
            ufdt[key] = find(ufdt, ufdt[key])
        return ufdt[key]
    def cellNo(r, c):
        return (c-1) + (r-1) * 50
    
    refs = {i: i for i in range(50 * 50)}
    vals = {i: "" for i in range(50 * 50)}
    output = []
    for cmd in commands:
        [op, *args] = cmd.split(" ")
        if op == "UPDATE" and len(args) == 2:
            # 값으로 업데이트
            for i in range(50 * 50):
                if vals[i] == args[0]:
                    vals[i] = args[1]
        elif op == "UPDATE" and len(args) == 3:
            # 위치로 업데이트
            vals[find(refs, cellNo(int(args[0]), int(args[1])))] = args[2]
        elif op == "MERGE":
            av = vals[find(refs, cellNo(int(args[0]), int(args[1])))]
            bv = vals[find(refs, cellNo(int(args[2]), int(args[3])))]
            nv = av if av != "" else bv if bv != "" else bv
            # 
            union(refs, cellNo(int(args[0]), int(args[1])), cellNo(int(args[2]), int(args[3])))
            vals[find(refs, cellNo(int(args[0]), int(args[1])))] = nv
        elif op == "UNMERGE":
            trgNo = find(refs, cellNo(int(args[0]), int(args[1])))
            pval = vals[trgNo]
            for k in range(50 * 50):
                if find(refs, k) == trgNo:
                    refs[k] = k
                    vals[k] = ""
            vals[find(refs, cellNo(int(args[0]), int(args[1])))] = pval
        elif op == "PRINT":
            if vals[find(refs, cellNo(int(args[0]), int(args[1])))] == "":
                output.append("EMPTY")
            else:
                output.append(vals[find(refs, cellNo(int(args[0]), int(args[1])))])
    return output


solution(["UPDATE 50 50 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", 
    "MERGE 1 3 1 2", "MERGE 1 4 1 2", 
    # "UPDATE 1 2 group1", 
    # "UPDATE 1 3 group2", 
    # "UPDATE 1 4 group3", 
    "UPDATE category hansik", 
    "UNMERGE 1 2", 
    "PRINT 1 2", 
    "PRINT 1 3", 
    "PRINT 50 50", 
    "PRINT 50 49", 
])
