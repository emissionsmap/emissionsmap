import folium

def mapPlot():
    m = folium.Map(location=[-9.189967, -75.015152],
                    position='absolute',zoom_start=2,
                    zoom_control = False, max_zoom=4,
                    prefer_canvas=True)
    	
    folium.TileLayer('stamenwatercolor').add_to(m)
    folium.Marker(location=[-9.189967, -75.015152]).add_to(m)
    return m._repr_html_()