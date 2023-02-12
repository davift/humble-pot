#!/usr/bin/python3
import time
import datetime
import smtplib
from email.mime.text import MIMEText
import os

def send_report(report):
    HOST = os.environ.get('SMTP_HOST')
    USER = os.environ.get('SMTP_USER')
    PASS = os.environ.get('SMTP_PASS')
    FROM = os.environ.get('SMTP_FROM')
    TO = os.environ.get('SMTP_TO')

    BODY = MIMEText(report, "html")
    BODY["Subject"] = 'Intrusion Alert (' + os.uname()[1] + ')'
    BODY["From"] = FROM
    BODY["To"] = TO

    send = smtplib.SMTP(HOST, 587)
    send.ehlo
    send.starttls()
    send.ehlo
    send.login(USER, PASS)
    send.sendmail(FROM, TO, BODY.as_string())
    send.quit()

while True:
    # Reading log file.
    with open("humblepot.log", "r") as file:
        lines = file.readlines()

    # Wiping out the file for the next cycle.
    with open("humblepot.log", "w") as file:
        file.write("")

    sources = {}
    ports = {}
    users_passwords = {}
    domains = {}
    restarts = 0
    
    for line in lines:
        if "from:" in line:
            source = line.strip().split(" ")[1]
            if source in sources:
                sources[source] += 1
            else:
                sources[source] = 1
                
            port = line.strip().split(" ")[4]
            if port in ports:
                ports[port] += 1
            else:
                ports[port] = 1
                
            if "username" in line:
                user_password = line.strip().split(" ")[6] + ":" + line.strip().split(" ")[8]
                if user_password in users_passwords:
                    users_passwords[user_password] += 1
                else:
                    users_passwords[user_password] = 1
                    
            if "domain" in line:
                domain = line.strip().split(" ")[8].strip()
                if domain in domains:
                    domains[domain] += 1
                else:
                    domains[domain] = 1
                    
        elif "Listening" in line:
            restarts += 1

    if len(lines) > 0:
        report = '[' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]\n"
        if len(sources) > 0:
            report += "    by Sources\n"
            for key, value in sources.items():
                report += "        " + str(value) + "    " + str(key) + "\n"
        if len(ports) > 0:
            report += "    by Ports\n"
            for key, value in ports.items():
                report += "        " + str(value) + "    " + str(key) + "\n"
        if len(users_passwords) > 0:
            report += "    by Credentials\n"
            for key, value in users_passwords.items():
                report += "        " + str(value) + "    " + str(key) + "\n"
        if len(domains) > 0:
            report += "    by Domains\n"
            for key, value in domains.items():
                report += "        " + str(value) + "    " + str(key) + "\n"
        if restarts > 0:
            report += "    Restarts counter\n        " + str(restarts)
    
        #print(report, flush=True)
        send_report(report.replace("\n", '<br />').replace("  ", ' &nbsp;'))

    #else:
    #    print('Dead silence...', flush=True)

    # Define sleeping time (default 10 minutes).
    time.sleep(60*10)
