from flask import request, redirect, url_for
from datetime import date, datetime
from json import JSONEncoder
from passlib.context import CryptContext

NUM_OF_ENCRY_ROUND = 1000

# encrypter initializer
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=NUM_OF_ENCRY_ROUND
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
