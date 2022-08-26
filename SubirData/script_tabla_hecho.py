import pandas as pd
import numpy as np
from script_Limpieza import _crearhash

df1 = pd.read_csv("./Normalizados/Normal_energyco2.csv")
pais = list(df1["País"].unique())

df2 = pd.read_csv("./Normalizados/Normal_sub-energy-fossil-renewables-nuclear.csv")
continente = list(df2[df2["Código"].isna() == True])

df3 = pd.read_csv("./Normalizados/Normal_gases.csv")
año = list(df2["Año"].unique())

tipo_ener = ['Biomass',
        'Coal',
        'Cogeneration',
        'Gas',
        'Geothermal',
        'Hydro',
        'Nuclear',
        'Oil',
        'Other',
        'Petcoke',
        'Solar',
        'Storage',
        'Waste',
        'Wave and Tidal',
        'Wind',
        'all energy types',
        'natural gas',
        'petroleum and other liquids',
        'nuclear',
        'renewables and other']

final = {
"Año":año,
"País":pais,
"Combustible":tipo_ener,
"Continente":continente
}

df_final = pd.DataFrame.from_dict(final, orient="index")
df_final = df_final.transpose()

for i in df_final.columns:
    df_final[i] = df_final[i].apply(lambda x: str(x))

_crearhash(df_final)
df_final.to_csv("./Normalizados/Tabla_Hecho.csv", index=False)
