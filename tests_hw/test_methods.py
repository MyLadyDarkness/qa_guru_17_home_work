import requests
from jsonschema import validate

from schemas.put_update_user import put_update_user
from schemas.get_list_of_users import get_list_of_users
from schemas.get_single_user import get_single_user
from schemas.post_users import post_users

url = "https://reqres.in"
js_data = {"name": "murzik", "job": "lay on carpet"}


def test_get_list_of_users():
    endpoint = "/api/users"
    response = requests.get(url + endpoint)
    body = response.json()

    assert response.status_code == 200
    assert response.json()["total"] == 12
    assert response.json()["total_pages"] == 2
    assert response.json()["per_page"] == response.json()["total"] / response.json()["total_pages"]

    validate(body, schema=get_list_of_users)


def test_get_single_user():
    endpoint = "/api/users/2"
    response = requests.get(url + endpoint)
    body = response.json()

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

    validate(body, schema=get_single_user)


def test_get_user_not_found():
    endpoint = "/api/users/23"
    response = requests.get(url + endpoint)

    assert response.status_code == 404
    assert response.json() == {}


def test_post_create_user():
    endpoint = "/api/users"
    response = requests.post(url + endpoint, json=js_data)
    body = response.json()

    assert response.status_code == 201
    assert response.json()["name"] == js_data["name"]
    assert response.json()["job"] == js_data["job"]

    validate(body, schema=post_users)


def test_put_update_user():
    endpoint = "/api/users/2"
    response = requests.put(url + endpoint, json=js_data)
    body = response.json()

    assert response.status_code == 200
    assert response.json()["name"] == js_data["name"]
    assert response.json()["job"] == js_data["job"]

    validate(body, schema=put_update_user)


def test_delete_user():
    endpoint = "/api/users/2"
    response = requests.delete(url + endpoint)

    assert response.status_code == 204
    assert response.text == ""
