# %% API 정의 블록
# 2022 KAKAO blind recuitment 2nd
# 접속을 위한 API 리스트 정의
# 
# # 내장 라이브러리
# - json        : JSON 데이터 처리
# - dataclass   : 클래스 정의를 보기 좋게 하기 위함
# 
# # 외부 라이브러리 이용
# - requests    : https://docs.python-requests.org/en/latest/  : HTTP 라이브러리, RESTful API 호출을 위해 호출
# - numpy       : https://numpy.org/                           : 선형대수 라이브러리, 배열을 다루기 위해 이용
# 
# 
# 문제 선택은
# `pno : 1|2` 변수를 이용해 진행합니다.
import requests as req
import numpy as np
import json
from dataclasses import dataclass


class API:
    X_AUTH_TOKEN = "ec927316f01bd2b363fc9a6b6b242851"
    BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

    @dataclass
    class Instance:
        auth_key: str
        problem: int
        time: int
        status: str

        def waiting_line(self):
            # -> [{"id": 고유계정, "from": 매칭 시작 시간}, ...]
            res = req.get(
                f'{API.BASE_URL}/waiting_line',
                headers={
                    'Authorization': self.auth_key,
                    'Content-Type': 'application/json',
                }
            ).json()
            return res['waiting_line']

        def game_result(self):
            # -> [{"win": 이긴유저, "lose": 진유저, "taken": 게임시간 }, ...]
            res = req.get(
                f'{API.BASE_URL}/game_result',
                headers={
                    'Authorization': self.auth_key,
                    'Content-Type': 'application/json',
                }
            ).json()
            return res['game_result']

        def user_info(self):
            # -> [{ "id": 유저, "grade": 등급 }, ...]
            res = req.get(
                f'{API.BASE_URL}/user_info',
                headers={
                    'Authorization': self.auth_key,
                    'Content-Type': 'application/json',
                }
            ).json()
            return res['user_info']

        def matching(self, matching_list):
            # matching_list : [[매칭유저1, 매칭유저2], ...]
            res = req.put(
                f'{API.BASE_URL}/match',
                data=json.dumps({
                    'pairs': matching_list
                }),
                headers={
                    'Authorization': self.auth_key,
                    'Content-Type': 'application/json',
                }
            ).json()
            self.status = res['status']
            self.time = res['time']

        def change_grade(self, idsets):
            # idsets : [{ "id": 유저, "grade": 등급 }, ...]
            res = req.put(
                f'{API.BASE_URL}/change_grade',
                data=json.dumps({
                    'commands': idsets
                }),
                headers={
                    'Authorization': self.auth_key,
                    'Content-Type': 'application/json',
                }
            ).json()
            self.status = res['status']

        def score(self):
            # -> {
            #       "status": "finished",
            #       "efficiency_score": -1.0,
            #       "accuracy_score1": 0.0,
            #       "accuracy_score2": 32.62,
            #       "accuracy_score2": 32.62,
            #       "score": 30.94
            # }
            res = req.get(
                f'{API.BASE_URL}/score',
                headers={
                    'Authorization': self.auth_key,
                    'Content-Type': 'application/json',
                }
            ).json()
            return res

    @classmethod
    def start(cls, pno):
        res = req.post(
            f'{API.BASE_URL}/start',
            data=json.dumps({
                'problem': pno,
            }),
            headers={
                'X-Auth-Token': API.X_AUTH_TOKEN,
                'Content-Type': 'application/json',
            }
        ).json()
        return API.Instance(res['auth_key'], res['problem'], res['time'], 'ready')

@dataclass
class UserStat:
    average : float
    std : float
    min : float
    max : float
