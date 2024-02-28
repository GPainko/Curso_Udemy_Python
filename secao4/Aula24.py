import os
import pathlib
import smtplib

from dotenv import load_dotenv #type:ignore
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

#caminho arquvi html
CAMINHO_HTML = pathlib.Path(__file__).parent /'Aula24.html'

#dados do rementente e destinatario
rementente = os.getenv('FROM_EMAIL','')
destinatario = rementente

#configurações smtp
smtp_server = os.getenv('SMTP_SERVER','')
smtp_port = os.getenv('SMTP_PORT','')
smtp_username = os.getenv('FROM_EMAIL','')
smtp_password = os.getenv('EMAIL_PASSWORD','')

#mensagem de texto
with open(CAMINHO_HTML,'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

#transformar nossa mensagem em MIMEMultipart
    
mime_multipart = MIMEMultipart()
mime_multipart['from']= rementente
mime_multipart['to']= destinatario
mime_multipart['subject']= 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email,'html','utf-8')
mime_multipart.attach(corpo_email)

# Envia o email
with smtplib.SMTP(smtp_server,smtp_port)as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username,smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')