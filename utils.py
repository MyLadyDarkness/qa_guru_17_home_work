import json
import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def load_schema(path=""):
    with open(path) as file:
        return json.loads(file.read())


def post_reqres(url, **kwargs):
    base_url = "https://reqres.in"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curlify.to_curl(response.request))
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response
