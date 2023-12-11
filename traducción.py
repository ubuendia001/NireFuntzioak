import pandas as pd
import sqlite3
import os

#Nos conectamos con la base de datos donde están todas las palabra y sus traducciones
PATH_etxean = "C:/Users/urkob/OneDrive - Ente Vasco de la Energia/HIZTEGIA/Hiztegia.db"
PATH_lanean = "C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/HIZTEGIA/Hiztegia.db"
if os.path.isfile(PATH_etxean):
    directorio=PATH_etxean
elif os.path.isfile(PATH_lanean):
    directorio=PATH_lanean

conn=sqlite3.connect(directorio)
hiztegiaDF=pd.read_sql('SELECT * FROM HIZTEGIA',con=conn)
conn.close()

def traducirEuskera(palabra):
    '''
    Traduce al euskera cualquier palabra en castellano
    '''
    try:
        if pd.isna(palabra):
            return pd.NA
        #Para que no afecte si hay letras en mayúsculas, ponemos siempre el capitalize 
        traduccion=hiztegiaDF.loc[hiztegiaDF['Palabra']==palabra.capitalize(),'Hitza'].values[0]
        return traduccion
    except Exception as e:
        print(e)
        # print(f'Ha habido algún problema con la palabra {palabra}')
        return palabra


def traducirIngles(palabra):
    '''
    Traduce al inglés cualquier palabra en castellano
    '''
    try:
        if pd.isna(palabra):
            return pd.NA
        #Para que no afecte si hay letras en mayúsculas, ponemos siempre el capitalize 
        traduccion=hiztegiaDF.loc[hiztegiaDF['Palabra']==palabra.capitalize(),'Word'].values[0]
        return traduccion
    except Exception as e:
        print(e)
        # print(f'Ha habido algún problema con la palabra {palabra}')
        return palabra