# %% 1번 문제
#
# 그냥 계속 레이팅 변경 없이 계속 진행한 결과
# {'status': 'finished', 'efficiency_score': '99.8801', 'accuracy_score1': '9.5556', 'accuracy_score2': '42.7034', 'score': '142.6148'}
#
# 1차 시도 성적
# UPSCORE = 20, 100, DOWNSCORE = 15, 65, ATHRES = 1000
# {'status': 'finished', 'efficiency_score': '1.4242', 'accuracy_score1': '60.8889', 'accuracy_score2': '61.6776', 'score': '148.2192'}
#
# 2차 시도 성적
# UPSCORE = 20, 100, DOWNSCORE = 15, 65, ATHRES = 15000
# {'status': 'finished', 'efficiency_score': '-42.5688', 'accuracy_score1': '65.7778', 'accuracy_score2': '61.8109', 'score': '119.0513'}
#
# 3차 시도 성적
# UPSCORE = 20, 100, DOWNSCORE = 15, 65, ATHRES = 5000, BASE_C = 7, DT_C = 1.5
# {'status': 'finished', 'efficiency_score': '-74.4343', 'accuracy_score1': '56.6667', 'accuracy_score2': '64.0161', 'score': '85.2719'}
#
# 4차 시도
# UPSCORE = 20, 100, DOWNSCORE = 15, 65, ATHRES = 5000, BASE_C = 30, DT_C = 7
# {'status': 'finished', 'efficiency_score': '80.2993', 'accuracy_score1': '69.1111', 'accuracy_score2': '57.8889', 'score': '216.6394'}
#
# 5차 시도
# UPSCORE = 20, 100, DOWNSCORE = 15, 65, ATHRES = 5000, BASE_C = 30, DT_C = 7
# MAX_WAITTIME 도입 = 40
# {'status': 'finished', 'efficiency_score': '80.2993', 'accuracy_score1': '69.1111', 'accuracy_score2': '57.8889', 'score': '216.6394'}
# 도입 효과는 없는 것 같지만 일단 유지
#
# 6차 시도
# # 아마 너무 랭크 오르는 속도가 느린 것으로 추정 가장 높은 랭크 유저가 1000점대도 못넘는 것 같음.
# # 더 점수 상승폭을 증가시켜야 함
# UPSCORE = 50, 400, DOWNSCORE = 30, 250, ATHRES = 5000, BASE_C = 30, DT_C = 7
# MAX_WAITTIME = 60
# {'status': 'finished', 'efficiency_score': '45.9556', 'accuracy_score1': '63.5556', 'accuracy_score2': '61.4671', 'score': '186.7916'}
#
# 7차 시도
# # 효율성 점수가 많이 떨어짐...MAXTIME 조정
# UPSCORE = 50, 400, DOWNSCORE = 30, 250, ATHRES = 15000, BASE_C = 60, DT_C = 10
# MAX_WAITTIME = 30
# {'status': 'finished', 'efficiency_score': '45.9556', 'accuracy_score1': '63.5556', 'accuracy_score2': '61.4671', 'score': '186.7916'}
#
# 8차 시도
# UPSCORE = 40, 320, DOWNSCORE = 30, 180, BASE_C = 60, DT_C = 10
# ATHRES = 20000
# MAX_WAITTIME = 30
# MODIFIER_FACTOR = [4, 6]
# # 모디파이어 팩터 추가, 레이팅 편차와 경기 시간을 종합해서 매칭 적용
# {'status': 'finished', 'efficiency_score': '60.8811', 'accuracy_score1': '70.4444', 'accuracy_score2': '63.8823', 'score': '209.8969'}
#
# 9차 시도
# UPSCORE = 40, 120, DOWNSCORE = 30, 70, BASE_C = 60, DT_C = 10
# ATHRES = 20000
# MAX_WAITTIME = 30
# MODIFIER_FACTOR = [4, 6]
# HARDER_RESULT = 90, 120
# # 레이팅이 더 낮은 사람의 승리에 가산점 추가
# {'status': 'finished', 'efficiency_score': '44.4444', 'accuracy_score1': '64.0', 'accuracy_score2': '56.1178', 'score': '179.697'}
#
# 10차 시도
# UPSCORE = 40, 120, DOWNSCORE = 30, 70, BASE_C = 60, DT_C = 10
# ATHRES = 20000
# MAX_WAITTIME = 30
# MODIFIER_FACTOR = [4, 6]
# HARDER_RESULT = 90, 120
# # 어려운 승리 보상 방법 변화
# {'status': 'finished', 'efficiency_score': '35.6879', 'accuracy_score1': '72.6667', 'accuracy_score2': '66.3195', 'score': '195.3338'}
#
# 11차 시도
# UPSCORE = 40, 120, DOWNSCORE = 30, 70
# BASE_C = 80, DT_C = 13, MAX_WAITTIME = 20
# MODIFIER_FACTOR = [4, 6]
# HARDER_RESULT = 90, 120
# # 매칭 최대 대기시간을 확 줄이고 시간에 따른 매칭 범위 확장과 기본 범위를 확대
# {'status': 'finished', 'efficiency_score': '85.6389', 'accuracy_score1': '63.7778', 'accuracy_score2': '61.705', 'score': '219.0904'}
#
# 12차 시도
# UPSCORE = 60, 120, DOWNSCORE = 50, 70
# BASE_C = 80, DT_C = 13, MAX_WAITTIME = 20
# MODIFIER_FACTOR = [4, 6]
# HARDER_RESULT = 90, 120
# # 기본 레이팅 보상 점수 확대
# {'status': 'finished', 'efficiency_score': '79.4744', 'accuracy_score1': '47.3333', 'accuracy_score2': '61.4153', 'score': '194.0779'}
#
# 13차 시도
# UPSCORE = 40, 80, DOWNSCORE = 30, 50
# BASE_C = 80, DT_C = 13, MAX_WAITTIME = 20
# MODIFIER_FACTOR = [4, 6]
# HARDER_RESULT = 90, 120
# # 기본 레이팅 보상 편차 축소
# {'status': 'finished', 'efficiency_score': '82.7709', 'accuracy_score1': '69.5556', 'accuracy_score2': '61.8487', 'score': '223.9018'}
#
# 14차 시도
# UPSCORE = 40, 80, DOWNSCORE = 30, 50
# BASE_C = 80, DT_C = 13, MAX_WAITTIME = 25
# MODIFIER_FACTOR = [4, 6]
# HARDER_RESULT = 90, 120
# # 최대대기시간 25분 확대
# {'status': 'finished', 'efficiency_score': '83.7311', 'accuracy_score1': '60.6667', 'accuracy_score2': '60.0198', 'score': '211.8087'}
# 
# 14차 시도 롤백

