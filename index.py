#import libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from setup import email_to ,email_from, smtp_server \
    ,smtp_port , password, subject, message
from colorama import Fore
from sendbyattachment.Functions import TextSeparator , PrintError , PrintSuccessText , ExitProgram




def send_email():

    #make a MIME object to define parts of the  Email
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    # Attach the body of the message
    msg.attach(MIMEText(message,"plain"))

    #define the file to attach
    filename = "report.txt"

    #Open the file in python as a binary
    attachment = open(filename, "rb") # r for read and b for binary



    #Encode as base 64
    try:
        attachment_package = MIMEBase("application", "octet-stream")
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header("Content-Disposition", "attachment; filename= " + filename)
        msg.attach(attachment_package)
    except Exception as e:
        PrintError(e)
        PrintError("Error: Could not Encode Email")
        TextSeparator()
        ExitProgram()

    #Cast as string
    text = msg.as_string()

    #Connect with the server
    try:
        PrintSuccessText("Connecting to server. . .")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, password)
        PrintSuccessText("Succesfully connected to server☻")
        TextSeparator()
    except Exception as e:
        PrintError(e)
        PrintError("Error: Could not send Email")
        TextSeparator()
        ExitProgram()


    #send Email to Email_to as
    try:
        print(f"{Fore.MAGENTA}Sending email to: {Fore.GREEN} {email_to} . . . {Fore.RESET}")
        TIE_server.sendmail(email_from, email_to, text)
        print(f"{Fore.MAGENTA}Email sent to: {Fore.GREEN} {email_to} {Fore.RESET}")
        PrintSuccessText("Successfully sending Email")
        TextSeparator()
    except Exception as e:
        PrintError(e)
        PrintError("Error: Could not send Email")
        TextSeparator()
        ExitProgram()

    #quit server
    TIE_server.quit()




#start  project
if __name__ == '__main__':
    send_email()














