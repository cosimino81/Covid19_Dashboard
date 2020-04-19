# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:42:04 2020

@author: CURIACOSI1
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


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

# =============================================================================
# PLOT CREATION
# =============================================================================

# world map 1
import plotly.graph_objects as go

dfworld = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

fig_world_1 = go.Figure(data=go.Choropleth(
            locations = dfworld['CODE'],
            z = dfworld['GDP (BILLIONS)'],
            text = dfworld['COUNTRY'],
            colorscale = 'Blues',
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title = 'Number of Cases',
))

fig_world_1.update_geos(
            #projection_type="orthographic",
            #landcolor="rgb(242, 242, 242)",
            oceancolor="rgb(204, 230, 255)",
            showocean=True,
            lakecolor="LightBlue",
            showcountries=True, countrycolor="Black",
            showsubunits=True, subunitcolor="Black"
)

fig_world_1.update_layout(
    # title={
    #     'text': "World Cases",
    #     'y':0.9,
    #     'x':0.5,
    #     'xanchor': 'center',
    #     'yanchor': 'top'},

    paper_bgcolor='#404040',
    
    margin=dict(
                l=0,
                r=5,
                b=10,
                t=10,
                pad=4
    ),
    
    font = dict(color= 'rgb(255, 255, 255)',
               size = 14),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        #projection_type="orthographic"
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: UE Open Data',
        showarrow = False
    )]
)



# World Map
import plotly.express as px
df = px.data.gapminder().query("year==2007")

fig_world = px.scatter_geo(df, locations="iso_alpha", color="continent",
                                hover_name="country", size="pop",
                                projection="natural earth")

fig_world.update_geos(
                    #projection_type="orthographic",
                    landcolor="rgb(242, 242, 242)",
                    oceancolor="rgb(51, 204, 255)",
                    showocean=True,
                    lakecolor="LightBlue",
                    showcountries=True, countrycolor="White",
                    showsubunits=True, subunitcolor="Black")

fig_world.update_layout(
                        legend_title='<b> Continents </b>',
                        legend=dict(x=1, y=1),  
                        paper_bgcolor="White",
                        plot_bgcolor = '#404040',
                        template="plotly_white",
                        margin=dict(r=10, t=25, b=40, l=60),
                        annotations=[
                            dict(
                                text="Source: UE Open Data",
                                showarrow=False,
                                xref="paper",
                                yref="paper",
                                x=5,
                                y=0)])


# Barchart
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig_bar = px.bar(data_canada, x='year', y='pop')
fig_bar.update_layout(
                      plot_bgcolor = '#404040',
                      paper_bgcolor = '#404040',
                      font = dict(
                                size=12,
                                color="#ffffff")
)

# Lineplot
import plotly.express as px
df = px.data.gapminder().query("continent=='Oceania'")
fig_line = px.line(df, x="year", y="lifeExp", color='country')
fig_line.update_layout(
                      plot_bgcolor = '#404040',
                      paper_bgcolor = '#404040',
                      font = dict(
                                size=12,
                                color="#ffffff"))

# Pie chart
import plotly.express as px
dfpie = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
fig_pie = px.pie(dfpie, values='pop', names='country',
             title='Population of American continent',
             hover_data=['lifeExp'], labels={'lifeExp':'life expectancy'})

fig_pie.update_traces(textposition='inside', textinfo='percent+label')

fig_pie.update_layout(
                      plot_bgcolor = '#404040',
                      paper_bgcolor = '#404040',
                      font = dict(
                                size=12,
                                color="#ffffff")
)
# =============================================================================
#  Dashbord
# =============================================================================

# set gapminder 
df_minder = px.data.gapminder().query("continent=='Oceania'")
fig_minder = px.line(df_minder, x="year", y="lifeExp", color="country", title="layout.hovermode='closest' (the default)")
fig_minder.update_traces(mode="markers+lines")



# external css style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# setting the app with external css style
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

# setting colors
colors = {'background': '#404040',
          'text': '#7FDBFF',
          'table':'#ffffff'}
 

app.layout = html.Div(style={'backgroundColor': 'rgb(64, 64, 64)'}, 
                      
            children = [
                
            # banner         
             html.Div([html.H2(children='COVID-19 Dashbord Tracker', style = {'textAlign':'left'}),
                       html.Img(src = 'assets/coding_waves_logo.png')], className = "banner"),
        
             
             # 1st level
             html.Div([
                 # left plot map
                 html.Div([
                     dcc.Graph(figure = fig_world_1)
                     ], className = "seven columns", style={'backgroundColor': colors['background']}),
                 
                 # rigth plot
                  html.Div([
                      dcc.Graph(figure = fig_bar)
                      ], className = "five columns")
                 
                  ]),
             
             
             #2nd level 
             html.Div([
                 # left plot
                 html.Div([
                     html.P("Column1"),
                     dcc.Graph(figure = fig_line)
                     ], className = "seven columns"),
                 
                 # right plot
                 html.Div([
                     html.P("Colum2"),
                     dcc.Graph( figure = fig_pie)
                     ], className = "five columns")
                 
                 ], style={'backgroundColor': colors['background']})
            
    
 ])
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader = False)


