# %%
import numpy as np
import plotly.express as px
import pandas as pd

from IPython import display

da = pd.DataFrame(
    np.array([
        x:=np.linspace(0, 10, 100),
        np.sin(x),
    ], dtype= np.float64).T,
    columns=['x', 'y'],
    
)

fig = px.line(da, x='x', y='y', title='Life expectancy in Canada')

fig.show()