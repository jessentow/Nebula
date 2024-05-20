import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Accessing environment variables
prod_db_host = os.getenv("PROD_DB_HOST")
prod_db_pass = os.getenv("PROD_DB_PASS")
prod_db_name = os.getenv("PROD_DB_NAME")
prod_db_user = os.getenv("PROD_DB_USER")
secret_key=os.getenv("SECRET_KEY")