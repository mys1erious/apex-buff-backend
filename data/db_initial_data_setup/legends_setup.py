import requests
import json

from constants import *


def legends_data_from_file(file):
    with open(file, 'r') as f:
        data = json.load(f)

        return data


def post_legend(url, legend):
    response = requests.post(url+'/legends/', data=legend)
    return response


def post_legends(url, data):
    for i, legend in enumerate(data['legends']):
        response = post_legend(url, legend)

        if not response.ok:
            print(i, response.status_code, response.json())


def setup():
    data = legends_data_from_file(PATH_TO_LEGENDS_JSON)
    post_legends(BASE_API_URL, data)
