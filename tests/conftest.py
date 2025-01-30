import pytest
from playwright.sync_api import Page, expect
from tests.config import get_base_url, get_mongo_url
import pymongo
import os

# Define base URL as a fixture
@pytest.fixture(scope="session")
def base_url() -> str:
    return get_base_url()

@pytest.fixture(scope="session")
def mongo_connection():
    # Establish connection
    client = pymongo.MongoClient(get_mongo_url())
    yield client
    # Close connection
    client.close()

@pytest.fixture(scope="session")
def mongo_operations(mongo_connection):
    class MongoOperations:
        def __init__(self, client):
            self.client = client
        
        def find_one(self, db_name: str, collection_name: str, query: dict):
            db = self.client[db_name]
            collection = db[collection_name]
            return collection.find_one(query)
        
        def update_one(self, db_name: str, collection_name: str, query: dict, update_data: dict):
            db = self.client[db_name]
            collection = db[collection_name]
            return collection.update_one(query, {"$set": update_data})
        
        def insert_one(self, db_name: str, collection_name: str, data: dict):
            db = self.client[db_name]
            collection = db[collection_name]
            return collection.insert_one(data)
    
    return MongoOperations(mongo_connection)

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close() 