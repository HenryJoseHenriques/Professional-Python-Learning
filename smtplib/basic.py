import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Cria a mensagem de email como MIMEMultipart para conter corpo e anexos
msg = MIMEMultipart()
msg['Subject'] = 'Você recebeu um arquivo?'
msg['From'] = 'henryjose@edu.univali.br'
msg['To'] = 'henryjose.321@gmail.com'

# Corpo do email (texto simples)
body = 'Aqui está o arquivo anexado.'
msg.attach(MIMEText(body, 'plain'))

# Anexa o arquivo
filename = 'dataset.csv'  # O nome do arquivo que você quer anexar
filepath = 'dataset.csv'  # O caminho do arquivo

# Abre o arquivo no modo binário
with open(filepath, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())  # Lê o conteúdo do arquivo

# Codifica o arquivo em base64 para enviá-lo por email
encoders.encode_base64(part)

# Adiciona o cabeçalho Content-Disposition para que o email saiba que é um anexo
part.add_header(
    'Content-Disposition',
    f'attachment; filename={filename}',  # Nome que aparecerá no anexo
)

# Anexa a parte do arquivo à mensagem
msg.attach(part)

# Envia o email usando smtplib
with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
    server.starttls()  # Inicia a conexão TLS
    server.login('#########', '########')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
