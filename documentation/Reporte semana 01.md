# Reporte proyecto


## Funciones

---
### Carga de data a Mysql
```python
def cargaMySql (nombre, dataset):
    a = nombre
    nombre = dataset
        
    #Creacion de variables
    host_name,db_name, u_name, u_pass, port_num  = "localhost","proyecto_final", "root", "contraseña", "3306"
        
    #Conexion a la db
    mydb = mysql.connector.connect(
    host=host_name,
    user=u_name,
    password=u_pass,
    database=db_name )
    #Creacion del motor de base de datos
    engine = create_engine("mysql+mysqlconnector://" + u_name + ":" + u_pass + "@" + host_name + ":" + port_num + "/" + db_name, echo=False)
        
    #Importacion del dataframe a nuestra base de datos en SQL
    nombre.to_sql(name=a, con=engine, if_exists="append", index=False)
    return print('Carga exitosa')
```
---

### Funcion para Calidad de dato

```python
    def calidaDato (data):
        df = data
        calidad = []
        mascara = df.isna().sum()
        for i in range(0,len(mascara)):
            p = (df.shape[0]- mascara[i]) / df.shape[0]
            calidad.append([mascara.index[i], round((p*100),2)])
    
        calidad = pd.DataFrame(calidad)
        calidad.rename(columns={0:'Columna', 1: 'Calida %'}, inplace=True)
        
        return calidad
```

---

### Tabla de datos y calidad

|    | Columna                        |   Calida % |
|---:|:-------------------------------|-----------:|
|  0 | country                        |     100    |
|  1 | country_long                   |     100    |
|  2 | name                           |     100    |
|  3 | gppd_idnr                      |     100    |
|  4 | capacity_mw                    |     100    |
|  5 | latitude                       |     100    |
|  6 | longitude                      |     100    |
|  7 | primary_fuel                   |     100    |
|  8 | other_fuel1                    |       5.56 |
|  9 | other_fuel2                    |       0.79 |
| 10 | other_fuel3                    |       0.26 |
| 11 | commissioning_year             |      49.94 |
| 12 | owner                          |      59.73 |
| 13 | source                         |      99.96 |
| 14 | url                            |      99.95 |
| 15 | geolocation_source             |      98.8  |
| 16 | wepp_id                        |      46.47 |
| 17 | year_of_capacity_data          |      42.61 |
| 18 | generation_gwh_2013            |      18.37 |
| 19 | generation_gwh_2014            |      20.68 |
| 20 | generation_gwh_2015            |      23.48 |
| 21 | generation_gwh_2016            |      26.17 |
| 22 | generation_gwh_2017            |      27.19 |
| 23 | generation_gwh_2018            |      27.58 |
| 24 | generation_gwh_2019            |      27.65 |
| 25 | generation_data_source         |      32.63 |
| 26 | estimated_generation_gwh_2013  |      46.14 |
| 27 | estimated_generation_gwh_2014  |      47.24 |
| 28 | estimated_generation_gwh_2015  |      48.8  |
| 29 | estimated_generation_gwh_2016  |      50.29 |
| 30 | estimated_generation_gwh_2017  |      94.85 |
| 31 | estimated_generation_note_2013 |     100    |
| 32 | estimated_generation_note_2014 |     100    |
| 33 | estimated_generation_note_2015 |     100    |
| 34 | estimated_generation_note_2016 |     100    |
| 35 | estimated_generation_note_2017 |     100    |


---



