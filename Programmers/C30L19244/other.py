# %%
import string


def solution(record):
    answer = []
    d = {}  # user_id: nickname
    for r in record:
        command, uid, *nickname = r.split(' ')
        if command in {'Enter', 'Leave'}:
            if command == 'Enter':
                m = f'${{{uid}}}님이 들어왔습니다.'
            else:
                m = f'${{{uid}}}님이 나갔습니다.'
            answer.append(string.Template(m))
        if command in {'Enter', 'Change'}:
            d[uid] = nickname[0]

    return [x.substitute(d) for x in answer]


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan",  "Enter 0 FALSE "]))
