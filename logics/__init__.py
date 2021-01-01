from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk

storage_set_passwd = dict()

class User(object):
    def __init__(self, uid, user_email, passwd):
        self.uid = uid
        self.user_email = user_email
        self.passwd = passwd
        return
    
