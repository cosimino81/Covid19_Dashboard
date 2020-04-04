# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:42:04 2020

@author: CURIACOSI1
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from plotlymap import mappa

# read df
#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
#df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# df function 
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# set world map
import plotly.express as px
df = px.data.gapminder()
fig_world = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     animation_frame="year",
                     projection="natural earth")


# set gapminder 
df_minder = px.data.gapminder().query("continent=='Oceania'")
fig_minder = px.line(df_minder, x="year", y="lifeExp", color="country", title="layout.hovermode='closest' (the default)")
fig_minder.update_traces(mode="markers+lines")



# external css style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# setting the app with external css style
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

# setting colors
colors = {'background': '#111111',
          'text': '#7FDBFF',
          'table':'#ffffff'}
 

app.layout = html.Div([
             # banner         
             html.Div([html.H2(children='COVID-19 Dashbord Tracker', style = {'textAlign':'left'}),
                       html.Img(src = 'assets/coding_waves_logo.png')], className = "banner"),
             
             # map
             html.Div([
                 html.Div([
                     dcc.Graph(figure = fig_world)
                     ], className = "seven columns"),
                 
                 html.Div([
                     dcc.Graph(figure = fig_minder)
                     ], className = "five columns")
                 
                 ]),
             
             # main plots
             html.Div([
                 # left plot
                 html.Div([
                     dcc.Graph(
                            id='left-graph-1',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                ],
                                'layout': {
                                    'plot_bgcolor': '#f0f0f5',
                                    'paper_bgcolor': '#f0f0f5',
                                    'font': {
                                        'color': colors['background']
                                    }
                                }
                            }
                        )
                     ], className = "six columns"),
                 
                 # right plot
                 html.Div([
                     dcc.Graph(
                            id='rigth-graph-1',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                ],
                                'layout': {
                                    'plot_bgcolor': '#f0f0f5',
                                    'paper_bgcolor': '#f0f0f5',
                                    'font': {
                                        'color': colors['background']
                                    }
                                }
                            }
                        )
                     ], className = "six columns")
                 
                 ])
            
            
    
 ])
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)


