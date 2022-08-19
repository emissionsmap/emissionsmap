# $$\text{Reporte para el csv: energyco2}$$

## Columnas inicial:

| Título | Descripción|
|:-------------------:|---|
|País|Nombre de los paises|
|Tipo_Energia|Tipo de energia: all_energy_types(Todas las energias), Carbón, Gas Natural, Nuclear, Petroleo, Energia renovable|
|Año|Año de registro|
|Consumo De Energía|Cantidad de consumo para la fuente de energía específica, medida  Btu|
|Producción De Energía|Cantidad de producción para la fuente de energía específica, medida Btu|
|Pib|Producto interno bruto basado en la paridad del poder adquisitivo del año 2015, medido en miles de millones|
|Población|Población total de país en terminos absolutos|
|Intensidad_Energética_Per_Capita|La intensidad energética es una medida de la ineficiencia energética de una economía. Se calcula como unidades de energía por unidad de habitante, medida MMBtu/persona|
|Intensidad_Energética_Por_Pib|La intensidad energética es una medida de la ineficiencia energética de una economía. Se calcula como unidades de energía por unidad de PIB, medido (1000 Btu/PIB)|
|Emisión De Co2|Emiciones de CO2 en Mt(tonelada metrica)|


<br>
<br>


## Observaciones: 
En primer lugar se cambiaron los nombres de las columnas para que queden todas en español.
Lugo se buscaron valores faltantes: 

| Columna                           | Valores Nulos |
| :---:                             | :-:           |
| Tipo_Energia                      |      0        |
| País                              |      0        |  
| Año                               |      0        |
| Consumo De Energía                |  11153        |
| Producción De Energía             |  11151        |
| Pib                               |  15414        |
| Población                         |   9426        |
| Intensidad_Energética_Per_Capita  |   5082        |
| Intensidad_Energética_Por_Pib     |   5082        |
| Emisión De Co2                    |   3826        |

Para reducir la cantidad de datos nulos, se utilizó otro dataset donde se encontró información sobre población y pbi. Luego de modificar las columnas antes dichas los valores nulos bajaron casi a la mitad: 

| Columna                           | Valores Nulos |
| :---:                             | :-:           |
| Pib                               |   9474        |
| Población                         |   4512        |

Además, los datos de la columna Población se modificaron a valores absolutos. 
Por último, para quedarnos con la cantidad mínima de valores nulos, se eliminaron los datos faltantes a partir de la columna “Emisión De Co2”, ya que es la más importante de la tabla. 

| Columna                           | Valores Nulos |
| :---:                             | :-:           |
|País                               |      0        |
|Tipo_Energia                       |      0        |
|Año                                |      0        |
|Consumo De Energía                 |   8591        |
|Producción De Energía              |   8591        |
|Pib                                |   7541        |
|Población                          |   3109        |
|Intensidad_Energética_Per_Capita   |   2490        |
|Intensidad_Energética_Por_Pib      |   2490        |
|Emisión De Co2                     |       0       |

Por último, cree cuatro columnas nuevas con los mismo valores de energía pero transformados a teravatios hora (TWh) para que coincida con los valores de las otras tablas.


## Columnas final:

| Título | Descripción|
|:-------------------:|---|
|País|Nombre de los paises|
|Tipo_Energia|Tipo de energia: all_energy_types(Todas las energias), Carbón, Gas Natural, Nuclear, Petroleo, Energia renovable|
|Año|Año de registro|
|Consumo De Energía|cantidad de consumo para la fuente de energía específica, medida  Btu|
|Producción De Energía|cantidad de producción para la fuente de energía específica, medida Btu|
|Pib|Producto bruto interno del pais en ese año en terminos absolutos|
|Población|Población total de país en terminos absolutos|
|Intensidad_Energética_Per_Capita|La intensidad energética es una medida de la ineficiencia energética de una economía. Se calcula como unidades de energía por unidad de habitante, medida MMBtu/persona|
|Intensidad_Energética_Por_Pib|La intensidad energética es una medida de la ineficiencia energética de una economía. Se calcula como unidades de energía por unidad de PIB, medido (1000 Btu/PIB)|
|Emisión De Co2|Emiciones de CO2 en Mt(tonelada metrica)|
|Consumo De Energía TWh|cantidad de consumo para la fuente de energía específica, medida  TWh|
|Producción De Energía TWh|cantidad de producción para la fuente de energía específica, medida TWh|
|Intensidad_Energética_Per_Capita TWh|La intensidad energética es una medida de la ineficiencia energética de una economía. Se calcula como unidades de energía por unidad de habitante, medida MMTWh/persona|
|Intensidad_Energética_Por_Pib TWh|La intensidad energética es una medida de la ineficiencia energética de una economía. Se calcula como unidades de energía por unidad de PIB, medido (TWh/PIB)|

<br>
<br>

