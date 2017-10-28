import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def _send_email(email, name, description,
                             endDate, amount, confirmation):
    # me == my email address
    # you == recipient's email address
    me = "jose.evanan@gmail.com"
    you = email
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "PagaPe"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
    <head></head>
    <body>
        <img src="https://scontent.faqp1-1.fna.fbcdn.net/v/t34.0-12/22901695_1930361390547116_415760123_n.png?oh=3bd1675bc7bb567e84baaad992e2e49b&oe=59F5D614" >
        <p>Hola! {}<br>
        {}<br>
        Tienes una deuda de {}, tienes para cancelar hasta {} <a href="http://pagape.com/confirmar/{}">link</a>.
        </p>
    </body>
    </html>
    """.format( name, description,amount, endDate, confirmation)
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('pagainfope@gmail.com', 'pagainfo2017')
    try:
        mail.sendmail(me, you, msg.as_string())
        mail.quit()
        return True
    except Exception as e:
        print(e)
        return False
