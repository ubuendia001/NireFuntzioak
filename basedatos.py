import pandas as pd
import numpy as np
import sqlite3
try:
    import pyodbc
except ModuleNotFoundError:
    print(f'No se ha podido importar el módulo pyodbc')

def leer_tabla_de_access(directorio_y_nombre_acess,nombre_tabla_consulta):
    """
    Esta función conecta con una base de datos access y extrae la información de una tabla o una consulta
    Importaciones necesarias:
        -import pyodbc
        -import pandas as pd.
    Parametros:
        -directorio_y_nombre_acess(str): directorio y nombre (con extensión) del archivo access.
        -nombre_tabla_consulta(string): Nombre de la tabla del access que se quiere leer.
    La función devuelve:
        -datos: dataframe de pandas con los datos de la tabla o consulta
    Ejemplo:
        directorio='I:/EIN00/10-Modelos/9-BD Certificación/BD Certificación - EJIE/Registro de Certificaciones.accdb'
    """
    conexion_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+directorio_y_nombre_acess+';')
    sentencia_sql= f"SELECT * FROM [{nombre_tabla_consulta}]"
    with pyodbc.connect(conexion_str) as conexion:
        datos=pd.read_sql(sentencia_sql,conexion)
    return datos

def leer_sentencia_sql_de_access(directorio_y_nombre_acess,sentencia_sql):
    """
    Esta función conecta con una base de datos access y extrae la información resultado de una sentencia sql.
    Importaciones necesarias:
        -import pyodbc
        -import pandas as pd.
    Parametros:
        -directorio_y_nombre_acess(str): directorio y nombre (con extensión) del archivo access.
        -sentencia_sql(string): Sentencia SQL que se quiere aplicar a la base de datos.
    La función devuelve:
        -datos: dataframe de pandas con los datos de consulta
    Ejemplo:
        directorio='I:/EIN00/10-Modelos/9-BD Certificación/BD Certificación - EJIE/Registro de Certificaciones.accdb'
    """
    conexion_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+directorio_y_nombre_acess+';')
    with pyodbc.connect(conexion_str) as conexion:
        datos=pd.read_sql(sentencia_sql,conexion)
    return datos


def leer_sentencia_sql_de_sqlite(directorio_y_nombre_DBsqlite,sentencia_sql):
    """
    Esta función conecta con una base de datos sqlite3 y extrae la información resultado de una sentencia sql.
    Importaciones necesarias:
        -import sqlite
        -import pandas as pd.
    Parametros:
        -directorio_y_nombre_DBsqlite(str): directorio y nombre (con extensión) de la base de datos sqlite3.
        -sentencia_sql(string): Sentencia SQL que se quiere aplicar a la base de datos.
    La función devuelve:
        -datos: dataframe de pandas con los datos de consulta
    Ejemplo:

    """
    conexion=sqlite3.connect(directorio_y_nombre_DBsqlite)
    datos=pd.read_sql(sentencia_sql,conexion)
    conexion.close()
    return datos
