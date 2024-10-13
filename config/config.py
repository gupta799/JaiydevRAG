import json
import os
import secrets
from dotenv import load_dotenv
load_dotenv()

class Config:  
    REDIS_HOST = os.getenv('REDIS_HOST') or 'abc'
    REDIS_PORT = os.getenv('REDIS_PORT') or 'abc'
    REDIS_PASSWORD = os.getenv('REDIS_PORT') or 'abc'
    JWT_SECRET_KEY = secrets.token_hex(16)
    USERS_FILE_PATH = os.path.join(os.path.dirname(__file__), 'users.json')
    with open(USERS_FILE_PATH) as users_file:
        USERS = json.load(users_file)['users']    