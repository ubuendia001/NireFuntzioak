import zipfile

def tabla_a_zip(datos, nombre_archivo="Archivo",nombre_carpeta='Datos', comprimir=True,incluir_index=True):
    """
    Esta función pasa un DataFrame a un archivo excel y lo mete en un archivo zip. Si se quiere se puede comprimir también.
    Importaciones necesarias:
        -import zipfile
    Parametros:
        -datos(pandas.DataFrame): DataFrame de pandas que se quiere pasar al zip.
        -nombre_archivo(string): Nombre (sin extensión) utilizado tanto para el excel como para el archivo zip comprimido. Por defecto 'Archivo'.
        -nombre_carpeta(string): Nombre que se le quiere da a la carpeta en la que irá el DataFrame dentro del archivo excel.
        -comprimir(True/False): ¿Se quiere comprimir el archivo? por defecto True.
    Hay distintos modos de compresión (compression): zipfile.ZIP_LZMA,zipfile.ZIP_BZIP2 y zipfile.ZIP_DEFLATED.
    Utilizamos el que más comprime, que es el zipfile.ZIP_LZMA

    """
    if comprimir == True:
        with zipfile.ZipFile(nombre_archivo+'_comprimido.zip', "w", compression=zipfile.ZIP_LZMA, compresslevel=9) as zf:  # zipfile.ZIP_LZMA
            with zf.open(nombre_archivo+".xlsx", "w") as buffer:
                with pd.ExcelWriter(buffer) as writer:
                    datos.to_excel(writer, sheet_name=nombre_carpeta,index=incluir_index)
    else:
        with zipfile.ZipFile(nombre_archivo+'_comprimido.zip', "w") as zf:
            with zf.open(nombre_archivo+".xlsx", "w") as buffer:
                with pd.ExcelWriter(buffer) as writer:
                    datos.to_excel(writer, sheet_name=nombre_carpeta,index=incluir_index)


def archivo_a_zip(archivo_nombre, zip_nombre='Archivo comprimido', comprimir=True):
    """
    Esta función mete cualquier archivo en un zip. Si se quiere se puede comprimir también.
    Importaciones necesarias:
        -import zipfile
    Parametros:
        -zip_nombre(string): Nombre (sin extensión) que se le quiere poner al archivo zip. Por defecto 'Archivo comprimido'.
        -archivo_nombre(string): Nombre del archivo que se quiere comprimir.
        -comprimir(True/False): ¿Se quiere comprimir el archivo? por defecto True.
    Hay distintos modos de compresión (compression): zipfile.ZIP_LZMA,zipfile.ZIP_BZIP2 y zipfile.ZIP_DEFLATED.
    Utilizamos el que más comprime, que es el zipfile.ZIP_LZMA
    """
    if comprimir == True:
        with zipfile.ZipFile(zip_nombre+'.zip', compression=zipfile.ZIP_LZMA, compresslevel=9, mode='w') as zf:
            zf.write(archivo_nombre)
    else:
        with zipfile.ZipFile(zip_nombre+'.zip', mode='w') as zf:
            zf.write(archivo_nombre)


def extraer_todo_de_zip(archivo_zip,directorio_objetivo):
    """
    Esta función extrae todos los archivos de archivo_zip al directorio_objetivo.
    Importaciones necesarias:
        -import zipfile.
    Parametros:
        -archivo_zip(string): Nombre (con extensión) del zip del que se quiere extraer todo.
        -directorio_objetivo(string): Directorio en el que queremos que se extraigan todos los archivos del zip
    """
    with zipfile.ZipFile(archivo_zip, 'r') as zf:
       zf.extractall(path=directorio_objetivo)

def extraer_archivo_de_zip(archivo_zip,archivo_a_extraer,directorio_objetivo):
    """
    Esta función extrae el archivo_a_extraer de archivo_zip al directorio_objetivo.
    Importaciones necesarias:
        -import zipfile.
    Parametros:
        -archivo_zip(string): Nombre (con extensión) del zip del que se quiere extraer todo.
        -archivo_a_extraer(string): Nombre (con extensión) del archivo que se quiere extraer.
        -directorio_objetivo(string): Directorio en el que queremos que se extraigan todos los archivos del zip

    """
    with zipfile.ZipFile(archivo_zip, 'r') as zipObj:
       zipObj.extract(member=archivo_a_extraer,path=directorio_objetivo)
