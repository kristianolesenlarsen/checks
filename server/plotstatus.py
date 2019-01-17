
"""
Dash app for showing the status of each student in the handin. 
"""


import pickle

import plotly.offline as py
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Event

from time import sleep
import subprocess


def cleandata():
    print("Reading raw data")
    with open('userdata.pckl', 'rb') as f:
        rawdata = pickle.load(f)
 
    print("Cleaning data")
    xvars  = list(rawdata.keys())
    ytrue  = [sum(rawdata[key].values()) for key in rawdata.keys()]
    yfalse = [sum([not i for i in rawdata[key].values()]) for key in rawdata.keys()]    
    
    t1 = go.Bar(
        x = xvars,
        y = ytrue,
        name = 'Correct',
        marker = dict(color = ["green" for _ in xvars])
        )

    t2 = go.Bar(
        x = xvars,
        y = yfalse,
        name = 'Wrong or unanswered',
        marker = dict(color = ["red" for _ in xvars])
        )

    return [t1, t2]


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=False),
        dcc.Interval(
            id='graph-update',
            interval=20*1000
        ),
    ]
)


@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph():
    data = cleandata()
    return {"data":data, "layout":go.Layout(barmode="stack")}
    

if __name__ == "__main__":
    app.run_server(debug=True)

