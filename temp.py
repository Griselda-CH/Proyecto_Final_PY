# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np

datos={'Nombre':['julio','leo','pepe'],'Calificaciones':['95','90','85'],
       'Deportes':['natacion','futbol','basquetbol'],'Materias':['calculo','programacion','quiminca']}

df= pd.DataFrame(datos)
print(df)
print('\n'*3)

datos2={'Nombre':['julio','julio','N/A'],'Calificaciones':['100','90', np.nan],
       'Deportes':['natacion','futbol','futbol'],'Materias':['calculo','programacion','programacion']}

df2= pd.DataFrame(datos2)
nuevo= pd.DataFrame(df)
print(df2)
print('\n'*2)
print(df2.info())
print('\n'*4)
print(df2.describe())
print('\n'*4)
nuevo2= pd.DataFrame(df2)
print(nuevo)

nuevo2= pd.DataFrame(df2)
nuevo2= nuevo2.dropna(how= 'any', inplace=True)
print(nuevo2)
print('\n'*4)
columna= df2[df2['Nombre']!="N/A"]
print(columna)
print('\n'*4)
nuevo3= pd.DataFrame(df2)
nuevo3.fillna(0,inplace=True)
print(nuevo3.describe())
print('\n'*4)
nuevo['Calificaciones']= nuevo.Calificaciones.astype(int)
print(nuevo.describe())

print("El promedio de notas es: ", nuevo['Calificaciones'].mean())
