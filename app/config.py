import secrets
from os import getenv

ALGORITHM = "HS256"
SECRET_KEY = secrets.token_urlsafe(32)

PARK_CAPACITY=int(getenv('PARK_CAPACITY', 'default'))
ACCESS_TOKEN_EXPIRE_MINUTES=int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 'default'))

if not PARK_CAPACITY:
    print("PARK_CAPACITY not set or empty. Using default value.")
    PARK_CAPACITY = 3

if not ACCESS_TOKEN_EXPIRE_MINUTES:
    print("ACCESS_TOKEN_EXPIRE_MINUTES not set or empty. Using default value.")
    ACCESS_TOKEN_EXPIRE_MINUTES = 5

USERS_DB = {
    "user": {
        "username": "user",
        "password": "passwd",
        "role": "user"
    },
    "admin": {
        "username": "admin",
        "password": "root",
        "role": "admin"
    }
}