import smtplib, ssl
from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk

from datetime import datetime


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "rpi.online.studio@gmail.com"  # Enter your address
password = "rpi#1824" # echo into environment variable when launch into server

def email_set_passwd(user_email, in_link):
    email_content = """\
        Dear User,

        Greetings.

        This is the online studio system. Your insturctors has just registered you for the platform. 

        Please complete your registration by clicking the link below and finish the process.

        {}

        Thank you very much.

        RPI ECSE, Online Studio Platform team.
        {}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)

        current_date = str(datetime.now()).split()[0]
        server.sendmail(sender_email, user_email, email_content.format(in_link, current_date))
    return