import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter.filedialog import askopenfilename


port = 465  # For SSL

subject = "CERTIFICATE WITH BLESSINGS - VANDE RAGHAVAM VIBHUM"
body = """Dear participant,Blessings from Srirangam Srimath Andavan Ashramam!

We thank you for your participation in Vande Raghavam Vibhum ! Your efforts are highly appreciated and noted.
Please find the attached e-certificate along with the detailed report on the Competitions.

In case you have any doubt regarding the certificate, kindly email to
vanderaghavamvibhumssaa@gmail.com, with the details of competition participated along with name and age of the participant.

Regards
Team Vande Raghavam Vibhum
"""
sender_email = "shashankp96@gmail.com"
receiver_email = "h20191030599@hyderabad.bits-pilani.ac.in"
password = input("Type your password and press enter:")

message = MIMEMultipart()
message["Subject"] = "CERTIFICATE WITH BLESSINGS - VANDE RAGHAVAM VIBHUM"
message["From"] = "shashankp96@gmail.com"
message["To"] = "h20191030599@hyderabad.bits-pilani.ac.in"

message.attach(MIMEText(body, "plain"))

filename = "./ACHINTYA RAMESH1.JPG"
# filename = askopenfilename()
# Create a secure SSL context

#open the attachment in binary mode
with open(filename,"rb") as attachment:
    part = MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename = {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
text = message.as_string()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("shashankp96@gmail.com", password)
    server.sendmail(sender_email, receiver_email, text)
