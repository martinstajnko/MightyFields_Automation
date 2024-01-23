import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

URL = os.getenv('URL')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')