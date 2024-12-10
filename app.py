from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

print(f"API Key: {api_key}")
print(f"Secret Key: {secret_key}")