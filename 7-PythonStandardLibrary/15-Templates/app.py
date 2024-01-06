from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template

# mime is multipurpose internet mail extensions


template = Template(Path("template.html").read_text())

# we can pass dics or arguments (name= "jhon")
body = template.substitute({"name": "jhon"})

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"
# if html is not sent then it is plain text
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("mosh.png").read_bytes()))  # To send a image


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.helo()  # to start the communication
    smtp.starttls()  # to enable tls: encryption
    # login to sender account
    smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
    smtp.send_message(message)  # send the message
    print("sent.")