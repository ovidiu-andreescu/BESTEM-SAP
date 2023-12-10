from responses import get_response

from email.message import EmailMessage
import ssl
import smtplib

def client_email(client_email, product_list):
    # nume_angajat = "John"

    sender = 'balex10ro@gmail.com'
    password = 'vwlv ldzt vsze rngg'
    receiver = client_email

    subject = 'Oferteț'
    body = get_response(product_list)

    em = EmailMessage()
    em['FROM'] = sender
    em['TO'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())
