import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

URL = os.getenv('URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')