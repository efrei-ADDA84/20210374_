# TSAMPI Augusta 

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APIKEY = os.environ.get('APIKEY')
    LAT = os.environ['LAT']  
    LONG = os.environ['LONG'] 