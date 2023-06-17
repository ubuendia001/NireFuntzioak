import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def distribucion(datos,titulo='Distribución de los datos'):
    """
    Esta función muestra el histograma y el boxplot de una serie de datos. En ambos gráficos se muestran datos estadísticos de la serie
    Importaciones necesarias:
        -import numpy as np
        -import matplotlib.pyplot as plt
        -import math.
    Parametros:
        -datos(serie):serie de datos que se quiere analizar.
    """
    datos=datos.values
    media=round(np.mean(datos),1)
    mediana=round(np.median(datos),1)
    desviacionEstandar=round(np.std(datos),3)
    desviacionEstandarCalculado=round(math.sqrt(np.sum(np.square(datos-media))/len(datos)),3)
    valor_max=round(np.max(datos),1)
    valor_min=round(np.min(datos),1)
    perc25,perc50,perc75=np.round(np.percentile(datos,[25,50,75]),1)
    iqr=perc75-perc25
    whisker_limite_superior=round(perc75+1.5*iqr,1)
    whisker_limite_inferior=round(perc25-1.5*iqr,1)
    if valor_max>whisker_limite_superior:
        whisker_superior=round(datos[np.ndarray.argmin(np.abs(datos-whisker_limite_superior))],1)
        outlier_superior=valor_max
    else:
        whisker_superior=valor_max
        outlier_superior=None

    if valor_min<whisker_limite_inferior:
        whisker_inferior=round(datos[np.ndarray.argmin(np.abs(datos-whisker_limite_inferior))],1)
        outlier_inferior=valor_min
    else:
        whisker_inferior=valor_min
        outlier_inferior=None

    fig,[izq,drch]=plt.subplots(nrows=1,ncols=2,figsize=(18,8))
    plt.suptitle(titulo)
    # izq.hist(datos,bins=int(round(valor_max,0)))
    izq.hist(datos,bins=10)
    izq.axvline(x=media,color='green',linestyle='--')
    izq.set_title('Histograma')
    drch.boxplot(datos,whis=1.5)
    drch.axhline(y=media,color='green',linestyle='--')
    drch.text(0.7,media,'Media: '+str(media),color='green',verticalalignment ='bottom')
    drch.text(1.1,perc50,'Perc50 o Mediana: '+str(perc50),verticalalignment ='center')
    drch.text(1.1,perc25,'Perc25: '+str(perc25),verticalalignment ='center')
    drch.text(1.1,perc75,'Perc75: '+str(perc75),verticalalignment ='center')
    drch.text(1.1,whisker_superior,'Whisker superior: '+str(whisker_superior),verticalalignment ='center')
    drch.text(1.1,whisker_inferior,'Whisker inferior: '+str(whisker_inferior),verticalalignment ='center')
    if outlier_superior:
        drch.text(1.1,outlier_superior,'Outlier: '+str(outlier_superior),verticalalignment ='center')
    if outlier_inferior:
        drch.text(1.1,outlier_inferior,'Outlier: '+str(outlier_inferior),verticalalignment ='center')
    drch.get_xaxis().set_visible(False)
    drch.set_title('Box plot')


