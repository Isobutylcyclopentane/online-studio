from flask import request, redirect, url_for
from datetime import date, datetime
from json import JSONEncoder
from passlib.context import CryptContext

# temporary storage places for password changing and registration process
registration_storage = dict()
change_password_storage = dict()

# security measure for admin access 
# ensure no user can change their own user type to admin 
admin_uids = ["0"]

# encrypter initializer
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=1000
)

def encrypt_password(password):
    """
    function for encrypting the password, not recoverale
    return a string
    """
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    """
    function for checking if the input password from user was correct
    return Boolean
    """
    return pwd_context.verify(password, hashed)
