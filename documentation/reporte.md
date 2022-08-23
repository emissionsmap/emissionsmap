# funciones
    coneccion a MySql
    porcentaje de calidad de datos


# Nombre de las columnas, con el porcentaje de informacio en cada una  y  refeencia

indice	Columna	Calida %	Esp
0	country	100.00
1	country_long	100.00
2	name	100.00
3	gppd_idnr	100.00
4	capacity_mw	100.00
5	latitude	100.00
6	longitude	100.00
7	primary_fuel	100.00
8	other_fuel1	5.56
9	other_fuel2	0.79
10	other_fuel3	0.26
11	commissioning_year	49.94
12	owner	59.73
13	source	99.96
14	url	99.95
15	geolocation_source	98.80
16	wepp_id	46.47
17	year_of_capacity_data	42.61
18	generation_gwh_2013	18.37
19	generation_gwh_2014	20.68
20	generation_gwh_2015	23.48
21	generation_gwh_2016	26.17
22	generation_gwh_2017	27.19
23	generation_gwh_2018	27.58
24	generation_gwh_2019	27.65
25	generation_data_source	32.63
26	estimated_generation_gwh_2013	46.14
27	estimated_generation_gwh_2014	47.24
28	estimated_generation_gwh_2015	48.80
29	estimated_generation_gwh_2016	50.29
30	estimated_generation_gwh_2017	94.85
31	estimated_generation_note_2013	100.00
32	estimated_generation_note_2014	100.00
33	estimated_generation_note_2015	100.00
34	estimated_generation_note_2016	100.00
35	estimated_generation_note_2017	100.00

# creacion de tabla master de global de plantas de energia por pais (archiv csv)

tabla_global_planta_energia = data02[['country', 'country_long', 'primary_fuel']]

tabla_global_planta_energia = data02[['country', 'country_long', 'primary_fuel']]

tabla_global_planta_energia.to_csv('master_global_planta_energia.csv')

Columna	Calida %
0	country	100.00
1	country_long	100.00
2	name	100.00
3	gppd_idnr	100.00
4	capacity_mw	100.00
5	latitude	100.00
6	longitude	100.00
7	primary_fuel	