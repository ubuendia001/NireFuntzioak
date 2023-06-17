import pandas as pd
import numpy as np
import os
import json

def gisEuropa(nombre,datos,columnaID,columnasMostrar,nivel='Paises'):
    """
    Esta función crea un geojson (para hacer mapas en Qgis) a partir de los ID de los Paises/CCAA/Provincia y las columnas que queramos mostrar.
    El id de los paises/CCAA/provincia es el empleado por eurostat.
    El geojson lo guarda en formato txt en el Onedrive/GIS/GIS-EUROPA/.
    Importaciones necesarias:
        -import pandas as pd
        -import os
        -import json
    Parametros:
        -nivel(string): tres niveles posibles (Paises, CCAA, Provincia)
        -nombre(string):nombre del archivo geojson (sin extensión).
        -datos(pandas DataFrame): tabla con los datos que queremos que se muestren en el mapa
        -columnsID(str):columna del dataframe datos que tiene el dato del ID del país
        -columnasMostrar(lista)=lista de columnas que queremos mostrar en el mapa
    Ejemplos:
        -gisEuropa('IndicadorRenovableTransporte',df,'ID',['Renovables en transporte 2020'])
    """
    PATH_etxean = "C:/Users/urkob/OneDrive - Ente Vasco de la Energia/GIS/GIS-EUROPA/"
    PATH_lanean = "C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/GIS/GIS-EUROPA/"
    if os.path.isdir(PATH_etxean):
        directorio=PATH_etxean
    elif os.path.isdir(PATH_lanean):
        directorio=PATH_lanean
    else:
        print('No está el directorio')

    with open(directorio+f'Plantillas/Plantilla3035{nivel}.txt',mode='r',encoding='utf-8',errors='ignore') as geojson:
        plantillaGeojson=json.load(geojson)
    with open(directorio+'/'+nombre+f'3035{nivel}.txt',mode='w',encoding='utf-8',errors='ignore') as geojsonNuevo:
        for fila in plantillaGeojson['features']:
            for columnaMostrar in columnasMostrar:
                try:
                    fila['properties'][columnaMostrar]=float(datos.loc[datos[columnaID]==fila['properties']['NUTS_ID'],columnaMostrar].values[0])
                except ValueError:
                    fila['properties'][columnaMostrar] = str(datos.loc[datos[columnaID]==fila['properties']['NUTS_ID'],columnaMostrar].values[0])
                except IndexError:
                    print('No se ha encontrado valor para: '+ fila['properties']['NUTS_ID'])
        json.dump(plantillaGeojson,geojsonNuevo)

def gisEspaña(nombre, datos, columnaID, columnasMostrar):
    """
    Esta función crea un geojson (para hacer mapas en Qgis) a partir de los ID de las comunidades autónomas de España y las columnas que queramos mostrar.
    El id de las CCAA es el empleado por el INE.
    El geojson lo guarda en formato txt en el Onedrive/GIS/GIS-ESPAÑA/.
    Importaciones necesarias:
        -import pandas as pd
        -import os
        -import json
    Parametros:
        -nombre(string):nombre del archivo geojson (sin extensión).
        -datos(pandas DataFrame): tabla con los datos que queremos que se muestren en el mapa
        -columnsID(str):columna del dataframe datos que tiene el dato del ID de la CCAA
        -columnasMostrar(lista)=lista de columnas que queremos mostrar en el mapa
    Ejemplos:
        -gisEspaña('IndicadorRenovableTransporte',df,'ID',['Renovables en transporte 2020'])
    """
    PATH_etxean = "C:/Users/urkob/OneDrive - Ente Vasco de la Energia/GIS/GIS-ESPAÑA/"
    PATH_lanean = "C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/GIS/GIS-ESPAÑA/"
    if os.path.isdir(PATH_etxean):
        directorio = PATH_etxean
    elif os.path.isdir(PATH_lanean):
        directorio = PATH_lanean

    with open(directorio + 'Plantillas/plantillaCCAAEspaña.txt', mode='r', encoding='utf-8', errors='ignore') as geojson:
        plantillaGeojson = json.load(geojson)
    with open(directorio + '/' + nombre + 'ETRS89CCAA.txt', mode='w', encoding='utf-8',errors='ignore') as geojsonNuevo:
        for fila in plantillaGeojson['features']:
            for columnaMostrar in columnasMostrar:
                try:
                    fila['properties'][columnaMostrar] = float(datos.loc[datos[columnaID] == fila['properties']['acom_code'], columnaMostrar].values[0])
                except ValueError:
                    fila['properties'][columnaMostrar] = str(datos.loc[datos[columnaID] == fila['properties']['acom_code'], columnaMostrar].values[0])
                except IndexError:
                    print('No se ha encontrado valor para: '+ fila['properties']['acom_code'])
        json.dump(plantillaGeojson, geojsonNuevo)

def gisEuskadi(nombre, datos, columnaID, columnasMostrar):
    """
    Esta función crea un geojson (para hacer mapas en Qgis) a partir de los códigos de lo municipios de Euskadi y las columnas que queramos mostrar.
    El geojson lo guarda en formato txt en el Onedrive/GIS/GIS-MUNICIPAL/.
    Importaciones necesarias:
        -import pandas as pd
        -import os
        -import json
    Parametros:
        -nombre(string):nombre del archivo geojson (sin extensión).
        -datos(pandas DataFrame): tabla con los datos que queremos que se muestren en el mapa
        -columnsID(str):columna del dataframe datos que tiene el dato del código del municipio
        -columnasMostrar(lista)=lista de columnas que queremos mostrar en el mapa

    """
    PATH_etxean = "C:/Users/urkob/OneDrive - Ente Vasco de la Energia/GIS/GIS-MUNICIPAL/"
    PATH_lanean = "C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/GIS/GIS-MUNICIPAL/"
    if os.path.isdir(PATH_etxean):
        directorio = PATH_etxean
    elif os.path.isdir(PATH_lanean):
        directorio = PATH_lanean

    with open(directorio + 'Plantillas/Municipios.geojson', mode='r', encoding='utf-8', errors='ignore') as geojson:
        plantillaGeojson = json.load(geojson)
    with open(directorio + '/' + nombre + '.txt', mode='w', encoding='utf-8',errors='ignore') as geojsonNuevo:
        for fila in plantillaGeojson['features']:
            for columnaMostrar in columnasMostrar:
                try:
                    fila['properties'][columnaMostrar] = float(datos.loc[datos[columnaID] == fila['properties']['EUSTAT'], columnaMostrar].values[0])
                except ValueError:
                    fila['properties'][columnaMostrar] = str(datos.loc[datos[columnaID] == fila['properties']['EUSTAT'], columnaMostrar].values[0])
                except IndexError:
                    print('No se ha encontrado valor para: '+ fila['properties']['EUSTAT'])
        json.dump(plantillaGeojson, geojsonNuevo)