# %% 2번 문제
# 1차 시도
# # 어뷰징 방지 없음
# {'status': 'finished', 'efficiency_score': '98.7052', 'accuracy_score1': '51.802', 'accuracy_score2': '57.2738', 'score': '209.8551'}
# 2차 시도
# # 어뷰징 방지용 패배 초과점수 만회 API가 포함됨
# {'status': 'finished', 'efficiency_score': '97.0077', 'accuracy_score1': '50.7442', 'accuracy_score2': '57.4162', 'score': '207.3986'}
# 3차 시도
# # 기록 기반 어뷰징 확인
# {'status': 'finished', 'efficiency_score': '99.1159', 'accuracy_score1': '52.8827', 'accuracy_score2': '56.9199', 'score': '211.0558'}





# %% 실행블록
# 상수 정의
GAME_MIN_T = 3
GAME_MAX_T = 40
GRADE_MIN = 0
GRADE_MAX = 9999
ADIFF_MIN = 1
ADIFF_MAX = 99000
ABUSER_GAMETIME_MAX = 10
# 조정값 정의
BASE_C = 80  # 기본적 매칭 레이팅 오차범위
DT_C = 13  # 시간 오차에 따른 매칭범위 확장
BASE_UPSCORE = 60
BASE_UPSCORE_ADVANTAGE = 80
BASE_DOWNSCORE = 50
BASE_DOWNSCORE_ADVANTAGE = 50
HARDER_RESULT_ADVANTAGE = 110
MAX_WAITTIME = 20
MODIFIER_FACTORS = [4, 6]  # TIME, RATING
ABUSER_PERNISHMENT = 75
ABUSER_CNT_THERES = 5
# 유도값
MODIFIER_TIME_FACTORS = MODIFIER_FACTORS[0] / sum(MODIFIER_FACTORS)
MODIFIER_RATING_FACTORS = MODIFIER_FACTORS[1] / sum(MODIFIER_FACTORS)
# ################################### #
# API 연결 : 여기서 문제를 선택
# pno = 1 | 2, 문제 선택
pno = 1
instance = API.start(pno)
# 통계측정용 변수
stat_loop = 0
stat_result_recv = 0
stat_match_send = 0
stat_mreq_recv = 0
# 
abuser_db_cnt = {}
abuser_db_val = {}

