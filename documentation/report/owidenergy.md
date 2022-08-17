
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
|gdp|Total real gross domestic product, inflation-adjusted| 0.49 ||
|coal_prod_change_pct|Annual percentage change in coal production| 0.44 ||
|energy_per_capita|Primary energy consumption per capita| 0.46 |medida en kilovatios-hora|
|hydro_electricity|Electricity generation from hydropower| 0.41 |medido en teravatios-hora|
|low_carbon_electricity|Electricity generation from low-carbon sources| 0.41 |medido en teravatios-hora|
|nuclear_electricity|Electricity generation from nuclear power| 0.39 |medido en teravatios-hora|
|oil_prod_change_pct|Annual percentage change in oil production| 0.46 ||
|other_renewable_electricity|Electricity generation from other renewable sources including biofuels| 0.4 |medido en teravatios-hora|
|renewables_electricity|Electricity generation from renewables| 0.4 |medido en teravatios-hora|
|solar_electricity|Electricity generation from solar| 0.4 |medido en teravatios-hora|
|wind_electricity|Electricity generation from wind|0.4 |medido en teravatios-hora |

<br>
<br>

## Conclusion:
Despues de analizar 27 columnas de las 128, podemos llegar a las siguientes conclusiones:
- En la columna 'country', además de los países también se encuentran los continentes, y datos de países que ya no existen (como yugoslavia). Para esta situación usaremos la columna 'iso_code' como filtro, ya que se encuentran los codigos solo de los 219 países.
- Existen datos vacios por que no en todos los países se usan todos los tipos de energía(Solar,Nuclear, etc).

<br>
<br>

## Nueva tabla:

| Título | Descripción|datos validos | Comentarios |
|:-------------------:|---|---|---|
|country|| 1  |contiene paises,continentes y total|
|year||1 |datos hasta el 2021|
|iso_code|ISO 3166-1 alpha3| 0.73 |existen 219 tipos de codigos, puede usarse como filtro para buscar solo paises|
|population|Numero de habitantes| 0.8 ||
|coal_production|||
|gas_production|||
|oil_production|||
|biofuel_consumption|||
|coal_consumption|||
|fossil_fuel_consumption|||
|gas_consumption|||
|hydro_consumption|||
|low_carbon_consumption|||
|nuclear_consumption|||
|oil_consumption|||
|other_renewable_consumption|||
|primary_energy_consumption|||
|renewables_consumption|||
|solar_consumption|||
|wind_consumption|||