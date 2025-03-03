import os
from pathlib import Path
from dotenv import load_dotenv



load_dotenv()
password = os.getenv('MONGO_PASSWORD')
login = os.getenv('MONGO_LOGIN')



# Get the project root directory
ROOT_DIR = Path(__file__).parent.parent

# Load environment variables from .env file
load_dotenv(ROOT_DIR / '.env')

# Get environment from .env file, default to 'dev' if not set
ENV = os.getenv('TEST_ENV', 'dev').lower()

# Environment URLs
URLS = {
    'dev': 'http://the-internet.herokuapp.com',
    'uat': 'http://uat.the-internet.herokuapp.com',  # example URL
    'prod': 'http://prod.the-internet.herokuapp.com'  # example URL
}

# Environment URLs
Mongo_URLS = {
    'dev': f"mongodb+srv://admin:{password}@cluster0.example.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    'uat': f"mongodb+srv://admin:{password}@cluster0.example.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",  # example URL
    'prod': f"mongodb+srv://admin:{password}@cluster0.example.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",  # example URL
}



# Get base URL for current environment
def get_base_url() -> str:
    if ENV not in URLS:
        raise ValueError(f"Invalid environment: {ENV}. Must be one of: {', '.join(URLS.keys())}")
    return URLS[ENV]

# After the existing get_base_url function
def get_mongo_url() -> str:
    if ENV not in Mongo_URLS:
        raise ValueError(f"Invalid environment: {ENV}. Must be one of: {', '.join(Mongo_URLS.keys())}")
    return Mongo_URLS[ENV]

