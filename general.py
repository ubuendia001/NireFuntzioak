import os
import shutil
import urllib.request as req
import ssl
import datetime


misColores=['salmon','skyblue','orange','green','darkgrey','mediumorchid','lime','tan','navy','maroon','blue','red']

coloresEVE={'VerdeEVE':(93,163,102),'AzulEVE':(0,93,181),'NegroEVE':(26,23,27),'GrisEVE':(238,238,238),
            'Industria': (114,199,216),'Transporte':(239,122,152),'Primario':(169,197,165),'Servicios':(254,208,99),'Residencial':(198,143,191),'Generación eléctrica':(244,154,115),
            'Petróleo y derivados':(215,185,191),'Carbón y derivados':(136,159,155),'Gas natural':(189,227,242),'Energías derivadas':(241,239,173),'Renovables':(167,205,118),'Electricidad':(119,157,79),
            'Eólica':(163,196,206),'Fotovoltaica':(250,187,105),'Hidroeléctrica':(114,199,216),'Biomasa':(199,214,168),'Biocarburantes':(224,195,148),'Solar':(255,232,122),'Térmicas avanzadas':(185,165,167),'Térmicas convencionales':(228,198,150),'Cogeneración':(248,192,186),'Geotérmica':(160,181,213),'Marina':(81,169,189)}


def descargar_archivo(url,ubicacion):
    """
    Esta función se descarga el archivo desde la web y lo guarda en una ubicación específica.
    A veces la página no deja utilizar estas aplicaciones, para esto, por si acaso introducimos la fila de SSL.
    Importaciones necesarias:
        -import urllib.request as req.
        -import ssl
    Parametros:
        -url(string):Dirección URL desde donde descargar el archivo
        -ubicacion(string): Directorio completo donde se quiere guardar el archivo descargado.

    Ejemplo:
    ubicacion='C:/Users/urkob/OneDrive - Ente Vasco de la Energia/CORES/consumos-pp-ccaa-provincias.xlsx'
    url='https://www.cores.es/sites/default/files/archivos/estadisticas/consumos-pp-ccaa-provincias.xlsx'
    descargar_archivo(url, ubicacion)
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    request = req.urlretrieve(url, ubicacion)

def copiaSeguridad(rutaYnombreArchivo,rutaNueva=None):
    """
    Esta función hace una copia de seguridad del archivo indicado con la fecha del día al principio del nombre.
    Si se indica una nueva ruta, se copiará en esa nueva ruta, en caso contrario se hará la copia en el mismo directorio del archivo original.
    Importaciones necesarias:
        -import datetime
        -import shutil
        -import os
    Parámetros:
        -rutaYnombreArchivo(string): Ruta y nombre del archivo que se quiere copiar.
        -rutaNueva(string): Nuevo directorio donde guardar la copia. Por defecto None.
    Ejemplo:
        -copiaSeguridad('C:/Users/urkob/Desktop/__init__.py','./Copias de seguridad/')
    """

    rutaYnombreArchivo=rutaYnombreArchivo.replace('\\','/')
    ruta,nombreArchivo=os.path.split(rutaYnombreArchivo)
    nombreArchivoNuevo=datetime.date.today().strftime(format='%Y%m%d')+'_'+nombreArchivo
    if rutaNueva != None:
        rutaNueva=rutaNueva.replace('\\','/')
        try:
            shutil.copy(rutaYnombreArchivo,os.path.join(rutaNueva,nombreArchivoNuevo))
            print('Copia realizada correctamente')
        except FileNotFoundError:
            print('El archivo o la nueva ruta no son correctos')
    else:
        try:
            shutil.copy(rutaYnombreArchivo,os.path.join(ruta,nombreArchivoNuevo))
            print('Copia realizada correctamente')
        except FileNotFoundError:
            print('El archivo con la ruta indicada no existe')
