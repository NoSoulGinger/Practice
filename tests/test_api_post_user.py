import requests
import allure

url = "https://reqres.in/api/users"
data = {"name": "Elek", "job": "Tester"}

@allure.id("TC-02")
@allure.title("API post user test")
def test_api_post_user():
    response = requests.post(url, json=data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 201
    assert response_data["name"] == data["name"]
    assert response_data["job"] == data["job"]
