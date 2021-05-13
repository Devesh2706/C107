import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")
studentdf = df.loc[df["student_id"] == "TRL_abc"]
print(df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(

    x = studentdf.groupby("level")["attempt"].mean(),
    y = ["level 1","level 2","level 3","level 4"],
    orientation = "h"
))

fig.show()