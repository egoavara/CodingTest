# %%
import math
import requests as req
import numpy as np
import json

# %%


def rfrom_id(n, id):
    x = id//n
    y = id % n
    return (n - y - 1, x)


with open("./problem1_day-1.json") as fp1d1, open("./problem1_day-2.json") as fp1d2, open("./problem1_day-3.json") as fp1d3:
    p1d1 = json.load(fp1d1)
    p1d2 = json.load(fp1d2)
    p1d3 = json.load(fp1d3)
    out_stats = np.zeros((5, 5))
    in_stats = np.zeros((5, 5))
    for dat in [p1d1, p1d2, p1d3]:
        for k, v in dat.items():
            for borrow_from, return_at, _ in v:
                out_stats[rfrom_id(5, borrow_from)] += 1
                in_stats[rfrom_id(5, return_at)] += 1
    print(out_stats)
    print(in_stats)
    diff_stats = out_stats - in_stats
    diff_mean = np.mean(diff_stats)
    diff_min = np.min(diff_stats)
    diff_max = np.max(diff_stats)
    desire = np.vectorize(lambda x: 2+2.7*(x - diff_min) /
                          (diff_max - diff_min))(diff_stats)
    print(desire)
    idesire = np.ceil(desire)
    print(idesire)
    print(np.sum(idesire))
    
# %%
class API:
    BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    Ns = {1: 5, 2: 60}
    TRUCKs = {1: 5, 2: 10}

    class Instance:

        def from_id(self, id):
            x = id//self.n
            y = id % self.n
            return (self.n - y - 1, x)

        def __init__(self, akey, pno, t):
            self.akey = akey
            self.pno = pno
            self.n = API.Ns[pno]
            #
            self.status = "init"
            self.t = t
            self.failed = 0
            self.distance = 0
            #
            self.storage = np.full((self.n, self.n), -1)
            self.trucks = np.full((API.TRUCKs[pno], 2), -1)
            #
            self.sync_storage()
            self.sync_trucks()

        def sync_storage(self):
            resj = req.get(
                f"{API.BASE_URL}/locations/",
                headers={
                    'Authorization': self.akey,
                    "Content-Type": "application/json"
                }
            ).json()

            for v in resj['locations']:
                rloc = self.from_id(v['id'])
                self.storage[rloc] = v['located_bikes_count']

        def sync_trucks(self):
            resj = req.get(
                f"{API.BASE_URL}/trucks/",
                headers={
                    'Authorization': self.akey,
                    "Content-Type": "application/json"
                }
            ).json()

            for v in resj['trucks']:
                self.trucks[v['id'], :] = (
                    v['location_id'], v['loaded_bikes_count'])

        def simulate(self, **kwargs):
            payload = {
                "commands": [
                    {
                        'truck_id': k,
                        'command': v
                    }
                    for k, v in kwargs.items()
                ]
            }
            resj = req.put(
                f"{API.BASE_URL}/simulate/",
                data=json.dumps(payload),
                headers={
                    'Authorization': self.akey,
                    "Content-Type": "application/json"
                }
            ).json()
            self.status = resj['status']
            self.t = resj['time']
            self.failed = resj['failed_requests_count']
            self.distance = resj['distance']

        def is_finished(self):
            return self.status == 'finished'

        def score(self, end_to_no_work=False):
            if not self.is_finished() and not end_to_no_work:
                return None
            i = 0
            while not self.is_finished():
                i += 1
                print(f"NO WORK SIM : {i:3}")
                self.simulate()
            return req.get(
                f'{API.BASE_URL}/score',
                headers={
                    'Authorization': self.akey,
                    "Content-Type": "application/json"
                }
            ).json()['score']

    @ classmethod
    def start(cls, pno) -> Instance:
        res = req.post(
            f'{API.BASE_URL}/start',
            data=json.dumps({"problem": pno}),
            headers={
                "X-Auth-Token": "e00d595ccd98662a6dfcdd62621eae39",
                "Content-Type": "application/json"
            }).json()
        return API.Instance(res['auth_key'], res['problem'], res['time'])


# %%
MOVE_LEFT = 1
MOVE_TOP = 2
MOVE_RIGHT = 3
MOVE_BOTTOM = 4
LOAD = 5
UNLOAD = 6


def way(lfrom, lto):
    fy, fx = lfrom
    ty, tx = lto
    dx = tx - fx
    dy = ty - fy
    return [MOVE_RIGHT if dx > 0 else MOVE_LEFT] * abs(dx) + [MOVE_BOTTOM if dy > 0 else MOVE_TOP]*abs(dy)


def dist(tructdat, dst_loc, dst_load, mv):
    cmds, src_r, src_c, loaded, reserved = tructdat
    action_cnt = 10 - len(cmds)
    available_load = loaded - reserved
    dst_r, dst_c = dst_loc
    if available_load >= dst_load:
        return (abs(src_c - dst_c) + abs(src_r - dst_r), way((src_r, src_c), (dst_c, dst_c)), [])
    mn_r, mx_r = min(src_r, dst_r), max(src_r, dst_r)
    mn_c, mx_c = min(src_c, dst_c), max(src_c, dst_c)
    wind = mv[mn_r:mx_r + 1, mn_c:mx_c+1]
    loc = np.unravel_index(np.argmin(wind, axis=None), wind.shape)
    if wind[loc] >= 0:
        return (math.inf, 0, [])
    # 
    distance = abs(src_c - dst_c)+ abs(src_r - dst_r)
    loading = min(dst_load - available_load, -wind[loc], (action_cnt - distance) //2)
    unloading = min(loading + available_load, dst_load, action_cnt - distance - loading)
    if unloading > 0:
        return (
            distance + loading + unloading,
            way((src_r, src_c), loc) + [LOAD]*loading +
            way(loc, (dst_c, dst_c)) + [UNLOAD]*unloading,
            [((mn_r+loc[0], mn_c + loc[1]), loading)],
            [((mn_r+loc[0], mn_c + loc[1]), loading)]
        )
    else:
        return (
            math.inf
        )


test = np.array([
    [1, 4, 0, 0, 0],
    [0, 0, 0, -1, 0],
    [1, 1, 0, -1, 0],
    [-4, 1, -4, 1, 1],
    [0, 0, 0, 1, 0],
])
print(dist([[1, 3, 1, 3], 4, 0, 0, 0], (0, 1), 4, test))

# %%
ins = API.start(1)
print(ins)
ideal = np.array([[5., 4., 4., 4., 4.],
                  [4., 4., 4., 3., 4.],
                  [5., 5., 4., 3., 4.],
                  [3., 5., 3., 2., 5.],
                  [4., 4., 4., 5., 4.]])


while not ins.is_finished():
    tstates = np.array([
        [[], *ins.from_id(ins.trucks[id][0]), ins.trucks[id][1], 0] for id in range(ins.trucks.shape[0])
    ])
    mv = ideal - ins.storage
    rrecv = sorted(filter(lambda v: v[1] > 0, np.ndenumerate(
        mv)), key=lambda v: v[1], reverse=True)
    rsend = sorted(
        filter(lambda v: v[1] < 0, np.ndenumerate(mv)), key=lambda v: v[1])
    while len(rrecv) <= 0 and np.any(tstates[:, 0] >= 0):
        (r, c), need = rrecv[0]

    ins.simulate()

print(ins.score(end_to_no_work=True))
