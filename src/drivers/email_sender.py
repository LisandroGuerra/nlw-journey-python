import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

user_eth = 'xjhfdydcngj4gfuj@ethereal.email'
pass_eth = 'urG2z2RkDmfusG6vNw'
smtp_eth = {'host': 'smtp.ethereal.email', 'port': 587, 'secure': False}

def send_email(addrs_list, body):
    sender_addr = user_eth
    login = user_eth
    password = pass_eth

    msg = MIMEMultipart()
    msg['From'] = sender_addr
    msg['To'] = ', '.join(addrs_list)
    msg['Subject'] = 'Trip confirmation'

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_eth['host'], smtp_eth['port'])
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for addr in addrs_list:
        server.sendmail(sender_addr, addr, text)

    server.quit()
