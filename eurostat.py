import pandas as pd
import numpy as np
import requests
import json

def eurostat_jaitsi(codigo_tabla,**parametros):
    """
    Esta función descarga la información de la tabla seleccionada de EUROSTAT
    Importaciones necesarias:
        -import pandas as pd
        -import requests
        -import numpy as np
        -import json
    Parametros:
        -codigo_tabla(string):código de la tabla que se quiere descargar de Eurostat.
        -parametros: Parametros necesarios para la query
    Ejemplos:
        -eurostat_jaitsi('nrg_pc_'+'202',product='4100',format='JSON',freq='S',tax='I_TAX',consom='4141902',unit='KWH',currency='EUR')
    """

    mi_url='https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'+codigo_tabla
    mi_parametros=parametros

    bruto_respuesta=requests.get(url=mi_url,params=mi_parametros)
    json_respuesta=bruto_respuesta.json()
    valores=json_respuesta['value']

    datos=pd.DataFrame.from_dict(valores,orient='index',columns=['Valor'])
    datos.index=datos.index.astype('int')

    años=list(json_respuesta['dimension']['time']['category']['label'].keys())
    paises=list(json_respuesta['dimension']['geo']['category']['label'].values())
    paises_labur=list(json_respuesta['dimension']['geo']['category']['label'].keys())

    for indTemp in range(len(años)*len(paises)):
        if indTemp not in datos.index:
            datos.loc[indTemp,'Valor']=np.nan
    datos=datos.sort_index()

    columna_paises=[]
    columna_años=[]
    columna_paises_cod=[]
    for pais,pais_cod in zip(paises,paises_labur):
        for año in años:
            columna_años.append(año)
            columna_paises.append(pais)
            columna_paises_cod.append(pais_cod)
    datos['Año']=columna_años
    datos['País']=columna_paises
    datos['País_cod']=columna_paises_cod
    datos['Valor']=datos['Valor'].astype('float')
    return datos

