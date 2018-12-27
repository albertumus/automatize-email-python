"""
El siguiente Script permite enviar correos en formato HTML desde Python y gmail de forma sencilla. Para ello hay que seguir los siguiente pasos:

* Instalar yagmail: https://yagmail.readthedocs.io/en/latest/setup.html

1. Escribir el correo de los destinatarios en "destinatarios". Separar por comas cada dirección y escribirlo entre comillas.

2. Introducir los datos del correo en cuerpo, asunto y si es necesario archivos adjuntos. Los archivos adjuntos deben de estar en la misma carpeta que el Script. 

3. Escribir el nombre de cuenta y la constraseña desde donde se va a enviar. 

4. Datos finales del correo.
"""
#Paquete de Python para la conexión con Gmail
import yagmail

### Funciones ###
def enviar_correo(destinatarios,asunto,cuerpo,archivos,copias,copias_ocultas):
    cuenta.send(
        #Destinatarios
        to=destinatarios,
        #Asunto
        subject= asunto,
        #Contenido
        contents=cuerpo, 
        #Adjuntos
        attachments=archivos,
        #Copias
        cc=copias,
        #Copias ocultas
        bcc=copias_ocultas,
    )

#################

# 1.Lista de personas que quieres que reciban el email
destinatarios = ["correodemiamigo@gmail.com","correodemiotroamigo@gmail.com"]

# 2. Datos del correo

#       Cuerpo del correo en formato HTML
cuerpo = """\
<html>
    </style>
    <body>
        <div style="text-align:center">
            <h2>Objetivos de Equipo 2</h2>
            <p><small>18 enero - 12 febrero</small></p><br>
        </div>
        <p style="font-size:16px">A continuación os adjunto un enlace a la carpeta
        donde se encuentra el documento de los objetivos del equipo
        para este Sprint</p>
        <ul>
            <li><p>Enlace:</p><a href="google.com">Google.com</a></li>
            <li><p>Fecha Reunión: 8 de enero, 9:00</p></li>
        </ul>
    </body>
</html>"""

#       Asunto
asunto = "Correo de Prueba"

#       Nombre del archivo con formato que se va a adjuntar
archivos = ["emails-python.py"]

#       Copias
copias = []

#       Copias Ocultas
copias_ocultas = []


# 3.Introducir datos de la cuenta de Gmail
cuenta = yagmail.SMTP("micorreo@gmail.com", 'micontraseña')

# 4. El correo se envia
try:
    enviar_correo(destinatarios,asunto,cuerpo,archivos,copias,copias_ocultas)
    print("Su correo se ha enviado correctamente")
except:
    print("Algo ha ido mal y su correo no se ha podido enviar")
