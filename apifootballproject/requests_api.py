import json

import requests
from common.utils.utils import JsonConductor
from common.models.data_parser import DataInterface, DataJsonInterface
from common.common import DataParser


URL = [
    'https://soccer365.ru/competitions/627/results/',
    'https://soccer365.ru/competitions/565/results/',
    'https://soccer365.ru/competitions/707/results/',
    'https://soccer365.ru/competitions/18/results/',
    'https://soccer365.ru/competitions/587/results/'
]

next_games_block = DataParser(DataInterface(url=URL[4])).get_http_data()
data = DataInterface(
    html_text=next_games_block[22100:174950].replace('\t', '').replace('\n', '')
)
crude_json = DataParser(data).tag_replacer()
new_data = DataInterface(
    text=crude_json
)

DataParser(new_data).make_result_league()

# print(crude_json)

# Запись json'a
# print(my_data)
