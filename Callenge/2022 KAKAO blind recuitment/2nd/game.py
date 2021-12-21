# %%
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

import more_itertools as mit
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers


class Game:
    def __init__(self, reals: "np.ndarray[1, np.int32]") -> None:
        self.reals: "np.ndarray[1, np.int32]" = reals
        self.users: "np.ndarray[1, np.float32]" = np.ones(
            reals.shape[0], np.float32)
        self._waits: Dict[int, int] = {}
        self.hist: List[int] = []
        self.ingame: Dict[int, List[Tuple[int, int]]] = {}
        self.tstamp: int = -1

    @classmethod
    def generate(cls, size: int) -> "Game":
        return Game(np.random.choice(9999, size, replace=True) + 1)

    def setupWaits(self, howmany: Union[int, float]):
        howmany = howmany if isinstance(howmany, int) \
            else int(np.ceil(np.clip(howmany, 0., 1.) * self.reals.shape[0]))

        availables = set(range(self.reals.shape[0])) - self._waits.keys()
        chosens = np.random.choice(list(availables), min(
            howmany, len(availables)), replace=False)
        self._waits |= {c: self.tstamp for c in chosens}

    def appendQueue(self, a: int, b: int) -> bool:
        if a in self._waits and b in self._waits:
            self.hist.append(self.tstamp - self._waits[a])
            self.hist.append(self.tstamp - self._waits[b])
            del self._waits[a], self._waits[b]
            t = Game.newtime(self.reals[a], self.reals[b])
            self.ingame[self.tstamp + t] = [*
                                            self.ingame[self.tstamp + t], (a, b)]
            return True
        return False

    @classmethod
    def newtime(cls, ascore: int, bscore: int) -> int:
        r = min(max(np.random.normal(scale=0.4) + 2, 0), 4) / 4
        t = 20 + 5 * r + 35 * (abs(ascore - bscore) / 10000)
        return min(max(t, 20), 60)

    def waits(self) -> List[Tuple[int, int]]:
        return [(k, self.tstamp - v) for k, v in self._waits.items()]
    # 순서점수, 실력점수, 효율성 점수

    def scoring(self) -> Tuple[float, float, float]:
        DIFF = 3775 - 100  # sum(range(100)) - sum(range(50)) - 100
        r0 = list(map(lambda e: e[0][0], sorted(
            np.ndenumerate(self.reals), key=lambda e: e[1])))
        r1 = list(map(lambda e: e[0][0], sorted(
            np.ndenumerate(self.users), key=lambda e: e[1])))
        rs = sum(map(lambda e: abs(e[0] - e[1]), zip(r0, r1)))
        order_score = np.clip((1 - rs / DIFF), 0, 1) * 100
        #
        RSCORE = self.reals / np.average(self.reals)
        USCORE = self.users / np.average(self.users)
        D = RSCORE / USCORE
        return (order_score,
                np.round(np.clip(100 - np.sum(np.abs(D - 1)) * 2, 0, 100), 4),
                max(100. - np.average(self.hist) if self.hist else 0, 0))

    def results(self) -> List[Tuple[int, int, int]]:
        self.tstamp += 1
        self.setupWaits((np.random.rand() ** 4 / 5))
        return [(a, b, self.tstamp) for a, b in self.ingame[self.tstamp]] if self.tstamp in self.ingame else []

    def next(self) -> bool:
        if self.tstamp > 2400:
            return False
        self.tstamp += 1
        self.setupWaits((np.random.rand() ** 4 / 5))
        return True


@dataclass
class Params:
    BASE_C: float = 80  # 기본적 매칭 레이팅 오차범위
    DT_C: float = 13  # 시간 오차에 따른 매칭범위 확장
    BASE_UPSCORE: float = 60
    BASE_UPSCORE_ADVANTAGE: float = 80
    BASE_DOWNSCORE: float = 50
    BASE_DOWNSCORE_ADVANTAGE: float = 50
    HARDER_RESULT_ADVANTAGE: float = 110
    MAX_WAITTIME: float = 20
    MODIFIER_FACTORS: List[float] = field(default_factory=lambda: [4, 6])
    ABUSER_PERNISHMENT: float = 75
    ABUSER_CNT_THERES: float = 5


game = Game.generate(100)
while game.next():
    n = game.results()
    w = game.waits()
print(game.tstamp)


# # %%
waiting_model = keras.Sequential([
    layers.InputLayer((32, 2)),
    layers.Conv1D(32, 2, padding='same'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(32 ** 2, activation='softmax'),
    layers.Reshape((32, 32)),
])
waiting_model.summary()
# %%
opti = keras.optimizers.RMSprop()

# # %%
# batchsize = 100000
# reals = np.random.random(size=(batchsize, 2))
# users = np.random.random(size=(batchsize, 2)) * reals
# times = np.vectorize(lambda ab: Game.newtime(
#     ab[0] * 10000, ab[1] * 10000), signature='(n)->()')(reals).reshape((batchsize, 1))
# resus = np.hstack([users, times])
# print("Complete")

# score_model = keras.Sequential([
#     layers.InputLayer((3,)),
#     layers.Dense(16, activation='relu'),
#     layers.Dense(16, activation='relu'),
#     layers.Dense(16, activation='relu'),
#     layers.Dense(16, activation='relu'),
#     layers.Dense(2, activation='softmax'),
# ], name='Scoring-Model')
# score_model.summary()
# score_model.compile(loss='mse')
# score_model.fit(resus, reals)
# # %%
# batchsize = 10
# reals = np.random.random(size=(batchsize, 2))
# users = np.random.random(size=(batchsize, 2)) * reals
# times = np.vectorize(lambda ab: Game.newtime(
#     ab[0] * 10000, ab[1] * 10000), signature='(n)->()')(reals).reshape((batchsize, 1))
# resus = np.hstack([users, times])
# predict = score_model.predict(resus)
# #
# reals = np.floor(reals * 10000)
# users = np.floor(users * 10000)
# predict = np.floor(predict * 10000)

# print(f'Real : User : Predict')
# print(np.hstack([reals, users, predict]))

# # %%
# rs = np.array([8657., 2211.])
# ds = np.array([591.,  999.])
