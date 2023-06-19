import requests
import random
import allure

random_id = random.randint(1, 10)
response = requests.get(f"https://reqres.in/api/users?id={random_id}")

@allure.id("TC-03")
@allure.title("API get user test")
def test_api_get_user():
    assert response.status_code == 200 or 201 or 202
    data = response.json()
    assert data["data"]["id"] == random_id
    for a, b in data["data"].items():
        print(a, ":", b)
