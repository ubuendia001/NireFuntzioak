import win32com.client
import smtplib
from email.message import EmailMessage

def enviar_email_gmail(email_destino,asunto,cuerpo,adjuntos=None):
    """
    Esta función envía un e-mail a través de GMAIL.
    Importaciones necesarias:
        -import smtplib
        -from email.message import EmailMessage
    Parámetros:
        -email_destino(string): Dirección a la que queremos enviar el email.
        -asunto(string): Asunto que queremos indicar en el mail.
        -cuerpo(string): Texto con el mensaje que queremos enviar
        -adjuntos(lista): Listado de archivos con dirección completa y extensión. Por defecto si adjunto.
    Ejemplo:
        email_destino='urkobuendia@hotmail.com'
        asunto='Este es el asunto'![](../ELECTRICIDAD/SPOTS/Precios SPOT europeos.png)
        cuerpo='Este es el cuerpo'
        adjuntos=['C:/Users/urkob/OneDrive - Ente Vasco de la Energia/ELECTRICIDAD/SPOTS/Precios SPOT europeos.png']

        enviar_email_gmail(email_destino=email_destino,asunto=asunto,cuerpo=cuerpo,adjuntos=adjuntos)
    """
    parar=False
    if os.path.isfile('C:/Users/urkob/OneDrive - Ente Vasco de la Energia/NIRE FUNTZIOAK/pasahitzak.txt'):
        archivo_contraseña='C:/Users/urkob/OneDrive - Ente Vasco de la Energia/NIRE FUNTZIOAK/pasahitzak.txt'
    elif os.path.isfile('C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/NIRE FUNTZIOAK/pasahitzak.txt'):
        archivo_contraseña='C:/Users/EOFUB/OneDrive - Ente Vasco de la Energia/NIRE FUNTZIOAK/pasahitzak.txt'
    else:
        print('Ez dago pasahitza duen txt dokumentua')
    with open(archivo_contraseña,mode='r') as archivo:
        pasahitza=archivo.readline()
    msg=EmailMessage()
    msg['Subject']=asunto
    msg['From']='urkobuendia@gmail.com'
    msg['To']=email_destino
    msg.set_content(cuerpo)

    if adjuntos!=None:
        for adjunto in adjuntos:
            try:
                with open(adjunto,'rb') as f:
                    file_data=f.read()
                    file_name=f.name
                msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
            except:
                print('Ha habido algún problema con los adjuntos')
                parar=True
    if parar==False:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
            s.login(user='urkobuendia@gmail.com',password=pasahitza)
            s.send_message(msg)

def enviar_email_outlook(emailDestino, emailAsunto, emailCuerpo,cuerpoEnHtml=False,tablas=None,firma=None,indicesTablas=True, emailEmisor=None, adjuntos=None, conCopia=None):
    """
    Esta función envía un e-mail a través de OUTLOOK.
    Si el cuerpo del email está en HTML, que incluya también la firma.
    Importaciones necesarias:
        -import win32com.client
    Parámetros:
        -emailDestino(string): Dirección a la que queremos enviar el email.
        -emailAsunto(string): Asunto que queremos indicar en el mail.
        -emailCuerpo(string): Texto con el mensaje que queremos enviar
        -cuerpoEnHtml(bool): Si el texto metido en emailCuerpo está en formato HTML o no. Por defecto no (False)
        -tablas(dict): Diccionario con el título de la tabla y la tabla pandas
        -firma(string): string con la dirección completa donde se encuentra la imagen con la firma
        -indicesTablas(bool): Es para indicar si queremos que añada la columna index de la tabla en el mail. Por defecto lo incluye (True)
        -emailEmisor(string): Dirección de la que queremos enviar el email cuando hay varios correos disponibles. Por defecto se envía desde el principal.
        -adjuntos(lista): Listado de archivos con dirección completa y extensión. Por defecto sin adjunto.
        -conCopia(lista): Listado de emails al que se les quiere poner en copia.

    Ejemplo:
        enviar_email_outlook(emailDestino='urkobuendia@hotmail.com',
                             emailAsunto='Asunto prueba',
                             emailCuerpo='Cuerpo prueba',
                             cuerpoEnHtml=False
                             tablas=None,
                             firma='C:/Users/urkob/Desktop/borrar/Consumos eléctricos.png',
                             indicesTablas=True,
                             emailEmisor=None,
                             adjuntos=['C:/Users/urkob/OneDrive - Ente Vasco de la Energia/ELECTRICIDAD/SPOTS/Precios SPOT europeos.png'],
                             conCopia=['urkobuendia@gmail.com'])
    """

    noEnviar=False #Si hay algún error, esto cambiará a True y no se enviará el mail

    try:
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        #mail.SendUsingAccount = emailEmisor #Antes utilizabamos esto pero dejó de funcionar
        if emailEmisor!=None:
            mail.SentOnBehalfOfName = emailEmisor
        mail.To = emailDestino
        mail.Subject = emailAsunto

        if cuerpoEnHtml==True:
            emailCuerpoHTML=emailCuerpo
        else:
            emailCuerpoHTML='<p>' + emailCuerpo + '<br><br> </p>'

        if tablas!=None:
            for titulo,tabla in tablas.items():
                emailCuerpoHTML += '<p>' + titulo + '</p>'
                if indicesTablas==True:
                    emailCuerpoHTML+=tabla.to_html()
                else:
                    emailCuerpoHTML+=tabla.to_html(index=False)
                emailCuerpoHTML+= '<br><br><br>'

        if firma!=None:
            #Para meter la firma en el cuerpo del mail, primero hay que adjuntarlo y luego cambiar sus propiedades.
            attachment = mail.Attachments.Add(firma)
            attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId1")
            img_tag = "<p> <img src=""cid:MyId1""></p>"
            emailCuerpoHTML += img_tag
            emailCuerpoHTML+= '<br><br><br>'


        mail.HTMLBody=emailCuerpoHTML

        if adjuntos != None:
            for adjunto in adjuntos:
                mail.Attachments.Add(adjunto)

        if conCopia != None:
            mail.CC = ';'.join(conCopia)

    except:
       noEnviar=True
       print('El email no ha sido enviado')

    if noEnviar==False:
        mail.Send()
        print('Email enviado')
