import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# General application settings
APP_NAME = "AugmentX"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"  # Read from .env (default to False)
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")

# Paths for data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# API settings
API_VERSION = "v1"
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))

# Security settings
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Other settings
DEFAULT_AUGMENTATION_PROBABILITY = 0.5  # Default probability of applying augmentations
