import os
from dotenv import load_dotenv

from config.constants import COMMON_PROJECT, URL_SEGMENTS

# Load environment variables from .env file
load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://default.example.com/homepage")
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 60000))

    # Credentials read safely from environment
    VALID_USERNAME = os.getenv("VALID_USERNAME")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD")
    VALID_OKTAPASSWORD = os.getenv("VALID_OKTAPASSWORD")

    INVALID_USERNAME = os.getenv("INVALID_USERNAME", "invalid_user@test.com")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "WrongPassword123!")

    # Trax environment used to build page URLs (Cypress: baseUrl / projectName)
    TRAX_BASE_URL = os.getenv("TRAX_BASE_URL", URL_SEGMENTS["base_url_int"])
    PROJECT_NAME = os.getenv("PROJECT_NAME", COMMON_PROJECT)
