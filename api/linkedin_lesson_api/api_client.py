import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
API_USERNAME = os.getenv("API_USERNAME")
API_PASSWORD = os.getenv("API_PASSWORD")

class ApiClient:
    def __init__(self):
        self.base_url = API_URL
        self.username = API_USERNAME
        self.password = API_PASSWORD

    # this is example of api token that uses username and password and application/x-www-form-urlencoded
    def get_token(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(
            f"{self.base_url}/token/",
            data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        return response.json()["access_token"]


    def create_new_task(self, text: str, status: str = "Draft"):
        try:
            response = requests.post(
                f"{self.base_url}/tasks",
                json={
                    "description": text,
                    "status": status,
                    "created_by": self.username  # user for task creation and deletion permissions
                }
            )
            return response.json()
        except requests.RequestException as e:
            print(f'API Error: {e}')
            raise e

    def verify_task(self, text: str, id: int):
        try:
            response = requests.get(
                f"{self.base_url}/tasks/{id}"
            )
            return response == text
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_tasks(self):
        try:
            response = requests.get(
            f"{self.base_url}/tasks/"
            )
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_tesks_by_description(self, description: str):
        response = self.get_tasks()
        for task in response:
            if description in task[description]:
                return task
        return {"error": "Task not found"}

    def delete_task(self, user_id: int):
        try:
            token = self.get_token()
            requests.delete(
                f"{self.base_url}/tasks/{user_id}",{
                    'headers':{
                        "accept": "application/json",
                        "Authorization": f"Bearer {token}"}
                }

            )
        except requests.RequestException as e:
            return {"error": str(e)}

    def get(self, endpoint: str):
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                headers={"Authorization": f"Bearer {self.get_token()}"}
            )
            return response.data
        except requests.RequestException as e:
            return {"error": str(e)}
