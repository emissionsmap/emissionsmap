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
      df = pd.read_csv("archivos/energyco2.csv")
      df = df[(df['Country']=='World') & (df['Energy_type']!='all_energy_types')]
      df.drop(columns='Unnamed: 0', inplace=True)

      color_continuous_scale={
                "all_energy_types": "#5C3C3C",
                "coal": "#591B1B",
                "natural_gas": "#7f0000",
                "petroleum_n_other_liquids": "#bd0003",
                "nuclear": "#ff0000",
                "renewables_n_other":"#F53900"
      }

      my_raceplot = barplot(df,  item_column='Energy_type', value_column='Energy_consumption', time_column='Year', top_entries=10, item_color=color_continuous_scale)
      fig=my_raceplot.plot(item_label = 'Energy_type', value_label = 'Energy_consumption', frame_duration = 200, date_format='%Y',orientation='horizontal')


      fig.update_layout( title='Consumo de energía segun su fuente ',
                        width=700,
                        height=500,
                        title_x=0.15,
                        margin=dict(t=70, b=0, l=70, r=40),
                        hovermode="x unified",
                        xaxis_tickangle=360,
                        xaxis_title=' ', yaxis_title=" ",
                        plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                        title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                        font=dict(color='#8a8d93'),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                          )
     # Add chart title, format the chart, etc.
      # fig.update_layout(
      #       title='Energy_consumption',
      #       title_x=0.15,
      #       width=700,
      #       height=500,
      #       hovermode="x unified",
      #       #paper_bgcolor="black",
      #       #template="plotly_dark", 
      #       plot_bgcolor='#2d3035', #paper_bgcolor='#2d3035',
      #       title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
      #       font=dict(color='#8a8d93'),
      #       legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
      #       )

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
      df = pd.read_csv("archivos/Normal_sub_energy_fossil_renewables_nuclear.csv")
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

      fig.update_layout( title='Energy_consumption',
                  height=300,
                  width=900,
                  title_x=0.15,
                  margin=dict(t=70, b=0, l=70, r=40),
                  hovermode="x unified",
                  xaxis_tickangle=360,
                  xaxis_title=' ', yaxis_title=" ",
                  plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                  title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                  font=dict(color='#8a8d93'),
                  legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                        )
      return fig

## df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub_energy_fossil_renewables_nuclear.csv')

def tipoenerA ():
      df = pd.read_csv("archivos/Normal_sub_energy_fossil_renewables_nuclear.csv")
      df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]
      my_raceplot = barplot(df,  item_column='País', value_column='Renovables (% Energía Primaria Equivalente)', time_column='Año',top_entries=5)
      fig=my_raceplot.plot(item_label = 'País', value_label = 'Renovables (% Energía Primaria Equivalente)', frame_duration = 200, date_format='%Y',orientation='horizontal')

      #Add chart title, format the chart, etc.

      fig.update_layout( title='Paises con mayor uso de energía renovables',
                  height=300,
                  width=900,
                  title_x=0.15,
                  margin=dict(t=70, b=0, l=70, r=40),
                  hovermode="x unified",
                  xaxis_tickangle=360,
                  xaxis_title=' ', yaxis_title=" ",
                  plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                  title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                  font=dict(color='#8a8d93'),
                  legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                        )
      return fig

# tipoenerW(df, 'País', 'Renovables (% Energía Primaria Equivalente)', 'Año')

def lineal2Plot():
      df01 = pd.read_csv('archivos/huella_biocapacidad.csv')
      fig= go.Figure(data=[
            go.Scatter(
            x=df01['Año'],
            y=df01['Biocapacidad PerCap'],
            mode='lines', 
            name='Biocapacidad PerCap',
            line=dict(color='cyan')
            ),
            go.Scatter(
            x=df01['Año'],
            y=df01['Huella Ecologica PerCap'],
            mode='lines',
            name='Huella Ecologica PerCap'
            )
      ])
      fig.update_layout(
            # title=name_title,
            height=300,
            width=900,
            plot_bgcolor='#2d3035',
            paper_bgcolor= '#2d3035',
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
                  bgcolor="#2d3035",
                  bordercolor="LightSteelBlue",
                  borderwidth=1
            ),
            xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
            yaxis=dict(showgrid=False),
            margin=dict(l=10,r=10,b=10,t=10))

      
      return fig


## df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub_energy_fossil_renewables_nuclear.csv')

