def mes_nombre(numero, idioma='Castellano'):
    """
    Esta función devuelve un string con el nombre del mes introduciendo el número de mes. Pudiendo elegir entre los nombres en castellano y en euskera.

    Parametros:
        -numero(integer):número del mes que se quiere convertir a texto.
        -idioma(string, 'Euskera' o 'Castellano'): Idioma en el que se quiere devolver los nombres de los meses. Por defecto en castellano.

    """
    if (idioma != 'Castellano') and (idioma != 'Euskera'):
        print('Elige bien el idioma, Castellano o Euskera')
    else:
        if idioma == 'Castellano':
            meses_dict = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
                          10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
        else:
            meses_dict = {1: 'Urtarrila', 2: 'Otsaila', 3: 'Martxoa', 4: 'Apirila', 5: 'Maiatza',
                            6: 'Ekaina', 7: 'Uztaila', 8: 'Abuztua', 9: 'Iraila', 10: 'Urria', 11: 'Azaroa', 12: 'Abendua'}
        return meses_dict[numero]

#/////////////////////////////////////////////////////////////////////////////////////////////////

def mes_numero(nombre):
    """
    Esta función devuelve un integer con el número del mes introduciendo el nombre del mes.
    Da igual que esté en mayúsculas, minúsculas, euskera o castellano porque lo transformamos a minúsculas todo.

    Parametros:
        -nombre(string): Nombre del mes que se quiere transformar a número.

    """
    nomb = nombre.lower()
    meses_dict = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8, 'septiembre': 9,
                  'octubre': 10, 'noviembre': 11, 'diciembre': 12, 'urtarrila': 1, 'otsaila': 2, 'martxoa': 3, 'apirila': 4,
                  'maiatza': 5, 'ekaina': 6, 'uztaila': 7, 'abuztua': 8, 'iraila': 9, 'urria': 10, 'azaroa': 11, 'abendua': 12,}
    return meses_dict[nomb]
