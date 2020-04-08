from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re
import time

#Server and port for SMTP connection
SMTP_SERVER = ""
#port number type: int
SMTP_PORT =

# Email address to send
SMTP_USER = ""
#Password of email address to send
SMTP_PASSWORD = ""

# Email address to receive
addr=""


# Function to check if email is valid
def is_valid(addr):

    if re.match('(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        return True
    else:
        return False


# function to send email
def send_mail(addr, subj_layout, cont_layout, attachment=None):
    if not is_valid(addr):
        print("Wrong receive email: " + addr)
        return
    if not is_valid(SMTP_USER):
        print("Wrong send mail: "+SMTP_USER)
        return

    # text file
    msg = MIMEMultipart("alternative")

    msg["From"] = SMTP_USER
    msg["To"] = addr
    msg["Subject"] = subj_layout
    contents = cont_layout
    text = MIMEText(_text=contents, _charset="utf-8")
    msg.attach(text)
    # print(msg.as_string())

    # Create class variable with server information to connect smtp
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    # login to server
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    # send mail
    smtp.sendmail(SMTP_USER, addr, msg.as_string())

    # exit
    smtp.close()
def time_set(timeFrequency,currentTime):
    if now.tm_min%timeFrequency==0:
        cont_layout = currentTime
        send_mail(addr, subj_layout, cont_layout, attachment=None)
        print("Mail send complete")




if __name__=="__main__":
    timeFrequency = int(input("Enter the minutes to send mail: "))
    subj_layout = input("Enter the subject of mail: ")
    while(1):
        t = time.time()
        now = time.gmtime(t)
        #The time is set to utc, so you need to set it back to the time appropriate for your area.
        hour = now.tm_hour
        hour %= 24
        if hour >= 12:
            check = "PM"
            hour -= 12
        else:
            check = "AM"
        nowTime = str(now.tm_year) + '-' + str(now.tm_mon) + '-' + str(now.tm_mday) + ' ' + check + ' ' + str(hour) + 'Hour' + str(
            now.tm_min) + 'Min' + str(now.tm_sec) + 'Secs'

        time_set(timeFrequency,nowTime);
        time.sleep(60)

