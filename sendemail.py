import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Olawale Ibrahim'
email['to'] = 'ibrahim.olawale13@gmail.com'
email['subject'] = 'Congratulations on your new job!!!'

email.set_content(html.substitute({'name': 'Rexha'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ibrahimagp1hf0@futa.edu.ng', '*****************.')
    smtp.send_message(email)
    print('All Good.')
