from re import template
import pandas as pd
from raceplotly.plots import barplot
import plotly.offline as py
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


#df:D:\emissionsmap\SubirData\archivosPrueba\energyco2.csv
#col1:'Energy_type' / col2:'Energy_consumption' / colTime:'Year'

def tipoenerW ():
      df = pd.read_csv("energyco2.csv")
      df = df[(df['Country']=='World') & (df['Energy_type']!='all_energy_types')]
      df.drop(columns='Unnamed: 0', inplace=True)

      color_continuous_scale={
                "all_energy_types": "rgb(166, 255, 249)",
                "coal": "rgb(132, 255, 233)",
                "natural_gas": "rgb(100, 255, 233)",
                "petroleum_n_other_liquids": "rgb(0, 186, 186)",
                "nuclear": "rgb(0, 124, 124)",
                "renewables_n_other":"rgb(0, 124, 124)"
      }

      my_raceplot = barplot(df,  item_column='Energy_type', value_column='Energy_consumption', time_column='Year', top_entries=10, item_color=color_continuous_scale)
      fig=my_raceplot.plot(item_label = 'Energy_type', value_label = 'Energy_consumption', frame_duration = 200, date_format='%Y',orientation='horizontal')

     # Add chart title, format the chart, etc.
      fig.update_layout(
            title='Energy_consumption',
            title_x=0.15,
            width=700,
            height=500,
            # paper_bgcolor="black",
            # labels="black"
            #template="seaborn")
      )

      # fig.update_layout(
      #       width=700,
      #       height=300,
      #       margin=dict(l=10,r=10,b=10,t=10),
      #       yaxis_title='',
      #       xaxis_title='',
      #       yaxis=dict(
      #           showticklabels=False)
      #   )
      return fig  


# df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub-energy-fossil-renewables-nuclear.csv')

def barPlot():
      df = pd.read_csv("Normal_sub_energy_fossil_renewables_nuclear.csv")
      list = []
      pais_df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]
      año = pais_df[pais_df['Año']== 2021]
      for País in año['País'].unique():
            total = año[año['País']==País]['Renovables (% Energía Primaria Equivalente)'].sum(axis=0)
            total_2 = año[año['País']==País]['Renovables (% Energía Primaria Equivalente)']
            list.extend([[País, total]])

            
      # Creacion de dataframe
      paises_renovables = pd.DataFrame(list, columns=['País', 'Renovables (% Energía Primaria Equivalente)']).sort_values(by='Renovables (% Energía Primaria Equivalente)',ascending=False)

      # Plotting 10 Países 2021
      fig = px.bar(paises_renovables.head(10), x='País', y='Renovables (% Energía Primaria Equivalente)',color='Renovables (% Energía Primaria Equivalente)', title='Top 10 Países que utilizan Energia Renovables (% Energía Primaria Equivalente)')

      return fig

## df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub_energy_fossil_renewables_nuclear.csv')

def tipoenerA ():
      df = pd.read_csv("Normal_sub_energy_fossil_renewables_nuclear.csv")
      df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]
      my_raceplot = barplot(df,  item_column='País', value_column='Renovables (% Energía Primaria Equivalente)', time_column='Año',top_entries=10)
      fig=my_raceplot.plot(item_label = 'País', value_label = 'Renovables (% Energía Primaria Equivalente)', frame_duration = 200, date_format='%Y',orientation='horizontal')

      #Add chart title, format the chart, etc.
      fig.update_layout(
            title='Renovables (% Energía Primaria Equivalente)',
            title_x=0.15,
            width=800,
            height=550,
            paper_bgcolor="whitesmoke",
            )
      return fig

# tipoenerW(df, 'País', 'Renovables (% Energía Primaria Equivalente)', 'Año')

def lineal2Plot():
      df01 = pd.read_csv('huella_biocapacidad.csv')
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


## df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub_energy_fossil_renewables_nuclear.csv')

def tipoenerB ():
      df = pd.read_csv("Normal_sub_energy_fossil_renewables_nuclear.csv")
      df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]
      my_raceplot = barplot(df,  item_column='País', value_column='Renovables (% Energía Primaria Equivalente)', time_column='Año',top_entries=10)
      fig=my_raceplot.plot(item_label = 'País', value_label = 'Renovables (% Energía Primaria Equivalente)', frame_duration = 200, date_format='%Y',orientation='horizontal')

      #Add chart title, format the chart, etc.
      fig.update_layout(
            title='Renovables (% Energía Primaria Equivalente)',
            title_x=0.15,
            width=800,
            height=550,
            paper_bgcolor="whitesmoke",
            )
      return fig

# tipoenerW(df, 'País', 'Renovables (% Energía Primaria Equivalente)', 'Año')


# df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_primary-sub-energy-source.csv')

def linealTwh():
      df = pd.read_csv("Normal_primary_sub_energy_source.csv")
      paises = df[df['Código']!='OWID_WRL']
      año = paises[paises['Año']>= 1995]
      fig1 = px.line(df, x='Año', y="Consumo Eólico - Twh", color="Código",title='Consumo de Consumo Eólico - Twh')

      return fig1

# # linealTwh(año)


def lineal2Plot2():
    df02 = pd.read_csv('Temperatura_anomalia.csv', sep=';', low_memory=False, encoding='utf-8')
    df04 = pd.read_csv('gases.csv')
    
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
        name='Variación Temperatura')
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