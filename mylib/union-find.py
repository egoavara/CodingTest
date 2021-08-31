# %%
"""Union-Find 자료구조, path compress 사용"""
from typing import Generic, Hashable, TypeVar


UFKT = TypeVar('UFKT', bound=Hashable)

class UnionFind(Generic[UFKT]):
    def __init__(self):
        self.__c_dt = dict()
    def union(self, a: UFKT, b: UFKT):
        a = self.find(a)
        b = self.find(b)
        self.__c_dt[a] = b
    def find(self, key: UFKT):
        if key not in self.__c_dt:
            self.__c_dt[key] = key
        if key != self.__c_dt[key]:
            self.__c_dt[key] = self.find(self.__c_dt[key])
        return self.__c_dt[key]

# %%
"""Union-Find 자료구조, path compress 미사용"""
from typing import Generic, Hashable, TypeVar

UFKT = TypeVar('UFKT', bound=Hashable)

class UnionFind(Generic[UFKT]):
    def __init__(self):
        self.__c_dt = dict()
    def union(self, a: UFKT, b: UFKT):
        a = self.find(a)
        b = self.find(b)
        self.__c_dt[a] = b
    def find(self, key: UFKT):
        if key not in self.__c_dt:
            self.__c_dt[key] = key
        if key != self.__c_dt[key]:
            return self.find(self.__c_dt[key])
        return self.__c_dt[key]
# %%
"""테스트"""
uf = UnionFind()
uf.union(1, 2)
uf.union(2, 3)
uf.union(3, 'A')
print(uf.find(1))
print(uf.find(2))
print(uf.find(3))
print(uf.find('A'))
print(uf.find(4))