import pandas as pd
from raceplotly.plots import barplot


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