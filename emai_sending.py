import os
import sys
import smtplib
import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def process_excel(file_path,sendermail,senderMailPassword,messageToSend):
    try:
        df = pd.read_excel(file_path)
        emails = df['Email'].tolist()  
        sender=smtplib.SMTP("smtp.gmail.com",587)
        sender.starttls()
        pwd = senderMailPassword.replace("\xa0", " ")
        sender.login(sendermail,pwd)
        message = MIMEMultipart("alternative")
        sendmessage=MIMEText(messageToSend, "plain")
        message.attach(sendmessage)
        for receiver_email in emails:
            sender.sendmail(sendermail,receiver_email,message.as_string())
        print("sucessfully done!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        print("done!")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py excel_file sender_email sender_password message_to_send")
        sys.exit(1)
    excel_file = sys.argv[1]
    sendermail= sys.argv[2]
    senderMailPassword= sys.argv[3]
    messageToSend=sys.argv[4]
    process_excel(excel_file,sendermail,senderMailPassword,messageToSend)










