# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
# 03t0qej1r8

import plotly.plotly as py
import pandas as pd
import plotly.tools as tls

tls.set_credentials_file(username='tonnamb', api_key='03t0qej1r8')

df = pd.read_csv('elections_data.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' +\
    'Hillary Clinton '+df['clinton']+' %'+'<br>'+\
    'Bernie Sanders '+df['sanders']+' %'+'<br>'+\
    'Donald Trump '+df['trump']+' %'+'<br>'+\
    'Ted Cruz'+df['cruz']+' %'

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['code'],
        z = df['percent democrat'].astype(float),
        locationmode = 'USA-states',
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            )
        ),
        colorbar = dict(
            title = "Percent of Democrats"
        )
    ) ]

layout = dict(
        title = '2016 US Presidential Prediction based on Twitter Analytics',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)',
        ),
    )
    
fig = dict( data=data, layout=layout )

url = py.plot( fig, filename='d3-cloropleth-map' )