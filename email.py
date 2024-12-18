import smtplib
import ssl
from email.mime import image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.utils import make_msgid
import mimetypes
import os
from dotenv import load_dotenv


load_dotenv()

def send_email(path_to_resume:str, path_to_cv:str = None,  to:str, subject:str):
    sender_address = os.get('ekompract@gmail.com')
    password = os.get('EMAIL_PASSWORD')
    
    
    image_cid = make_msgid()
    message = MIMEMultipart('alternative')
    message['From'] = sender_address
    message['To'] = to
    message['Subject'] = Header(subject, 'utf-8')
    context = ssl.create_default_context()
    
    text = MIMEText(resume_email.format(),"html", "uft8")
    message.attach(text)
    company_logo = MIMEImage(open("Image/aivan.png","rb").read())
    
    company_logo.add_header('Content-ID','')
    if path_to_cv != None:
        with open(path_to_cv) as cv_pdf:
            cv = MIMEApplication(cv_pdf.read(), _subtype="pdf")
            
        message.add_header('Content-Disposition', 'attachment', filename=str(path_to_cv))
        message.attach(cv)
        
        
    with open(path_to_resume, "rb") as resume_file:
        resume = MIMEApplication(resume_file.read(), _subtype="pdf")
        
    resume.add_header('Content-Disposition', 'attachment', filename=str(path_to_resume))
    
    message.attach(resume )
         
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465 ,context=context) as email:
            email.login(user=sender_address, password=password)
            email.sendmail(sender_address, to, message.as_string())
            print('email sent successfully')
            email.close()
    except Exception as e:
        print(f"failed to send email due to {e}")   