# %%
import itertools as it
import datetime as tm


def solution(lines):
    answer = 0
    ise = sorted(
        it.chain(
            *map(
                lambda l: (
                    (start_at := (end_at := tm.timedelta(hours=int(l[11:13]), minutes=int(l[14:16]),
                                                         seconds=int(l[17:19]), milliseconds=int(l[20:23]))
                                  ) - tm.timedelta(seconds=float(l[24:-1]) - 0.001), 1),
                    (end_at, -1),
                ),
                lines
            )
        ),
        key=lambda tp: (
            tp[0] - tm.timedelta(milliseconds=999), -2) if tp[1] == 1 else tp,

    )
    #
    trf = 0
    for t, dtrafic in ise:
        trf += dtrafic
        if dtrafic == 1:
            print(f'[{str(t):20}:{"":20}] = {trf}')
            answer = max(answer, trf)
        elif dtrafic == -1:
            print(f'[{"":20}:{str(t):20}] = {trf}')
        else:
            print(
                f'[???] = {t}, {dtrafic}')
            pass
    return answer


test_cases = [
    (
        ([
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"],
         ),
        1
    ),
    # (
    #     ([
    #         "2016-09-15 00:00:01.999 2.0s",
    #         "2016-09-15 01:00:07.000 2s"],
    #      ),
    #     1
    # ),
    # (
    #     ([
    #         "2016-09-15 01:00:04.001 2.0s",
    #         "2016-09-15 01:00:07.000 2s"],
    #      ),
    #     1
    # ),
    # (
    #     ([
    #         "2016-09-15 01:00:04.002 2.0s",
    #         "2016-09-15 01:00:07.000 2s"
    #     ],),
    #     2
    # ),
    # (
    #     ([
    #         "2016-09-15 20:59:57.421 0.351s",
    #         "2016-09-15 20:59:58.233 1.181s",
    #         "2016-09-15 20:59:58.299 0.8s",
    #         "2016-09-15 20:59:58.688 1.041s",
    #         "2016-09-15 20:59:59.591 1.412s",
    #         "2016-09-15 21:00:00.464 1.466s",
    #         "2016-09-15 21:00:00.741 1.581s",
    #         "2016-09-15 21:00:00.748 2.31s",
    #         "2016-09-15 21:00:00.966 0.381s",
    #         "2016-09-15 21:00:02.066 2.62s"
    #     ],),
    #     7
    # )


]
for tc in test_cases:
    print(
        f'{f"solution{tc[0]}":40}, real = {solution(*tc[0]):6}, expected = {tc[1]:6}')