def check_intersect(a, b):
    amin, amax = a
    bmin, bmax = b
    adiff = amax - amin
    bdiff = bmax - bmin
    if adiff > bdiff and amin <= bmin and bmax <= amax:
        return True
    if adiff < bdiff and bmin <= amin and amax <= bmax:
        return True
    if bmin <= amax and bmax >= amin:
        return True
    if amin <= bmax and amax >= bmin:
        return True
    return False


def intersect_space(a, b):
    amin, amax = a
    bmin, bmax = b
    adiff = amax - amin
    bdiff = bmax - bmin
    if adiff > bdiff and amin <= bmin and bmax <= amax:
        return bdiff
    if adiff < bdiff and bmin <= amin and amax <= bmax:
        return adiff
    if bmin <= amax and bmax >= amin:
        return bmax - amin
    if amin <= bmax and amax >= bmin:
        return amax - bmin
    return 0

# 게임 결과 분석
def game_result_calc(gr, users, user_stat:UserStat):
    changings = []
    for gresult in gr:
        taken = gresult['taken']
        who_win = gresult['win']
        who_lose = gresult['lose']
        # e는 알수 없으니 무시
        # 실력 차이는 1 ~ 99000 !같은 실력은 없음
        abil_diff = (GAME_MAX_T - taken) / 35 * 99000
        abil_diff = min(max(abil_diff, ADIFF_MIN), ADIFF_MAX)
        # 기본적인 레이팅 변환 장치
        nwing = users[who_win]
        nloseg = users[who_lose]
        modifier_time = (abil_diff/ADIFF_MAX)
        modifier_rating = (abs(nwing - nloseg) /
                           user_stat.std) if user_stat.std > 1 else 1
        modifier = min(modifier_time * MODIFIER_TIME_FACTORS +
                       modifier_rating * MODIFIER_RATING_FACTORS, 1)
        nwing += BASE_UPSCORE + BASE_UPSCORE_ADVANTAGE * modifier
        nloseg -= BASE_DOWNSCORE + BASE_DOWNSCORE_ADVANTAGE * modifier
        # 어려운 승리
        if users[who_win] < users[who_lose]:
            nwing += HARDER_RESULT_ADVANTAGE * modifier_rating
        # 어뷰져 탐색
        if pno == 2:
            # 어뷰저의 게임 시간은 10분 내이다
            if taken <= ABUSER_GAMETIME_MAX :
                # 진 쪽이 어뷰저인지 확인해야 함
                # 레이팅이 비교적 정확하다고 가정하고 확인
                if users[who_lose] > users[who_win]:
                    # 진쪽이 레이팅이 높다면 어뷰저인지 확인해야 함
                    if modifier_rating > 0.03:
                        if who_lose not in abuser_db_cnt:
                            abuser_db_cnt[who_lose] = 0
                            abuser_db_val[who_lose] = 0
                        abuser_db_cnt[who_lose] += 1
                        abuser_db_val[who_lose] += modifier_rating
                    if who_lose in abuser_db_cnt and abuser_db_cnt[who_lose] >= ABUSER_CNT_THERES:
                        arate = abuser_db_val[who_lose] / abuser_db_cnt[who_lose]
                        nloseg += ABUSER_PERNISHMENT * arate ** 2
        # 
        nwing = max(min(nwing, GRADE_MAX), GRADE_MIN)
        nloseg = max(min(nloseg, GRADE_MAX), GRADE_MIN)
        # 레이팅 변동사항 전달
        changings.append({
            "id": who_win,
            "grade": int(nwing),
        })
        changings.append({
            "id": who_lose,
            "grade": int(nloseg),
        })
    return changings

