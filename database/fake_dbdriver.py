from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk

from logics import encrypter, User, storage_set_passwd
from os import path
import csv

def gen_user(filename, all_users_idkey, all_users_ekey, mode):
    temp_id_increment = int(max(all_users_idkey.keys()))
    ref_path = path.split(__file__)[0]
    with open(path.join(ref_path, "data", filename), 'r') as f_users_debug:
        csv_reader = csv.reader(f_users_debug, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                if mode == "debug":
                    user_email = row[0]
                    user_passwd = encrypter.encrypt_password(row[1])
                    if user_email not in all_users_ekey.keys():
                        
                        temp_id_increment += 1
                        temp_user = User(str(temp_id_increment), user_email, user_passwd)\
                        
                        all_users_ekey[user_email] = temp_user
                        all_users_idkey[str(temp_id_increment)] = temp_user
                elif mode == "email":
                    temp_id_increment += 1
                    

            line_count += 1
    return 


def gen_users_from_email(filename, all_users_idkey, all_users_ekey):
    temp_id_increment = int(str(max(all_users_idkey.keys())))
    ref_path = path.split(__file__)[0]
    with open(path.join(ref_path, "data", filename), 'r') as f_users_email:
        csv_reader = csv.reader(f_users_email, delimiter=',')
        pass
    return

all_users_ekey = dict()
all_users_idkey = dict()

DEBUG_ADMIN = User('0', "onlinestudioadmin@rpi.edu", encrypter.encrypt_password("admin"))

all_users_ekey[DEBUG_ADMIN.user_email] = DEBUG_ADMIN
all_users_idkey[DEBUG_ADMIN.uid] = DEBUG_ADMIN

try:
    gen_user_debug("users_debug.csv", all_users_idkey, all_users_ekey)
except FileNotFoundError:
    print("No Debug Users file avalibale, skippped. ")


