import requests
import json
import html
import re

from common.common import DataParser, JsonConductor
from common.models.main_model import Command, History, Game, League
from common.models.data_parser import DataInterface, DataJsonInterface

urls = [
    'https://soccer365.ru/competitions/12',
    'https://soccer365.ru/competitions/16',
    'https://soccer365.ru/competitions/17',
    'https://soccer365.ru/competitions/15',
]

for i in urls:
    next_games_block = DataParser(DataInterface(url=i)).get_http_data()
    data=DataInterface(
        text=next_games_block[40490:52350].replace('\t', '').replace('\n', '')
    )
    blank_html = DataParser(data).get_html_for_last_tour()
    crude_json = DataParser(DataInterface(html_text=blank_html)).tag_replacer()
    last_tour_json = DataParser(DataInterface(text=crude_json)).make_last_tour_data()
    print('\n'+last_tour_json)


# next_games_block = DataParser(DataInterface(url=urls[0])).get_http_data()
# with open('bundes_ligue.txt', 'w') as file:
#     file.write(next_games_block)


# with open('bundes_ligue.txt', 'r') as f:
#     crude_block = f.read()
#     # print(crude_block[28900:32000])
#     # print(crude_block[41700:54350].replace('\t', '').replace('\n', ''))
#     data=DataInterface(
#         text=crude_block[40690:52350].replace('\t', '').replace('\n', '')
#     )
#     blank_html = DataParser(data).get_html_for_last_tour()
#     crude_json = DataParser(DataInterface(html_text=blank_html)).tag_replacer()


# last_tour_json = DataParser(DataInterface(text=crude_json)).make_last_tour_data()
# print(last_tour_json)

# # Запись json'a
# JsonConductor(for_json_data).next_tour_record()
# json_schedule = JsonConductor(DataJsonInterface(
#     write_json_data='',
#     json_next_tour_name=for_json_data.json_next_tour_name)
# ).next_tour_json()
#
# print(json_schedule['data'][0])
#
# NEAREST_SCHEDULE = League(
#     league_id=1,
#     game=Game(
#         game=json_schedule['data'][0]['name'],
#         date=json_schedule['data'][0]['startDate']
#     )
# )
#
# LAST_RESULT = League(
#     league_id=1,
#     commands=Command(
#         host='',
#         guest='',
#         history=History(
#             score=-1,
#             un_score=-1
#         )
#     ),
#     game=Game(
#         date=''
#     ),
#
#
# )
# print (LAST_RESULT)