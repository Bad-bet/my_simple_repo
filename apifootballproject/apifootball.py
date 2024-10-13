import requests
import json
import html
import re

from common.common import DataParser, JsonConductor
from common.models.main_model import Command, History, Game, League
from common.models.data_parser import DataInterface, DataJsonInterface

urls = ['https://soccer365.ru/competitions/18/']

# next_games_block = DataParser(DataInterface(url=urls[0])).get_data()
#
# with open('bundes_ligue.txt', 'w') as file:
#     file.write(next_games_block)

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

print(json_schedule['data'])

NEAREST_SCHEDULE = League(
    league_id=1,
    game=Game(
        game=json_schedule['data'][0]['name'],
        date=json_schedule['data'][0]['startDate']
    )
)

LAST_RESULT = League(
    league_id=1,
    commands=Command(
        host='',
        guest='',
        history=History(
            score=-1,
            un_score=-1
        )
    ),
    game=Game(
        date=''
    ),


)
print (LAST_RESULT)