def tipoenerB ():
      df = pd.read_csv("archivos/Normal_sub_energy_fossil_renewables_nuclear.csv")
      df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]

      color_continuous_scale={
            "Norway": "#5C3C3C",
            "Brazil": "#591B1B",
            "New Zealand": "#7f0000",
            "Sweden": "#bd0003",
            "Iceland": "#ff0000",
            "Austria":"#F53900"
      }

      my_raceplot = barplot(df,  item_column='País', value_column='Renovables (% Energía Primaria Equivalente)', time_column='Año',top_entries=5, item_color=color_continuous_scale)
      fig=my_raceplot.plot(item_label = 'País', value_label = '% de energía renovable utilizada', frame_duration = 200, date_format='%Y',orientation='horizontal')


      #Add chart title, format the chart, etc.
      fig.update_layout( title='Consumo de energía renovable por país(%)',
                        title_x=0.15,
                        margin=dict(t=70, b=0, l=70, r=40),
                        #hovermode="x unified",
                        #xaxis_tickangle=360,
                        #xaxis_title=' ', yaxis_title=" ",
                        plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                        title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                        font=dict(color='#8a8d93'),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                  )
      return fig

# tipoenerW(df, 'País', 'Renovables (% Energía Primaria Equivalente)', 'Año')


# df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_primary-sub-energy-source.csv')

def linealTwh():
      df = pd.read_csv("archivos/Normal_primary_sub_energy_source.csv")
      paises = df[df['Código']!='OWID_WRL']
      año = paises[paises['Año']>= 1995]
      fig1 = px.line(df, x='Año', y="Consumo Eólico - Twh", color="Código",title='Consumo de Energia Eólica (Twh) por País')

      fig1.update_layout(
            height=300,
            width=900,
            plot_bgcolor='#2d3035',
            paper_bgcolor= '#2d3035',
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
                  bgcolor="#2d3035",
                  bordercolor="LightSteelBlue",
                  borderwidth=1
            ),
            xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
            yaxis=dict(showgrid=False),
            margin=dict(l=10,r=10,b=10,t=10)
      )

      return fig1

# # linealTwh(año)


def lineal2Plot2():
    df02 = pd.read_csv('archivos/Temperatura_anomalia.csv', sep=';', low_memory=False, encoding='utf-8')
    df04 = pd.read_csv('archivos/gases.csv')
    
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
            width=900,
        plot_bgcolor='#2d3035',
        paper_bgcolor= '#2d3035',
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
                bgcolor="#2d3035",
                bordercolor="LightSteelBlue",
                borderwidth=1
        ),
        xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
        yaxis=dict(showgrid=False),
        margin=dict(l=10,r=10,b=10,t=10)
    )
    return fig


##data_co = pd.read_csv('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_energyco2.csv')

def emisionco2():
      df = pd.read_csv("archivos/Normal_energyco2.csv")
      list = []

      for País in df['País'].unique():
            df = df[df['País'] != 'World']
            df = df[df['País'] != 'Former U.S.S.R.']
            emisionco_2 = df.groupby('País').count()['Emisión De Co2'].reset_index().sort_values(by='Emisión De Co2',ascending=False)
            emisionco_2.style.background_gradient(cmap='winter')
            total = df[df['País']==País]['Emisión De Co2'].sum(axis=0)
            total_2 = df[df['País']==País]['Emisión De Co2']
            list.extend([[País, total]])
      # Creacion de dataframe
      df = pd.DataFrame(list, columns=['País', 'Emisión De Co2']).sort_values(by='Emisión De Co2',ascending=False)

      # Plotting 20 Países 2021
      fig = px.bar(df.head(10), x='País', y='Emisión De Co2', color='Emisión De Co2', title='Top 10 Países que utilizan Energia Emisión De Co2', color_continuous_scale=px.colors.sequential.solar_r)
      fig.update_layout( title='Top 10 Países con mas emisiones de Co2',
                        title_x=0.15,
                        margin=dict(t=70, b=0, l=70, r=40),
                        hovermode="x unified",
                        xaxis_tickangle=360,
                        xaxis_title='País', yaxis_title="Emisión De Co2",
                        plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                        title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                        font=dict(color='white'),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                                                )
      return fig

## emisionco2(data_co)


def emisionco_22():
    df = pd.read_csv("archivos/Normal_energyco2.csv")
    list = []

    for País in df['País'].unique():
        df = df[df['País'] != 'World']
        df = df[df['País'] != 'Former U.S.S.R.']
        emisionco_2 = df.groupby('País').count()['Emisión De Co2'].reset_index().sort_values(by='Emisión De Co2',ascending=False)
        total = df[df['País']==País]['Emisión De Co2'].sum(axis=0)
        total_2 = df[df['País']==País]['Emisión De Co2']
        list.extend([[País, total]])
    # Creacion de dataframe
    df = pd.DataFrame(list, columns=['País', 'Emisión De Co2']).sort_values(by='Emisión De Co2',ascending=False)
    df.reset_index(inplace=True)
    return df.head(10)

