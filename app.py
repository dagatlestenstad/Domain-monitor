import config
import os
import yaml
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText


def get_html_from_browser(url, delay=0):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--no-sandbox')

    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    time.sleep(delay) 
    html = browser.page_source
    browser.quit()

    return html


def get_text_from_tagname(html, tag, name):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find(tag, {name}).text


def send_email(to, subject, body, sender=None):

    if sender is None:
        sender_email = config.mail_username
    else:
        sender_email = sender
        
    msg = MIMEText(body)
    msg["From"] = sender_email
    msg["To"] = to
    msg["Subject"] = subject 

    with smtplib.SMTP_SSL(host=config.mail_host, port=config.mail_port) as server:
        server.login(user=config.mail_username, password=config.mail_password)
        server.sendmail(sender_email, to, msg.as_string())
        server.quit()


if __name__ == '__main__':
    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'domains.yaml'), 'r') as stream:
        domains = yaml.safe_load(stream)
                
        for domain in domains['Domains']:
            html = get_html_from_browser('https://www.webhuset.no/bestillingsskjema/domenesok?coupon-2=&fqdn='+ domain, 2)
            status = get_text_from_tagname(html, 'div', 'col-xs-12 result-text').strip()
            print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " " + domain + ": " + status)

            if status.find("ledig") != -1:
                email = domains['Email']
                send_email(email, domain + " is finaly available!", "")