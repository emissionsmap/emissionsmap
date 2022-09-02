
# $$\text{Reporte para el csv: owid-energy-consumption-source}$$

## Columnas con datos validados mayor o igual al 50%:

| Título | Descripción|datos validos | Comentarios |
|:-------------------:|---|---|---|
|country|| 1  |contiene paises,continentes y total|
|year||1 |datos hasta el 2021|
|iso_code|ISO 3166-1 alpha3| 0.73 |existen 219 tipos de codigos, puede usarse como filtro para buscar solo paises|
|population|Numero de habitantes| 0.8 ||
|coal_prod_change_twh|Variación anual de la producción de carbón| 0.74 |medida en teravatios-hora|
|coal_prod_per_capita|Producción de carbón per cápita| 0.65 | medida en kilovatios-hora|
|coal_production|Producción de carbón| 0.75 |medida en teravatios-hora|
|energy_cons_change_pct|Variación porcentual anual del consumo de energía primaria| 0.55 ||
|energy_cons_change_twh|Cambio anual en el consumo de energía primaria| 0.56 |medido en teravatios-hora|
|gas_prod_change_twh|Cambio anual en la producción de gas| 0.76 |medido en teravatios-hora|
|gas_prod_per_capita|Producción de gas per cápita| 0.66 |medida en kilovatios-hora|
|gas_production|Producción de gas| 0.77 |medida en teravatios-hora|
|oil_prod_change_twh|Cambio anual en la producción de petróleo| 0.79 |medido en teravatios-hora|
|oil_prod_per_capita|Producción de petróleo per cápita| 0.68 |medida en kilovatios-hora|
|oil_production|Producción de petróleo| 0.8 |medida en teravatios-hora|
|primary_energy_consumption|Primary energy consumption| 0.57 |medido en teravatios-hora|

<br>
<br>

## Columnas con datos validados mayor al 39% y menor al 50%:

| Título | Descripción|datos validos | Comentarios |
|:-------------------:|---|---|---|
|gdp|Producto interno bruto real total| 0.49 |ajustado por inflación|
|coal_prod_change_pct|Cambio porcentual anual en la producción de carbón| 0.44 ||
|energy_per_capita|Consumo de energía primaria per cápita| 0.46 |medida en kilovatios-hora|
|hydro_electricity|Generación de electricidad a partir de energía hidroeléctrica| 0.41 |medido en teravatios-hora|
|low_carbon_electricity|Generación de electricidad a partir de fuentes bajas en carbono| 0.41 |medido en teravatios-hora|
|nuclear_electricity|Generación de electricidad a partir de la energía nuclear| 0.39 |medido en teravatios-hora|
|oil_prod_change_pct|Cambio porcentual anual en la producción de petróleo| 0.46 ||
|other_renewable_electricity|Generación de electricidad a partir de otras fuentes renovables, incluidos los biocombustibles| 0.4 |medido en teravatios-hora|
|renewables_electricity|Generación de electricidad a partir de renovables| 0.4 |medido en teravatios-hora|
|solar_electricity|Generación de electricidad a partir de energía solar.| 0.4 |medido en teravatios-hora|
|wind_electricity|Generación de electricidad a partir del viento|0.4 |medido en teravatios-hora |

<br>
<br>

## Conclusion:
Despues de analizar 27 columnas de las 128, podemos llegar a las siguientes conclusiones:
- En la columna 'country', además de los países también se encuentran los continentes, y datos de países que ya no existen (como yugoslavia). Para esta situación usaremos la columna 'iso_code' como filtro, ya que se encuentran los codigos solo de los 219 países.
- Existen datos vacios por que no en todos los países se usan todos los tipos de energía(Solar,Nuclear, etc). Una manera de imputar los valores nulos es cambiandolos por "0", ya que eso indicaría que para tal país que no produzca dicho tipo de energía sea cero.
- Las columnas de energías fósiles:
    - fossil_electricity = oil_electricity  + coal_electricity + gas_electricity
- Las columnas de energías renovables:
    - renewables_electricity = wind_electricity + solar_electricity + hydro_electricity + other_renewable_electricity

<br>
<br>

## Nueva tabla:

| Título | Descripción|Comentarios |
|:-------------------:|---|---|
|year||datos hasta el 2021|
|country||contiene paises,continentes y total|
|population|||
|iso_code|ISO 3166-1 alpha3|219 tipos de codigos, solo paises|
|gdp|Producto interno bruto real total|ajustado por inflación|
|carbon_intensity_elec|Intensidad de carbono de la producción de electricidad|medida en gramos de dióxido de carbono emitido por kilovatio-hora|<!-- emisiones de gases de efecto invernadero -->
|greenhouse_gas_emissions|Emisiones de gases de efecto invernadero producidas en la generación de electricidad|medidas en millones de toneladas de CO2 equivalente|<!----------no renovables----fosiles -->
|oil_electricity|Energía no renovable fósil|medidas en teravatios-hora|
|oil_consumption|Energía no renovable fósil|medidas en teravatios-hora|
|coal_electricity|Energía no renovable fósil|medidas en teravatios-hora|
|coal_consumption|Energía no renovable fósil|medidas en teravatios-hora|
|gas_electricity|Energía no renovable fósil|medidas en teravatios-hora|
|gas_consumption|Energía no renovable fósil|medidas en teravatios-hora|<!-- no renovables-- nuclear-->
|nuclear_electricity|Energía no renovable nuclear|medidas en teravatios-hora|
|nuclear_consumption|Energía no renovable nuclear|medidas en teravatios-hora|<!------------------ renovables ----------------------->
|hydro_electricity|Energía renovable|medidas en teravatios-hora|
|hydro_consumption|Energía renovable|medidas en teravatios-hora|
|solar_electricity|Energía renovable|medidas en teravatios-hora|
|solar_consumption|Energía renovable|medidas en teravatios-hora|
|wind_electricity|Energía renovable|medidas en teravatios-hora|
|wind_consumption|Energía renovable|medidas en teravatios-hora|
|other_renewable_electricity|Energía renovable|medidas en teravatios-hora|
|other_renewable_consumption|Energía renovable|medidas en teravatios-hora|

<br>
<br>

## otras columnas que pueden ser de uso:
| Título | Descripción|Comentarios |
|:-------------------:|---|---|
|energy_cons_change_pct|Cambio porcentual anual en el consumo de energía primaria||
|energy_per_gdp|Consumo de energía por unidad de PIB| Esto se mide en kilovatios-hora por $ internacional de 2011|
|net_elec_imports|Importaciones netas de electricidad| medidas en teravatios-hora|