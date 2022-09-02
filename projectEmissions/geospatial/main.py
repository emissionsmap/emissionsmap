import geopandas as gpd
import pandas as pd
import folium

geojson1 = gpd.read_file('/home/alex/Escritorio/emissionsmap/projectEmissions/geospatial/world.geojson')
geojson1=geojson1[['NAME', 'geometry']]
CO2_df=pd.read_csv('/home/alex/Escritorio/emissionsmap/projectEmissions/geospatial/co.csv')
CO2_df = CO2_df[['Country Name','2010']]
# def mapPlot():
#     return CO2_df._repr_html()


def mapPlot():
   m = folium.Map(location=[-9.189967, -75.015152],
                   position='absolute',zoom_start=2,
                   zoom_control = False, max_zoom=4,
                   prefer_canvas=True)
   folium.Choropleth(
           geo_data=geojson1,
           data=CO2_df,
           columns=['Country Name','2010'],
           key_on='feature.properties.NAME',
           fill_color='YlOrRd',
           nan_fill_color="White",
           fill_opacity=0.7,
           line_opacity=0.2,
           legend_name='CO2 per capita 2010 ',
           highlight=True,
           line_color='black').add_to(m) 
   return m._repr_html_()
#
#print(geojson1)