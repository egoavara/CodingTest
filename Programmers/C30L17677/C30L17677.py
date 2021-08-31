# %%
import itertools as it
from collections import Counter


def solution(str1, str2):
    cs1 = Counter((str.lower(s1) for i in range(len(str1) - 1)
                   if str.isalpha(s1 := str1[i:i+2])))
    cs2 = Counter((str.lower(s2) for i in range(len(str2) - 1)
                   if str.isalpha(s2 := str2[i:i+2])))
    union = {k: max(cs1[k], cs2[k]) for k in it.chain(cs1.keys(), cs2.keys())}
    inter = {k: min(cs1[k], cs2[k]) for k in it.chain(cs1.keys(), cs2.keys())}
    return int((sum(inter.values()) / sum_union
                if (sum_union := sum(union.values())) > 0 else 1) * 65536)


# print(solution("FRANCE", "french"))
# print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("aaaa+bbb", "aaa+bbbb"))
# print(solution("E=M*C^2", "e=m*c^2"))
# %%
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    a,b=[],[]
    t,p=1,1
    for i in range(len(str1)-1):
        if((str1[i]+str1[i+1]).isalpha()==True):
            a.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if((str2[i]+str2[i+1]).isalpha()==True):
            b.append(str2[i]+str2[i+1])
    for i in range(len(a)):
        if(a.count(a[i])>1):
            a[i]=a[i]+('@'*t)
            t+=1
    for j in range(len(b)):
        if(b.count(b[j])>1):
            b[j]=b[j]+('@'*p)
            p+=1
    a=set(a)
    b=set(b)
    union=len(a&b)
    combine=len(a|b)
    print(a, b)
    if(combine==0):
        return 65536
    return int((union/combine)*65536)
print(solution("aa+aa+bb+bb", "AAAA+BBBB"))