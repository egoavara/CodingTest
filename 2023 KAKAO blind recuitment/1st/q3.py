# %%
import itertools as it

table = {40: 0.6, 30: 0.7, 20: 0.8, 10: 0.9}


def solution(users, emoticons):
    maxPlus = -1
    maxTotal = -1
    for case in it.product(*[[10, 20, 30, 40]] * len(emoticons)):
        emots = [(emo, disc, emo * table[disc]) for emo, disc in zip(emoticons, case)]
        # 
        casePlus =0
        caseTotal =0
        for user in users:
            totalPrice = sum(map(lambda e : e[2], filter(lambda e: e[1] >= user[0],emots)))
            if totalPrice >= user[1]:
                casePlus +=1
            else:
                caseTotal += totalPrice
        if maxPlus < casePlus:
            maxPlus = casePlus
            maxTotal = caseTotal
        if maxPlus == casePlus and maxTotal < caseTotal:
            maxPlus = casePlus
            maxTotal = caseTotal
    return [maxPlus, maxTotal]


solution([[40, 10000], [25, 10000]], [7000, 9000])
