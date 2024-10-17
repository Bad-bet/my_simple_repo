import attrs
import requests
import json
import html
import re

from common.common import DataParser, JsonConductor
from common.models.main_model import Command, History, Game, League
from common.models.data_parser import DataInterface, DataJsonInterface

urls = ['https://soccer365.ru/competitions/17/']

next_games_block = DataParser(DataInterface(url=urls[0])).get_http_data()

with open('bundes_ligue.txt', 'w') as file:
    file.write(next_games_block)

"""
data = DataInterface(
    html_text=next_games_block[28900:47350]
)
crude_json = DataParser(data).tag_replacer()
"""

with open('bundes_ligue.txt', 'r') as f:
    crude_block = f.read()
    # print(crude_block[28900:32000])
    # print(crude_block[39000:41350])
    data=DataInterface(
        html_text=crude_block[28900:45350]
    )
    crude_json = DataParser(data).tag_replacer()

# print(get_data(crude_json))
for_json_data = DataJsonInterface(
    write_json_data=DataParser(DataInterface(text=crude_json)).make_next_tour_json(),
    json_next_tour_name=f'next_tour_json.json'
)
# Запись json'a
JsonConductor(for_json_data).json_record()
json_schedule = JsonConductor(DataJsonInterface(
    json_next_tour_name=for_json_data.json_next_tour_name)
).get_from_json()

for i in range(9):
    print(json_schedule['data'][i]['name'])

NEAREST_SCHEDULE = League(
    league_name='en',
    game=Game(
        game=json_schedule['data'][0]['name'],
        date=json_schedule['data'][0]['startDate']
    ),
    commands=Command(
        host=json_schedule['data'][0]['performer'][0]['name'],
        guest=json_schedule['data'][0]['performer'][1]['name'],
        history_host=[
            History(
                score=None,
                un_score=3
            ),
            History(
                score=1,
                un_score=0
            )
        ],
        history_guest=[
            History(
                score=0,
                un_score=3
            ),
            History(
                score=2,
                un_score=3
            )
        ]
    )
)

# print (attrs.asdict(NEAREST_SCHEDULE))