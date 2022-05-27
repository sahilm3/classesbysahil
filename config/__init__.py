import os

class Config:
    API_ID = int(os.environ.get('API_ID', 8763712))
    API_HASH = os.environ.get('API_HASH', "835d27216f117e22a5c192b89a4ce457")
    TOKEN = os.getenv("token","5383986748:AAF6E0nTxExvqSMMdChsnSBA-yUXVxrdZ8U")
    DOMAIN  = os.getenv("domain","https://newdlstar.herokuapp.com")
    CHANNEL = int(os.getenv("channel","-1001631582129") )