def regresión_lineal(datos, columnaX, columnaY):
    """
    Esta función hace una regresión lineal entre la columnaY y la columnaX de la tabla datos.
    Al dataFrame introducido se le añade una columna 'Y_regresión_lineal' con los datos resultado de aplicar el modelo.
    La función devuelve los valores de la fórmula y=x0.x+coeficiente
    Importaciones necesarias:
        -import matplotlib.pyplot as plt
        -import numpy as np
        -from sklearn.linear_model import LinearRegression
        -from sklearn.metrics import mean_squared_error, r2_score
        -import pandas as pd.
    Parametros:
        -datos(pandas.DataFrame): tabla del tipo DataFrame que se quiere pegar en el word
        -columnaX(string): Nombre de la columna que se quiere utilizar como eje X.
        -columnaY(string): Nombre de la columna que se quiere utilizar como eje Y.
    Esta función devuelve los valores de la fórmula y=x0.x+coeficiente:
        -datos: datos con la columna 'Y_regresión_lineal' resultado de aplicar el modelo
        -valor_x0: valor base de la fórmula de la regresión lineal
        -coeficiente: valor de coeficiente de la fórmula de la regresión lineal
        -r2valor: Valor de r^2 que indica cuán buena es la regresión
    Para hacer el gráfico:
        plt.figure(figsize=(8,6))
        plt.scatter(columnaX,columnaY,data=datos,c='skyblue')
        plt.plot(datos[columnaX],datos['Y_regresión_lineal'],c='salmon')
        plt.ylabel(columnaY)
        plt.xlabel(columnaX)
        plt.text(5,100,'y='+str(round(coeficiente[0],1))+'x'+'+'+str(round(valor_x0,1))+'\n'+ 'r2='+str(round(r2valor,2)))
        plt.tight_layout()
        plt.show()

    """
    X=datos.loc[:,columnaX].values
    Y_original=datos.loc[:,columnaY].values
    X=X[:,np.newaxis]
    regr = LinearRegression()
    regr.fit(X, Y_original)
    Y_predic = regr.predict(X)
    datos['Y_regresión_lineal']=Y_predic
    coeficiente=regr.coef_
    r2valor=r2_score(Y_original,Y_predic)
    valor_x0=regr.intercept_
    # valor_x0=np.array([0,1,2]) Otro método de conseguir el x0
    # valor_x0=regr.predict(valor_x0[:,np.newaxis])[0] Otro método de conseguir el x0
    return datos,valor_x0,coeficiente,r2valor

    # ---------------------------------------- Ejemplo----------------------------------------
    # df=pd.read_excel('Ejemplo.xlsx')
    # df,x0valor,coeficiente,r2=regresión_lineal(df,'Grados dia','Consumo GN')
    # df.sort_values('Grados dia',inplace=True)
    # plt.scatter(df['Grados dia'],df['Consumo GN'],color='skyblue')
    # plt.plot(df['Grados dia'],df['Y_regresión_lineal'],color='salmon')
    # plt.legend([f'y={round(float(x0valor),2)}+{round(float(coeficiente),2)}x\nR cuadrado: {round(float(r2),2)}'],
    #             loc='upper left')
    # plt.show()

def regresión_polinomial(datos,columnaX,columnaY):
    """FALTA ANALIZAR BIEN LO QUE DEVULEVE LA FUNCIÓN"""

    """
    Esta función hace una regresión lineal entre la columnaY y la columnaX de la tabla datos.
    Al dataFrame introducido se le añade una columna 'Y_regresión_lineal' con los datos resultado de aplicar el modelo.
    La función devuelve los valores de la fórmula y=x0.x+coeficiente
    Importaciones necesarias:
        -import matplotlib.pyplot as plt
        -import numpy as np
        -from sklearn.linear_model import LinearRegression
        -from sklearn.preprocessing import PolynomialFeatures
        -from sklearn.metrics import mean_squared_error, r2_score
        -import pandas as pd.
    Parametros:
        -datos(pandas.DataFrame): tabla del tipo DataFrame que se quiere pegar en el word
        -columnaX(string): Nombre de la columna que se quiere utilizar como eje X.
        -columnaY(string): Nombre de la columna que se quiere utilizar como eje Y.
    Esta función devuelve los valores de la fórmula y=x0.x+coeficiente:
        -datos: datos con la columna 'Y_regresión_lineal' resultado de aplicar el modelo
        -valor_x0: valor base de la fórmula de la regresión lineal
        -coeficiente: valor de coeficiente de la fórmula de la regresión lineal
        -r2valor: Valor de r^2 que indica cuán buena es la regresión
    """
    X=datos.loc[:,columnaX].values
    Y_original=datos.loc[:,columnaY].values
    X=X[:,np.newaxis]
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, Y_original)
    Y_predic=pol_reg.predict(poly_reg.fit_transform(X))
    datos['Y_regresión_polinomial']=Y_predic
    coeficientes=pol_reg.coef_
    r2valor=r2_score(Y_original,Y_predic)
    valor_x0=np.array([0,1,2])
    valor_x0=valor_x0[:,np.newaxis]
    valor_x0=pol_reg.predict(poly_reg.fit_transform(valor_x0))[0]
    return datos,valor_x0,coeficientes,r2valor

    # ---------------------------------------- Ejemplo----------------------------------------
    # df=pd.read_excel('Ejemplo.xlsx')
    # df,x0valor,coeficientes,r2=regresión_polinomial(df,'Grados dia','Consumo GN')
    # df.sort_values('Grados dia',inplace=True)
    # plt.scatter(df['Grados dia'],df['Consumo GN'],color='skyblue')
    # plt.plot(df['Grados dia'],df['Y_regresión_polinomial'],color='salmon')
    # plt.legend([f'y={round(float(coeficientes[2]),4)}x^2+{round(float(coeficientes[1]),2)}x+{round(float(x0valor),2)}\nR cuadrado: {round(float(r2),2)}'],
    #             loc='upper left')
    # plt.show()
