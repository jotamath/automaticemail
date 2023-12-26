import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

#dados do email
password = open("senha", "r").read()
from_email="meuemail@gmail.com"
to_email="emaildapessoa@gmail.com"
subject="Automação Planilha"
body="""
Olá, segue em anexo a automação da planilha
para a empresa XYZ Automação.

Qualquer dúvida, estamos à disposição.
"""

#montando a estrutura do email
message= EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

#adicionar o anexo
anexo = "test.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

#enviando o email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email,password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
