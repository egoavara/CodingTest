# %%
def to_minute(a):
    hh, mm = a.split(":")
    return int(mm) + int(hh) * 60


def solution(fees, records):
    ENDTIME = to_minute('23:59')
    dt, dp, ut, up = fees

    def calc(v):
        return dp + max(((v - dt) + ut - 1) // ut, 0) * up
    #
    result = {}
    parking = {}
    for r in records:
        sat, who, inout = r.split(" ")
        at = to_minute(sat)
        print(f'{inout} : {who} : {at}')
        if inout == 'IN':
            parking[who] = at
        else:
            pat = parking.pop(who)
            result[who] = (result[who] if who in result else 0) + (at - pat)
    for who in parking:
        result[who] = (result[who] if who in result else 0) + \
            (ENDTIME - parking[who])
    #
    print(result)
    return [calc(result[who]) for who in sorted(result)]


# print(23 * 60 + 59, 18 +)
print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
     "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
     "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
