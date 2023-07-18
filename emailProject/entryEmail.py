import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dennis = 'dennisungureanu0@gmail.com'


#open html and send the email as html?
def send(fname, email):

    user = 'dennjsu.business@gmail.com'
    password = 'qczqtuyctdckbakb'

    message = MIMEMultipart('alternative')
    message['Subject'] = 'Welcome to our Newsletter'
    message['From'] = 'Kaizen <dennjsu.business@gmail.com>'
    message['To'] = email
    text = ''

    welcome_message = f"""
    <html lang="en">
    <body>
        <h1>Welcome to our Newsletter {fname}!</h1>
        <p>This newsletter is all about self-improvement, personal growth, and motivation. We provide valuable insights, tips, and resources to help you enhance various aspects of your life and achieve your goals.</p>
        <p>Stay tuned for inspiring articles, thought-provoking quotes, recommended books and podcasts, and much more!</p>
        <p>If you ever wish to unsubscribe from our newsletter, you can do so by clicking the following link: <a href="http://127.0.0.1:5000/k-signup">Unsubscribe</a>.</p>
        <p>Thank you for joining us on this journey of self-improvement!</p>
        <p>Best regards,<br>Your Newsletter Team</p>
    </body>
    <!-- <footer><a href="http://127.0.0.1:5000/unsubscribe">Unsubscribe</a>From our newsletter</footer> -->

    </html>
    """
    # <br> <br>
    # <footer> ™ BY DJUngureanu</footer

    # text_part = MIMEText(text, 'plain')
    html_part = MIMEText(welcome_message, 'html')

    # message.attach(text_part)
    message.attach(html_part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:


        smtp.login(user, password)
        smtp.sendmail(user, email, message.as_string())

send('User', dennis)



