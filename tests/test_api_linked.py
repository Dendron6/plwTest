from api.linkedin_lesson_api.api_client import ApiClient
import os
from dotenv import load_dotenv

load_dotenv()
BASEURL_API = os.getenv("API_URL")
api_client = ApiClient()

# @pytest.fixture(scope="session")
# def api_client():
#     return ApiClient()

# Initialize API client
api_client = ApiClient()
this_task = "Task Number 2"

def test_open_api_documentation(page):
    page.goto(BASEURL_API)
    # Take a screenshot
    page.screenshot(path="api-docs.png")

# def test_get_token():
#     token = api_client.get_token()
#     print(f"Token: {token}")
#     assert token is not None

def test_create_task():
    """Create a task with name Task Number 2"""
    # api_client = ApiClient()
    response = api_client.create_new_task(this_task)
    # token = api_client.get_token()
    # print(f"Token: {token}")
    # print(f"Response: {response}")
    assert response is not None

def test_get_tasks():
    """Get all tasks"""
    response = api_client.get_tasks()
    print(f"Response: {response}")


# def test_verify_task():
#     """Verify that the task exists based on the id"""
#     task_id = api_client.get_tesks_by_description(this_task)
#     response = api_client.verify_task(this_task, task_id)
#     print(f"Response: {response}")
#     assert response is True

# def test_delete_task():
#     """Delete task number 2"""
#     task_id = api_client.get_tesks_by_description(this_task)
#     response = api_client.delete_task(task_id)
#     assert response is not None
