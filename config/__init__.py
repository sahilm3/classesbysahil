import os

class Config:
    API_ID = int(os.environ.get('API_ID', 0))
    API_HASH = os.environ.get('API_HASH', None)
    TOKEN = os.getenv("token","xxxxx")
    DOMAIN  = os.getenv("domain","https://newdlstar.herokuapp.com")