import pandas as pd

directorio_nireFuntzioak_EVE = 'C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/NIRE FUNTZIOAK/'
directorio_nireFuntzioak_CASA = 'C:/Users/urkob/OneDrive - Ente Vasco de la Energia/NIRE FUNTZIOAK/'


try:
    municipios_convertidor = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='Convertidor', dtype='str')
    comarca_convertidor = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='ConvertidorComarcas', dtype='str')
    tabla_municipios = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='Nombres_oficiales', dtype='str')
    tabla_municipios.set_index('MunicipioCodigoOficial', inplace=True)
    tabla_comarcas_municipios = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='ComarcasCodigos', dtype='str')
    tabla_comarcas_municipios.set_index('MunicipioCodigo',inplace=True)
    tabla_comarcas = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='Nombres_oficiales_comarcas', dtype='str')
    tabla_comarcas.set_index('ComarcaCodigo', inplace=True)
    CCAA_convertidor = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='ConvertidorESP_CCAA', dtype='str')
    tabla_CCAA = pd.read_excel(directorio_nireFuntzioak_EVE+'Convertidor.xlsx', sheet_name='ESP_CCAA_oficiales', dtype='str',header=0,usecols=['CCAA_cod','Nombre_recortado'])
    tabla_CCAA.set_index('CCAA_cod', inplace=True)
except FileNotFoundError:
    municipios_convertidor = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='Convertidor', dtype='str')
    comarca_convertidor = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='ConvertidorComarcas', dtype='str')
    tabla_municipios = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='Nombres_oficiales', dtype='str')
    tabla_municipios.set_index('MunicipioCodigoOficial', inplace=True)
    tabla_comarcas_municipios = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='ComarcasCodigos', dtype='str')
    tabla_comarcas_municipios.set_index('MunicipioCodigo',inplace=True)
    tabla_comarcas = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='Nombres_oficiales_comarcas', dtype='str')
    tabla_comarcas.set_index('ComarcaCodigo', inplace=True)
    CCAA_convertidor = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='ConvertidorESP_CCAA', dtype='str')
    tabla_CCAA = pd.read_excel(directorio_nireFuntzioak_CASA+'Convertidor.xlsx', sheet_name='ESP_CCAA_oficiales', dtype='str',header=0,usecols=['CCAA_cod','Nombre_recortado'])
    tabla_CCAA.set_index('CCAA_cod', inplace=True)


def arreglar_municipio(nombre_mal):
    """
    Esta función devuelve un string con el código oficial del municipio introducido con el nombre mal escrito.
    Devuelve un '0' si no lo encuentra, en tal caso, hay que introducir en la pestaña 'Convertidor' del excel
    'Convertidor.xlsx' esta manera de escribir el municipio mal y su código correcto.
    Importaciones necesarias:
        -El DataFrame denominado 'municipios_convertidor'. municipios_convertidor = pd.read_excel('Convertidor.xlsx', sheet_name='Convertidor', dtype='str').
    Parametros:
        -nombre_mal(string): string con el nombre del municipio mal escrito
    """
    try:
        return str(municipios_convertidor.loc[municipios_convertidor['MunicipioNombre'] == nombre_mal, 'MunicipioCod'].values[0])
    except:
        return '0'

def arreglar_comarca(nombre_mal):
    """
    Esta función devuelve un string con el código oficial de la comarca introducido con el nombre mal escrito.
    Devuelve un '0' si no lo encuentra, en tal caso, hay que introducir en la pestaña 'ConvertidorComarcas' del excel
    'Convertidor.xlsx' esta manera de escribir el municipio mal y su código correcto.
    Importaciones necesarias:
        -El DataFrame denominado 'comarca_convertidor'. comarca_convertidor = pd.read_excel('Convertidor.xlsx', sheet_name='ConvertidorComarcas', dtype='str').
    Parametros:
        -nombre_mal(string): string con el nombre de la comarca mal escrita
    """
    try:
        return str(comarca_convertidor.loc[comarca_convertidor['ComarcaNombre'] == nombre_mal, 'ComarcaCodigo'].values[0])
    except:
        return '0'

def arreglar_CCAA(nombre_mal):
    """
    Esta función devuelve un string con el código oficial de la comunidad autónoma introducido con el nombre mal escrito.
    Devuelve un '0' si no lo encuentra, en tal caso, hay que introducir en la pestaña 'ConveridorESP_CCAA' del excel
    'Convertidor.xlsx' esta manera de escribir la CCAA mal y su código correcto.
    Importaciones necesarias:
        -El DataFrame denominado 'CCAA_convertidor'. CCAA_convertidor = pd.read_excel('Convertidor.xlsx', sheet_name='ConvertidorESP_CCAA', dtype='str').
    Parametros:
        -nombre_mal(string): string con el nombre de la CCAA mal escrita
    """
    try:
        return str(CCAA_convertidor.loc[CCAA_convertidor['CCAA_nombre_mal'] == nombre_mal, 'CCAA_cod'].values[0])
    except:
        return '0'

def nombre_municipio(codigo):
    """
    Esta función devuelve un string con el nombre oficial del municipio introducido con el código oficial.
    Importaciones necesarias:
        -El DataFrame denominado 'tabla_municipios':
            tabla_municipios = pd.read_excel('Convertidor.xlsx', sheet_name='Nombres_oficiales', dtype='str')
            tabla_municipios.set_index('MunicipioCodigo', inplace=True)
    Parametros:
        -codigo(string): string con el código oficial del municipio
    """
    try:
        return tabla_municipios.loc[str(codigo), 'MunicipioNombreOficial']
    except:
        return '0'

def nombre_comarca(codigo):
    """
    Esta función devuelve un string con el nombre de la comarca del municipio utilizando el código del municipio.
    Parametros:
        -codigo(string): string con el código oficial del municipio
    """
    try:
        codigoComarca=tabla_comarcas_municipios.loc[str(codigo),'ComarcaCodigo']
        return tabla_comarcas.loc[codigoComarca, 'ComarcaNombreOficial']
    except:
        return '0'

def nombre_TTHH(codigo):
    """
    Esta función devuelve un string con el nombre del TTHH utilizando el código del municipio.
    Importaciones necesarias:
        -El DataFrame denominado 'tabla_municipios':
            tabla_municipios = pd.read_excel(
                'Convertidor.xlsx', sheet_name='Nombres_oficiales', dtype='str')
            tabla_municipios.set_index('MunicipioCodigo', inplace=True)
    Parametros:
        -codigo(string): string con el código oficial del municipio
    """
    try:
        return tabla_municipios.loc[str(codigo), 'TTHH']
    except:
        return '0'


def nombre_CCAA(codigo):
    """
    Esta función devuelve un string con el nombre oficial de la CCAA introducido con el código oficial.
    Importaciones necesarias:
        -El DataFrame denominado 'tabla_municipios':
            tabla_CCAA = pd.read_excel('Convertidor.xlsx', sheet_name='ESP_CCAA_oficiales', dtype='str')
            tabla_CCAA.set_index('CCAA_cod', inplace=True)
    Parametros:
        -codigo(string): string con el código oficial de la CCAA
    """
    try:
        return tabla_CCAA.loc[codigo, 'Nombre_recortado']
    except:
        return '0'
