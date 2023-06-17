import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def descargarImagen(url,nombre_archivo):
    """
    Esta función descarga la imagen de una url indicada en la carpeta 'ImágenesDescargadas'.
    Si esta carpeta no existe en el directorio actual, la crea.
    Importaciones necesarias:
        -import requests
        -import os
    Parametros:
        -url(string):URL donde está la .
        -nombre_archivo(string): Nombre (con extensión) con el que queremos que se guarde el archivo
    """
    imagen=requests.get(url)

    if not os.path.isdir('ImágenesDescargadas'):
        os.mkdir('ImágenesDescargadas')

    with open('./ImágenesDescargadas/'+nombre_archivo,'wb') as archivo:
        archivo.write(imagen.content)


def descargarImagenesDeConcepto(concepto_buscar,num_imagenes,extension='png'):
    """
    Esta función descarga un número de imágenes sobre el concepto que se indique y en el formato indicado.
    Para ello, busca en google imágenes y descarga los primeros resultados.
    Las imágenes se descargan en la carpeta 'ImágenesDescargadas'.
    Si esta carpeta no existe en el directorio actual, la crea.
    Importaciones necesarias:
        -from selenium import webdriver
        -from selenium.webdriver.common.keys import Keys
        -import time
    Parámetros:
        -concepto_buscar(string):texto que se busca en google imágenes.
        -num_imagenes(int): Número de imágenes que se quiere descargar.
        -extension(string): texto de la extensión que queremos para las imágenes de descarga. Por defecto 'png'
    Ejemplo:
        -descargarImagenesDeConcepto('Euskal herria bandera',3)
    """

    PATH_etxean = 'C:\Program Files (x86)\Google\Chrome\chromedriver.exe'
    PATH_lanean = "C:\\Users\\EOFUB\\Desktop\\chromedriver.exe"
    try:
        driver = webdriver.Chrome(PATH_etxean)
    except FileNotFoundError:
        driver = webdriver.Chrome(PATH_lanean)

    #Entrar a google imágenes
    driver.get('https://www.google.es/imghp?hl=es')
    time.sleep(1)

    #Aparece un menú sobre normativa de google que hay que aceptar
    btn_aceptar=driver.find_element_by_id('L2AGLb')
    btn_aceptar.click()
    time.sleep(1)

    #Buscamos el concepto a través de la barra de busqueda de google imágenes
    buscador=driver.find_element_by_name('q')
    buscador.send_keys(concepto_buscar)
    buscador.send_keys(Keys.RETURN)

    #Para obtener el URL donde está la imagen hay que pinchar primero sobre la  y cuando se ha abierto a la derecha, obtener el src.
    #Para descargar varias imágenes hay que hacer un ciclo entre los resultados.
    numero=1
    imagenesDescargadas=1
    while imagenesDescargadas<=num_imagenes:
        try:
            btn_foto=driver.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/div[{numero}]')
            btn_foto.click()
            time.sleep(1)

            imagen_drch=driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
            link_imagen=imagen_drch.get_attribute("src")
            print(link_imagen)
            descargarImagen(link_imagen,concepto_buscar+str(numero)+'.'+extension)
            print('Descargada  número: '+ str(imagenesDescargadas))
            imagenesDescargadas+=1
            numero+=1
        except:
            #Si alguna imagen no tiene src que pase al siguiente resultado de google.
            numero+=1
            pass

    driver.quit()
