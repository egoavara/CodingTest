# %%


def solution(enroll, referral, seller, amount):
    tree = {
        '-': {
            'parent': None,
            'earn': 0,
            'children': []
        }
    }
    for enr, refer in zip(enroll, referral):
        tree[enr] = {
            'parent': refer,
            'earn': 0,
            'children': []
        }
    for k, v in tree.items():
        if v['parent'] != None:
            tree[v['parent']]['children'].append(k)
    # setup complete

    def calc(seller, amount):
        if tree[seller]['parent'] == None:
            tree[seller]['earn'] += amount
            return
        tree[seller]['earn'] += mine
        calc(tree[seller]['parent'], referers)
    for mem, earn in zip(seller, amount):
        me, pr = tree[mem], tree[mem]['parent']
        total = earn * 100
        while pr != None and total != 0:
            referers = total // 10
            mine = total - referers
            # 
            me['earn'] += mine
            me = tree[pr]
            pr = me['parent']
            # 
            total = referers
        me['earn'] += total

    answer = [tree[k]['earn'] for k in enroll]
    return answer


print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
))
