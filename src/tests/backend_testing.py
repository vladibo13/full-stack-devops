import os
from dotenv import load_dotenv
import requests
from sqlalchemy import create_engine, MetaData, Table
import time
import pymysql

load_dotenv()

# API and Database setup
API_URL = "http://127.0.0.1:5000/api/users"
DB_URL = (
    f'mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}'
    f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
)

def test_post_get_delete_user(delete_user=False):
    # 1. Post new user data
    user_data = {"name": "Jane Doe", "email": "jane@example.com"}
    post_response = requests.post(API_URL, json=user_data)

    assert post_response.status_code == 201, f"POST failed: {post_response.text}"
    user_id = post_response.json()['id']
    print(f"User {user_data['name']} posted successfully with ID {user_id}!")

    # Wait for DB operations to complete
    time.sleep(1)

    # 2. GET the user by ID to verify the data
    get_response = requests.get(f"{API_URL}/{user_id}")
    assert get_response.status_code == 200, f"GET failed: {get_response.text}"
    expected_data = {"id": user_id, "name": "Jane Doe", "email": "jane@example.com"}
    assert get_response.json()['id'] == expected_data['id'], "Data mismatch!"
    print(f"User data retrieved and verified for ID {user_id}!")

    # 3. Verify the user exists in the database
    engine = create_engine(DB_URL)
    conn = engine.connect()
    metadata = MetaData()
    users = Table('user', metadata, autoload_with=engine)

    result = conn.execute(users.select().where(users.c.email == "jane@example.com")).fetchone()
    assert result is not None, "User not found in the database!"
    print(f"Result found in database: {result}")

    # 4. Delete the user from the database
    if delete_user:
        delete_response = requests.delete(f"{API_URL}/{user_id}")
        assert delete_response.status_code == 204, f"DELETE failed: {delete_response.text}"
        print(f"User with ID {user_id} deleted successfully!")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    test_post_get_delete_user(True)
