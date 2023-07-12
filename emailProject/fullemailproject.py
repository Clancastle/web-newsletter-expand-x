"""this is just the script to send the email. i can host it to the
cloud and have it run every 5 days/bi-weekly. put email in input, sends auto, if no input
no send.
"""

#open file of emails, do the dodo
import smtplib

user = 'dennjsu.business@gmail.com'
password = 'qczqtuyctdckbakb'
emails = ["dennisungureanu0@gmail.com", user, 'Sc842506@gmail.com', 'lbnqvgmhnqvfbe@protonmail.com',
          'andrewli3645@gmail.com']
emails = [user, "apple@gmail.com", 'apple1@gmail.com']
# email = [email for email in emails] #can place list as a (to send) and it will work

msg = """msg
"""

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # identifies with mail server
    smtp.starttls()  # encrypts traffic (email)
    smtp.ehlo()  # re-identifies with mail server

    smtp.login(user, password)

    smtp.sendmail(user, emails, None)

"""Plan:
make a decent webpage w js and html, css, and connect to my backend, 
here, which should make 'emails' a list, open in a document, (learn to save the data)
then i send the emails signing up (before w rgex) here to emails. """


"""To integrate this script with a web page, you can follow these steps:

Create a web page using HTML, CSS, and JavaScript to collect user input, including the email address. (✔︎)
-> better to do this client side, since you dont want to throw away the data once its submitted. 
'defer src=""' makes sure the DOM is ready when the page runs
(later) Use AJAX requests to submit the form without refreshing the entire page. This prevents users from losing
their progress on the current task when they accidentally hit reload before submitting their information. ()

Validate the email address using JavaScript to ensure it matches the desired pattern. (✔︎)
Once the form is submitted, send an HTTP request to your backend server, passing the email address as data.
In your backend server, receive the HTTP request and extract the email address.
Append the email address to the emails list in your Python script.
Save the updated emails list to a file or database to persist the data for future use.
Use a scheduling mechanism (e.g., cron job, task scheduler) to run the Python script periodically, sending emails to the email addresses in the emails list."""