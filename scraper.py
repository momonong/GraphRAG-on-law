import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Step 1: Authenticate and get token
auth_url = "https://data.judicial.gov.tw/jdg/api/Auth"
auth_data = {
    "user": os.getenv("USER"),  # Use environment variable for user
    "password": os.getenv("PASSWORD")  # Use environment variable for password
}
auth_response = requests.post(auth_url, json=auth_data)
token = auth_response.json().get("token")
print('token:', token)

# Step 2: Get list of judgment changes
if token:
    jlist_url = "https://data.judicial.gov.tw/jdg/api/JList"
    jlist_data = {"token": token}
    jlist_response = requests.post(jlist_url, json=jlist_data)
    changes = jlist_response.json()
    print("Judgment Changes:", changes)

    # Step 3: Retrieve a specific judgment's content
    for entry in changes:
        for jid in entry["LIST"]:
            jdoc_url = "https://data.judicial.gov.tw/jdg/api/JDoc"
            jdoc_data = {"token": token, "j": jid}
            jdoc_response = requests.post(jdoc_url, json=jdoc_data)
            judgment_content = jdoc_response.json()
            print("Judgment Content:", judgment_content)