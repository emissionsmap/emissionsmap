import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from googletrans import Translator
from pathlib import Path
import csv
import os


#df:D:\emissionsmap\SubirData\archivosPrueba\energyco2.csv
#col1:'Energy_type' / col2:'Energy_consumption' / colTime:'Year'

def tipoenerW (df, col1, col2, colTieme):
      df = df[(df['Country']=='World') & (df['Energy_type']!='all_energy_types')]
      df.drop(columns='Unnamed: 0', inplace=True)
      my_raceplot = barplot(df,  item_column=col1, value_column=col2, time_column=colTieme,top_entries=10)
      fig=my_raceplot.plot(item_label = col1, value_label = col2, frame_duration = 200, date_format='%Y',orientation='horizontal')

      #Add chart title, format the chart, etc.
      fig.update_layout(
            title=col2,
            title_x=0.15,
            width=800,
            height=550,
            paper_bgcolor="whitesmoke",
            )
      return fig



def lineal2Plot():
      df01 = pd.read_csv(r'D:\emissionsmap\SubirData\archivosPrueba\huella_biocapacidad.csv')
      fig= go.Figure(data=[
            go.Scatter(
            x=df01['Año'],
            y=df01['Biocapacidad PerCap'],
            mode='lines', 
            name='Adultos con Covid',
            line=dict(color='cyan')
            ),
            go.Scatter(
            x=df01['Año'],
            y=df01['Huella Ecologica PerCap'],
            mode='lines',
            name='Menores de Edad con Covid'
            )
      ])
      fig.update_layout(
            # title=name_title,
            height=300,
            plot_bgcolor='black',
            paper_bgcolor= 'black',
            font_color='#cee3e1',
            legend=dict(
                  x=0.05,
                  y=1,
                  title_font_family="Times New Roman",
                  font=dict(
                  family="Courier",
                  size=12,
                  color="LightSteelBlue"
                  ),
                  bgcolor="Black",
                  bordercolor="LightSteelBlue",
                  borderwidth=1
            ),
            xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
            yaxis=dict(showgrid=False),
            margin=dict(l=10,r=10,b=10,t=10)
      )
      return fig



def lineal2Plot2():
    df02 = pd.read_csv(r'D:\emissionsmap\SubirData\archivosPrueba\Temperatura_anomalia.csv', sep=';', low_memory=False, encoding='utf-8')
    df04 = pd.read_csv(r'D:\emissionsmap\SubirData\archivosPrueba\gases.csv')
    
    df04.rename(columns={'year':'Año'}, inplace=True)
    df04 = df04.sort_values('Año')
    df04['Dif_co2'] = df04['Media co2'].diff()
    df04 = df04[['Año', 'Dif_co2']]
    df02 = df02[['Año', 'Anomalia de la temperatura media del promedio de 1961 a 1990']]
    df_n = pd.merge(df02, df04[['Año' ,'Dif_co2']], on=['Año'], how='left')
    df_n = df_n[df_n['Año'] >= 1960]
    
    fig= go.Figure(data=[
        go.Scatter(
        x=df_n['Año'],
        y=df_n['Dif_co2'],
        mode='lines', 
        name='Varición CO2',
        line=dict(color='cyan')
        ),
        go.Scatter(
        x=df_n['Año'],
        y=df_n['Anomalia de la temperatura media del promedio de 1961 a 1990'],
        mode='lines',
        name='Variación Temperatura'
        )
      ])
    fig.update_layout(
        # title=name_title,
        height=300,
        plot_bgcolor='black',
        paper_bgcolor= 'black',
        font_color='#cee3e1',
        legend=dict(
                x=0.05,
                y=1,
                title_font_family="Times New Roman",
                font=dict(
                family="Courier",
                size=12,
                color="LightSteelBlue"
                ),
                bgcolor="Black",
                bordercolor="LightSteelBlue",
                borderwidth=1
        ),
        xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
        yaxis=dict(showgrid=False),
        margin=dict(l=10,r=10,b=10,t=10)
    )
    return fig