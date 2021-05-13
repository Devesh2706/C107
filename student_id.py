import plotly.graph_objects as go
import pandas as pda

studentiddf = pda.read_csv("data_csv")
print(studentiddf.groupby("student_id")["attempt"].mean())
fig = go.Figure(go.Bar(

    x = studentiddf.groupby("student_id")["attempt"].mean(),
    y = ["attempt"],
    orientation = "h"
))
fig.show()