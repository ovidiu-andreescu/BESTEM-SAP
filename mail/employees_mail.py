from email.message import EmailMessage
import ssl
import smtplib
import random


nume_angajat = "John"
item = "ProdusX"
nr = 5
nume_departament = "Resurse Umane"

mesaje = [
    f"""

    

Subiect: URGENT: Comandă Necesară - {nr} de {item}


Situația noastră de stoc pentru {item} necesită o acțiune imediată. Vă rugăm să plasați o comandă pentru {nr} de {item} în cel mai scurt timp posibil pentru a ne asigura că avem suficiente în stoc.

Cu apreciere,
Departamentul de Resurse Umane""",



f"""
Subiect: URGENT: Comandă Necesară pentru {item}
Este necesar să plasați o comandă pentru {nr} de {item}. Ne puteți contacta pentru orice asistență suplimentară.

Cu recunoștință,
Departamentul de Resurse Umane""",


f"""
Subiect: Atenție: Cerere Crescută pentru {item} - Acțiune Urgentă Necesară


Am observat o creștere semnificativă a cererii pentru {item}, și este crucial să acționăm acum. Vă rugăm să plasați o comandă pentru {nr} de {item} pentru a ne asigura că putem satisface cererea.

Cu apreciere,
Departamentul de Resurse Umane""",
    f"""Subiect: Acțiune Urgentă Necesară: Stoc {item} pe Punctul de Expirare
,

Vă informăm că stocul nostru de {item} este pe punctul de a se epuiza. Pentru a evita situații de stoc insuficient, vă rugăm să plasați o comandă pentru {nr} de {item} cât mai curând posibil.

Cu apreciere,
Departamentul de Resurse Umane""",

    f"""Subiect: URGENT: Acțiune Necesară - Plasare Comandă {item}


Situația stocului de {item} necesită atenție imediată. Vă rugăm să plasați o comandă pentru {nr} de unități.

Cu recunoștință,
Departamentul de Resurse Umane"""
]


def employee_email(email, product_name, amount):
    sender='balex10ro@gmail.com'
    password='vwlv ldzt vsze rngg'
    receiver='zeeztwzeeztw@gmail.com'

    subject='Instrucțiune'

    i = random.randint(0, 4)
    body=mesaje[i]

    em=EmailMessage()
    em['FROM']=sender
    em['TO']=receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender,receiver,em.as_string())