def matching_calc(waits, users, user_stat):
    matching_send = []
    temporal_grade = {}
    for id in users:
        # 일시적으로 사용되는 사용자 점수의 범위,
        # 기본적으로 오래 기달린 경우 점수 범위를 점점 늘린다.
        # BASE_C를 통해 정확히 일치하는 점수만 매칭되는 일을 피하게 만든다.
        tdelta = DT_C * (waits[id] if id in waits else 0)
        temporal_grade[id] = (users[id] - tdelta - BASE_C,
                              users[id] + tdelta + BASE_C)
    # 큐에서 오래 기다린 순서대로 정렬
    temporal_queue = sorted(waits.keys(), key=lambda id: waits[id])
    while len(temporal_queue) >= 2:
        # 큐에서 매칭을 고를 사람을 고른다.
        champion = temporal_queue.pop(0)
        chalenger = None
        #
        if waits[champion] >= MAX_WAITTIME:
            # 너무 오래 기다린 경우 매칭 점수에서 가장 가까운 상대를 대상으로 바로 진행
            chalenger = min(temporal_queue, key=lambda e: abs(
                users[champion] - users[e]))
        else:
            avilable_chalengers = [(id, sp) for id in temporal_queue if (
                sp := intersect_space(temporal_grade[champion], temporal_grade[id])) > 0]
            if len(avilable_chalengers) == 0:
                continue
            chalenger, _ = max(
                avilable_chalengers, key=lambda e: e[1])
        # 도전자를 찾아낸 경우 큐에서 도전자 제거후 반복
        if chalenger is not None:
            temporal_queue.remove(chalenger)
            matching_send.append([champion, chalenger])
    return matching_send

# 주 매칭 루프
while instance.status == 'ready':
    # 유저 정보를 dict 형태로 변형
    users = {dat['id']: dat['grade'] for dat in instance.user_info()}
    grades = list(users.values())
    # 유저들의 성적을 분석함
    user_stat = UserStat(
        np.average(grades),
        np.std(grades),
        np.min(grades),
        np.max(grades),
    )
    # 디버깅
    if stat_loop % 30 == 0:
        print(f"> {stat_loop}번째 작업")
        print(
            f">> 매칭<요청/승인/결과> {stat_mreq_recv}/{stat_match_send}/{stat_result_recv} 회")
        print(f">> 레이팅 : 평균 = {user_stat.average:.4f}, 표준편차 = {user_stat.std:.4f}")
        print()
    # 게임 결과 분석
    gr = instance.game_result()
    if len(gr) != 0:
        stat_result_recv += len(gr)
        instance.change_grade(game_result_calc(gr, users, user_stat))
        # 매칭라인 정보를 dict형으로 변형
    waits = {dat['id']: instance.time - dat['from']
             for dat in instance.waiting_line()}
    stat_mreq_recv += len(waits)
    # 매치매이킹 설치
    matchmaking = matching_calc(waits, users, user_stat)
    #
    stat_loop += 1
    stat_match_send += len(matchmaking)
    instance.matching(matchmaking)
print("-- END -- ")
score = instance.score()
print(f"Score : {score}")
