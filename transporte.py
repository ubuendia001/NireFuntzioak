import pandas as pd
import numpy as np
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def dgt_descargar(años,meses,tipo='Matriculaciones'):
    """
    Esta función descarga los microdatos del portal estadístico de la DGT.
    Importaciones necesarias:
        -import pandas as pd
        -import numpy as np
        -from selenium import webdriver
        -from selenium.webdriver.support.ui import Select
        -import time
        -import os
    Parámetros:
        -año(lista): Años de los que se quiere descargar los microdatos.
        -meses(lista): Meses de los que se quiere descargar los microdatos.
        -tipo(string): Matriculaciones o Bajas. Descargar microdatos de matriculaciones o bajas. Por defecto Matriculaciones.
    """
    #Entrar a DGT
    PATH_etxean = "C:/Program Files (x86)/Google/Chrome/chromedriver.exe"
    PATH_lanean = "C:/Users/EOFUB/Desktop/chromedriver.exe"
    if os.path.isfile(PATH_etxean):
        directorio_chrome=PATH_etxean
    elif os.path.isfile(PATH_lanean):
        directorio_chrome=PATH_lanean
    driver = webdriver.Chrome(directorio_chrome)

    try:
        driver.get('https://sedeapl.dgt.gob.es/WEB_IEST_CONSULTA/')
        time.sleep(2)

        #Click en vehículos a la izquierda
        btn_vehiculos=driver.find_element(By.XPATH,'/html/body/form/div[2]/div[2]/div/input')
        btn_vehiculos.click()
        time.sleep(1)
        #Click en Matriculaciones/Bajas a la izquierda
        if tipo=='Bajas':
            btn_matriculaciones_bajas=driver.find_element(By.XPATH,'//*[@id="menu:listadoMenu:0:listadoSubMenu:0:j_id41"]/input')
        elif tipo=='Transferencias':
            btn_matriculaciones_bajas=driver.find_element(By.XPATH,'//*[@id="menu:listadoMenu:0:listadoSubMenu:2:j_id41"]/input')
        else:
            btn_matriculaciones_bajas=driver.find_element(By.XPATH,'//*[@id="menu:listadoMenu:0:listadoSubMenu:3:j_id41"]/input')
        btn_matriculaciones_bajas.click()
        time.sleep(1)
        #Click en informes microdatos
        btn_informes=driver.find_element(By.NAME,'accesoInformes:listadoInformesExternos:2:j_id95')
        btn_informes.click()
        time.sleep(1)

        #Recorremos el listado de años y meses que haymos introducido
        for año in años:
            for mes in meses:
                try:
                    #Elegir el año
                    seleccion_año = Select(driver.find_element(By.ID,'configuracionInfPersonalizado:filtroMesAnyo'))
                    seleccion_año.select_by_value(str(año))
                    time.sleep(1)

                    #Elegir el mes
                    seleccion_mes = Select(driver.find_element(By.ID,'configuracionInfPersonalizado:filtroMesMes'))
                    seleccion_mes.select_by_visible_text(mes)
                    time.sleep(1)

                    #Click en el botón descargar
                    btn_descargar=driver.find_element(By.NAME,'configuracionInfPersonalizado:j_id131')
                    btn_descargar.click()
                    time.sleep(5)
                    while True:
                        if os.path.isdir('C:/Users/EOFUB/Downloads/'):
                            directorio_descarga='C:/Users/EOFUB/Downloads/'
                        elif os.path.isdir('C:/Users/urkob/Downloads/'):
                            directorio_descarga='C:/Users/urkob/Downloads/'
                        listado_descargas=[archivo for archivo in os.listdir(directorio_descarga) if '.crdownload' in archivo]
                        if len(listado_descargas)==0:
                            break
                        time.sleep(10)
                except:
                    print(f'Ha habido algún problema con el archivo del año {año} y el mes {mes}')
                    pass
    except Exception as e:
        print(f'Ha habido un problema con el driver del tipo: {e}')
    finally:
        driver.close()
#Si aparece un menú sobre normativa de google que hay que aceptar, colocar esto antes de entrar a la web
# btn_aceptar=driver.find_element(By.ID,'L2AGLb')
# btn_aceptar.click()
# time.sleep(1)
