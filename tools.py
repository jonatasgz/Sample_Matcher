import os
import secrets
from dotenv import load_dotenv

def get_secret():
    if load_dotenv():
        return os.getenv('MATCHER_SECRET_KEY')
    else:
        key = secrets.token_hex()
        file = open('.env', 'w')
        file.write(f'MATCHER_SECRET_KEY={key}')
        return key