## emisionco2(data_co)

def mapa ():
      df_newmap = pd.read_csv("archivos/Normal_energyco2.csv")
      df_newmap = df_newmap[["País", "Año", "Combustible", "Emisión De Co2"]]
      df_newmap = df_newmap[(df_newmap["País"] != "World") & (df_newmap["Combustible"] == "all energy types") & (df_newmap["Año"] == 2019)]

      for i in df_newmap["País"].values:
            if "U.S." in i:
                  aux = df_newmap[df_newmap["País"] == i].index
                  df_newmap = df_newmap.drop(aux)

      data = dict(type = 'choropleth', 
                  locations = df_newmap['País'], 
                  locationmode = 'country names', 
                  z = list(df_newmap['Emisión De Co2']), 
                  colorscale=[
                        [0, "#ffa372"],
                        [0.10, "#F53900"],
                        [0.25, "#ff0000"],
                        [0.50, "#bd0003"],
                        [0.60, "#7f0000"],
                        [0.75, "#591B1B"],
                        [1, "#5C3C3C"]],
                  text = df_newmap['País'])
      layout = dict(geo = dict(scope='world'))

      fig = go.Figure(data=[data], layout=layout)
      fig.update_layout(
            margin=dict(l=5,r=5,b=5,t=5),
            paper_bgcolor= 'black',
            font_color='#cee3e1',
      )              
      return fig





def co2Menos():
      list = []
      data_co = pd.read_csv("archivos/Normal_energyco2.csv")
      top_5m = data_co[(data_co['País'] != 'World') & (data_co['Combustible'] != 'all energy types')]
      top_5m = data_co[(data_co['País'] != 'Former U.S.S.R.')]
      top_5m = top_5m.groupby('País')['Emisión De Co2'].sum()
      top_5m = top_5m.reset_index()

      top_5m.sort_values('Emisión De Co2',ascending=True, inplace=True)
      df = top_5m.iloc[3:]
      for País in df['País'].unique():

            emisionco_2 = df.groupby('País').count()['Emisión De Co2'].reset_index().sort_values(by='Emisión De Co2',ascending=False)
            emisionco_2.style.background_gradient(cmap='winter')
            total = df[df['País']==País]['Emisión De Co2'].sum(axis=0)
            total_2 = df[df['País']==País]['Emisión De Co2']
            list.extend([[País, total]])
      # Creacion de dataframe
      df = pd.DataFrame(list, columns=['País', 'Emisión De Co2']).sort_values(by='Emisión De Co2',ascending=False)

      # Plotting 10 Países 2021
      fig = px.bar(df.tail(10), x='País', y='Emisión De Co2', color='Emisión De Co2', title='Top 10 menor emisión de CO2', color_continuous_scale=px.colors.sequential.solar)
      fig.update_layout( title='Top 10 Países que utilizan Energia Emisión De Co2',
                              title_x=0.15,
                              margin=dict(t=70, b=0, l=70, r=40),
                              hovermode="x unified",
                              xaxis_tickangle=360,
                              xaxis_title='País', yaxis_title="Emisión De Co2",
                              plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                              title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                              font=dict(color='white'),
                              legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                              )
      fig.update_xaxes(tickangle = -90)
      return fig

    ## emisionco2(df)


def co2menostab():
      list = []
      data_co = pd.read_csv("archivos/Normal_energyco2.csv")
      top_5m = data_co[(data_co['País'] != 'World') & (data_co['Combustible'] != 'all energy types')]
      top_5m = data_co[(data_co['País'] != 'Former U.S.S.R.')]
      top_5m = top_5m.groupby('País')['Emisión De Co2'].sum()
      top_5m = top_5m.reset_index()
      top_5m.sort_values('Emisión De Co2',ascending=True, inplace=True)
      df = top_5m.iloc[3:]

      for País in df['País'].unique():
            emisionco_2 = df.groupby('País').count()['Emisión De Co2'].reset_index().sort_values(by='Emisión De Co2',ascending=False)
            total = df[df['País']==País]['Emisión De Co2'].sum(axis=0)
            total_2 = df[df['País']==País]['Emisión De Co2']
            list.extend([[País, total]])
      # Creacion de dataframe
      df = pd.DataFrame(list, columns=['País', 'Emisión De Co2']).sort_values(by='Emisión De Co2',ascending=False)
      df.reset_index(inplace=True)
      return df.tail(10)


## emisionco_2(df)
