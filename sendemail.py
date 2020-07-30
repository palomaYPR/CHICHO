import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
# Migrar libreria email
import ssl

#Cargar variable entrada/salida y reemplzar (STR)
def sendemail(a, b):
    msg = EmailMessage()
    if b == 1:
        # Verificación de registro
        msg.set_content('Hello\n\nFaceCamIIEG has recoginized ' + str(a) + ' with a confidence of ' + str(
            b) + '%' ' \n\nPlease verify the updated database.\n\nPlease do not reply this email as it is automated')
    else:
        # Verificación de salida
        msg.set_content('Hello\n\nFaceCamIIEG has recoginized ' + str(a) + ' with a confidence of ' + str(
            b) + '%' ' \n\nPlease verify the updated database.\n\nPlease do not reply this email as it is automated')

    msg['Subject'] = 'Missing person report by FaceCamIIEG'
    msg['From'] = "pdprodelfin@gmail.com"
    msg['To'] = "yppr09@gmail.com"
    #msg['To'] = "kofrran@gmail.com"


    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("pdprodelfin@gmail.com", "facereconiieg.")
    server.send_message(msg)
    server.quit()

    print('Email sent!')

sendemail(1,1)


