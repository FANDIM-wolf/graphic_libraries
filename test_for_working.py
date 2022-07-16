import plotly.express as px
import pandas as pd
def insert_array():
    d_array = [1, 32, 21, 4]
    return d_array
df = pd.DataFrame(dict(
    x = insert_array(),
    y = [1, 2, 3, 4]
))
fig = px.line(df, x="x", y="y", title="Unsorted Input") 
fig.show()

df = df.sort_values(by="x")
fig = px.line(df, x="x", y="y", title="Sorted Input") 
fig.show()
