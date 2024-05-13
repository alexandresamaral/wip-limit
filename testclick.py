import numpy as np
import pandas as pd
import plotly.express as px
import math, json
import dash
from dash.dependencies import Input, Output, State
from jupyter_dash import JupyterDash

GS = 100
fig = px.line(
    x=np.linspace(0, 1, 300), y=(np.sin(np.linspace(0, math.pi * 3, 300)) / 2) + 0.5
).add_traces(
    px.scatter(
        x=np.repeat(np.linspace(0, 1, GS), GS), y=np.tile(np.linspace(0, 1, GS), GS)
    )
    .update_traces(marker_color="rgba(0,0,0,0)")
    .data
)

# Build App
app = JupyterDash(__name__)
app.layout = dash.html.Div(
    [dash.dcc.Graph(id="graph", figure=fig), dash.html.Div(id="where")]
)


@app.callback(
    Output("where", "children"),
    Input("graph", "clickData"),
)
def click(clickData):
    if not clickData:
        raise dash.exceptions.PreventUpdate
    return json.dumps({k: clickData["points"][0][k] for k in ["x", "y"]})


# Run app and display result inline in the notebook
app.run_server(mode="inline")