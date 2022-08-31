// style choropleth map color
function getColor(d) {
    return d > 1000 ? '#800026' :
           d > 500  ? '#BD0026' :
           d > 200  ? '#E31A1C' :
           d > 100  ? '#FC4E2A' :
           d > 50   ? '#FD8D3C' :
           d > 20   ? '#FEB24C' :
           d > 10   ? '#FED976' :
                      '#FFEDA0';
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.density),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}


// get leaflet and configuration
var map = L.map('map',{ zoomControl: false }).setView([51.505, -0.09], 5);

var southWest = L.latLng(-50.98155760646617, -180),
northEast = L.latLng(82.99346179538875, 180);
var bounds = L.latLngBounds(southWest, northEast);

map.setMaxBounds(bounds);
map.on('drag', function() {
    map.panInsideBounds(bounds, { animate: false });
});



// // base and control layers
var osmBase = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 8,
    minZoom:2,
    attribution: '© OpenStreetMap ....................'
}).addTo(map);


// // var punto = L.marker([37.88437176085360, -4.779524803161621]).bindPopup('Soy un puntazo');
// // punto.addTo(map);

var baseMaps = {
    "OSM": osmBase,
    // "Catastro": catastroBase
};

var overlayMaps = {
    // "Puntazo": punto
};

L.control.layers(
    baseMaps, 
    overlayMaps,
    {
	position: 'topright',
	collapsed: true
}).addTo(map);


// geoJson
L.geoJSON(statesData, {
        style: style
    })
    .bindPopup((layer) => {
        if(layer.feature.properties.name){
            aside__right.classList.add('move__right')
            }
        console.log(layer.feature.properties.name)
        return layer.feature.properties.name
    })
    .addTo(map);


//legend
var legend = L.control({position: 'bottomleft'});

legend.onAdd = function () {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 20, 50, 100, 200, 500, 1000]

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
};
legend.addTo(map);