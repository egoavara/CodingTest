
# %%
from dataclasses import dataclass

@dataclass
class Click:
    g : int
    h : int

li = [
    ['ACT', '1'],
    {'D' : 1, 'E' : 2},
    {'D' : 3, 'E' : 4, 'G' : 5},
    Click(11, 22),
]
for el in li:
    match el:
        case [action, obj]:
            print(f'AB : {action}, {obj}')
        case {'D' : d, 'E' : e, **kwargs}:
            print(f'DE : {d}, {e}, {kwargs}')
        case Click(g, h):
            print(f'GH : {g}, {h}')