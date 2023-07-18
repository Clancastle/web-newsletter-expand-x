import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dennis = 'dennisungureanu0@gmail.com'

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
        <!-- <img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.topgear.com%2Fsites%2Fdefault%2Ffiles%2F2022%2F03%2FTopGear%2520-%2520Tesla%2520Model%2520Y%2520-%2520003.jpg&tbnid=ZN8N_svReknZuM&vet=12ahUKEwjIpL6R4ZiAAxUYHN4AHZiZD6cQMygCegUIARD5AQ..i&imgrefurl=https%3A%2F%2Fwww.topgear.com%2Fcar-reviews%2Ftesla%2Fmodel-y&docid=9RrU3geMXTh6cM&w=4926&h=2771&q=testla&client=safari&ved=2ahUKEwjIpL6R4ZiAAxUYHN4AHZiZD6cQMygCegUIARD5AQ" height="1" width="1" > --> <!-- For tracking pixel, listen to GET req once website is on -->
        
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



