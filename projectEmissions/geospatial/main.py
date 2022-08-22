import folium

def mapPlot():
    m = folium.Map(location=[-9.189967, -75.015152], zoom_start=5)
    folium.Marker(location=[-9.189967, -75.015152]).add_to(m)
    return m._repr_html_()