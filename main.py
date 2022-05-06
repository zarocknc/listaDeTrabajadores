#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd

separador = '=' * os.get_terminal_size().columns
# importando la tabla de trabajadores actual 'df
df = pd.read_csv('Trabajadores.csv')
print(df) 
print(separador)

# Funcion para crear nuevos trabajadores y actualizar la tabla

def crearTrabajador():
    # Solicitando datos
    tname = input('Ingrese su nombre: ')
    tlastname = input('Ingrese sus apellidos: ')
    tage = int(input('ingrese su edad: '))
    tDNI = int(input('ingrese su DNI: '))
    # Creando dict con los datos obtenidos
    tworker = {
        'Nombre': tname,
        'Apellidos': tlastname,
        'Edad': tage,
        'DNI': tDNI
        }
    # Creando un dataframe con el dict
    workerframe = pd.DataFrame(tworker, index=[0]) # contatenando el dataframe y la tabla principal 'df'
    global result
    result = pd.concat([df, workerframe], ignore_index=True)

# Funcion de guardar los cambios realizados
def saveChanges():
    result.to_csv('Trabajadores.csv', index=False)
    sys.exit('adios, se guardaron los datos')

# Pregunta si desea crear un trabajador

def preguntar():
    ask = input('desea añadir un trabajador? Si / Guardar / MostrarCambios / Salir: ')
    if ask == 'Si':
        crearTrabajador()
        preguntar()
    elif ask == 'Guardar':
        saveChanges()
    elif ask == 'MostrarCambios':
        print(separador)
        print(result)
        print(separador)
        preguntar()
    else:
        sys.exit('adios ten un buen dia')

preguntar()
