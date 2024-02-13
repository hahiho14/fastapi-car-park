from os import getenv

PARK_CAPACITY=int(getenv('PARK_CAPACITY', 'default'))

if not PARK_CAPACITY:
    print("Environment variable not set or empty. Using default value.")
    PARK_CAPACITY = 3