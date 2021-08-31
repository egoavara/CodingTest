def solution(record):
    namemap = {args[0] : args[1] for [op, *args] in map(lambda e : e.split(), record) if op != 'Leave'}
    return [
        (f'{namemap[args[0]]}님이 들어왔습니다.' if op == 'Enter' else f'{namemap[args[0]]}님이 나갔습니다.')
        for [op, *args] in map(lambda e : e.split(), record) if op != 'Change'
    ]