import pandas as pd
from raceplotly.plots import barplot
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub-energy-fossil-renewables-nuclear.csv')

def barPlot(df):
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

def tipoenerW (df, col1, col2, colTieme):
      df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]
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

# tipoenerW(df, 'País', 'Renovables (% Energía Primaria Equivalente)', 'Año')


# df = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_primary-sub-energy-source.csv')

def linealTwh(df):
    paises = df[df['Código']!='OWID_WRL']
    año = paises[paises['Año']>= 1995]
    fig1 = px.line(df, x='Año', y="Consumo Eólico - Twh", color="Código",title='Consumo de Consumo Eólico - Twh')
    fig1.show()
    return fig1

# linealTwh(año)


import plotly.offline as py
def Lineal2(df):
    pais_df = df[(df['Código'].isna() != True) & (df['País'] != 'World')]
    col = ['Consumo De Carbón - Twh', 'Consumo Hidroeléctrico - Twh','Consumo Solar - Twh','Consumo De Aceite - Twh']
    año = pais_df.groupby('Año')[col].sum()
    py.iplot([{
        'x':año.index,
        'y':año[col],
        'name': col
    } for col in  año.columns], filename='cufflinks/multiple-lines-on-same-chart')
    return py.iplot



## data = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_primary-sub-energy-source.csv')

## data = cargadata('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_sub_energy_fossil_renewables_nuclear.csv')

##  tipoenerW(data, 'País', 'Consumo Hidroeléctrico - Twh', 'Año')



##data_co = pd.read_csv('C:\\Users\\x\\OneDrive\\Escritorio\\Agus\\Henry DATA 02\\emissionsmap\\SubirData\\Normalizados\\Normal_energyco2.csv')

def emisionco2(df):
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
    fig = px.bar(df.head(10), x='País', y='Emisión De Co2', color='Emisión De Co2', title='Top 10 Países que utilizan Energia Emisión De Co2')
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
    return fig

## emisionco2(data_co)


def emisionco_2(df):
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
    return df.head(10)

## emisionco2(data_co)




# top_5m = data_co[(data_co['País'] != 'World') & (data_co['Combustible'] != 'all energy types')]
# top_5m = data_co[(data_co['País'] != 'Former U.S.S.R.')]
# top_5m = top_5m.groupby('País')['Emisión De Co2'].sum()
# top_5m = top_5m.reset_index()

# top_5m.sort_values('Emisión De Co2',ascending=True, inplace=True)
# df = top_5m.iloc[3:]


def emisionco2(df):
    list = []

    for País in df['País'].unique():

        emisionco_2 = df.groupby('País').count()['Emisión De Co2'].reset_index().sort_values(by='Emisión De Co2',ascending=False)
        emisionco_2.style.background_gradient(cmap='winter')
        total = df[df['País']==País]['Emisión De Co2'].sum(axis=0)
        total_2 = df[df['País']==País]['Emisión De Co2']
        list.extend([[País, total]])
    # Creacion de dataframe
    df = pd.DataFrame(list, columns=['País', 'Emisión De Co2']).sort_values(by='Emisión De Co2',ascending=False)

    # Plotting 10 Países 2021
    fig = px.bar(df.tail(10), x='País', y='Emisión De Co2', color='Emisión De Co2', title='Top 10 Países que utilizan Energia Emisión De Co2')
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
    fig.update_xaxes(tickangle= -90)
    return fig

    ## emisionco2(df)


    def emisionco_2(df):
        list = []

        for País in df['País'].unique():
            emisionco_2 = df.groupby('País').count()['Emisión De Co2'].reset_index().sort_values(by='Emisión De Co2',ascending=False)
            total = df[df['País']==País]['Emisión De Co2'].sum(axis=0)
            total_2 = df[df['País']==País]['Emisión De Co2']
            list.extend([[País, total]])
        # Creacion de dataframe
        df = pd.DataFrame(list, columns=['País', 'Emisión De Co2']).sort_values(by='Emisión De Co2',ascending=False)
        return df.tail(10)


    ## emisionco_2(df)

    