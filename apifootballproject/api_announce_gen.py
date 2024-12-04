import json

import requests
from common.utils.utils import JsonConductor
from common.models.data_parser import DataInterface, DataJsonInterface
from common.common import DataParser
from common.position_maker import PositionMaker
from common.data_maker import DataAnnounceMaker
from common.utils.utils import (
    ready_announce_10,
    ready_announce_11,
    ready_announce_9,
    ready_announce_12
)

URLS = [
    # 'https://soccer365.ru/competitions/627/shedule/',
    # 'https://soccer365.ru/competitions/587/shedule/',
    # 'https://soccer365.ru/competitions/565/shedule/',
    # 'https://soccer365.ru/competitions/581/shedule',
    'https://soccer365.ru/competitions/707/shedule/'
]
LEAGUE_NAME = [
    # 'ita-b',
    # 'ger-b',
    # 'en-b',
    # 'fr-b',
    'es-b'
]

seriaB_announce = []
ger_leagueB_announce = []
fr_leagueB_announce = []
en_leagueB_announce = []
es_leagueB_announce = []

for i in range(len(URLS)):
    fragment = ''

    next_games_block = DataParser(DataInterface(url=URLS[i])).get_http_data()
    if LEAGUE_NAME[i] == 'ita-b':
        fragment = next_games_block[22100:36000].replace('\t', '')
    elif LEAGUE_NAME[i] == 'ger-b':
        fragment = next_games_block[22100:36000].replace('\t', '')
    elif LEAGUE_NAME[i] == 'en-b':
        fragment = next_games_block[34100:48600].replace('\t', '')
    elif LEAGUE_NAME[i] == 'fr-b':
        fragment = next_games_block[27000:39000].replace('\t', '')
    elif LEAGUE_NAME[i] == 'es-b':
        fragment = next_games_block[22100:44000].replace('\t', '')
    data = DataInterface(
        html_text=fragment
    )
    #___________________my schedule________
    my_schedule = DataParser(data).make_my_schedule()
    # print(my_schedule)
    for_json_data = DataJsonInterface(
        write_json_data=json.dumps(my_schedule, ensure_ascii=False),
        json_next_tour_name=f'next_tour_{LEAGUE_NAME[i]}_json.json'
    )
    #_________________________________________
    # crude_json = DataParser(data).tag_replacer()
    # for_json_data = DataJsonInterface(
    #     write_json_data=DataParser(DataInterface(text=crude_json)).make_next_tour_json(),
    #     json_next_tour_name=f'next_tour_{LEAGUE_NAME[i]}_json.json'
    # )
    # Запись json'a
    JsonConductor(for_json_data).json_record()
    json_schedule = JsonConductor(DataJsonInterface(
        json_next_tour_name=for_json_data.json_next_tour_name)
    ).get_from_json()
    # print(json_schedule)
    update_schedule = PositionMaker(data=json_schedule, name=LEAGUE_NAME[i]).make_result()
    # if LEAGUE_NAME[i] == 'ita-b':
    #     seriaB_announce = DataAnnounceMaker(data=update_schedule, name=LEAGUE_NAME[i]).bild_ten_events()

    # if LEAGUE_NAME[i] == 'ger-b':
    #     ger_leagueB_announce = DataAnnounceMaker(data=update_schedule, name=LEAGUE_NAME[i]).build_nine_events()
    #
    # elif LEAGUE_NAME[i] == 'en-b':
    #     en_leagueB_announce = DataAnnounceMaker(data=update_schedule, name=LEAGUE_NAME[i]).build_twelve_events()

    if LEAGUE_NAME[i] == 'es-b':
        es_leagueB_announce = DataAnnounceMaker(data=update_schedule, name=LEAGUE_NAME[i]).build_eleven_events()

    # elif LEAGUE_NAME[i] == 'fr-b':
    #     fr_leagueB_announce = DataAnnounceMaker(data=update_schedule, name=LEAGUE_NAME[i]).build_nine_events()

# print(fr_leagueB_announce)

# ita_b_announce_data = DataJsonInterface(
#     write_json_data=json.dumps(ready_announce_10(seriaB_announce), ensure_ascii=False),
#     json_next_tour_name=f'./outputs/announce_next_tour_itaB.json'
# )
# JsonConductor(ita_b_announce_data).json_update_record()

# ger_announce_data = DataJsonInterface(
#     write_json_data=json.dumps(ready_announce_9(ger_leagueB_announce), ensure_ascii=False),
#     json_next_tour_name=f'./outputs/announce_next_tour_gerB.json'
# )
# JsonConductor(ger_announce_data).json_update_record()
#
# fr_announce_data = DataJsonInterface(
#     write_json_data=json.dumps(ready_announce_9(fr_leagueB_announce), ensure_ascii=False),
#     json_next_tour_name=f'./outputs/announce_next_tour_frB.json'
# )
# JsonConductor(fr_announce_data).json_update_record()
#
# en_b_announce_data = DataJsonInterface(
#     write_json_data=json.dumps(ready_announce_12(en_leagueB_announce), ensure_ascii=False),
#     json_next_tour_name=f'./outputs/announce_next_tour_enB.json'
# )
# JsonConductor(en_b_announce_data).json_update_record()

es_b_announce_data = DataJsonInterface(
    write_json_data=json.dumps(ready_announce_11(es_leagueB_announce), ensure_ascii=False),
    json_next_tour_name=f'./outputs/announce_next_tour_esB.json'
)
JsonConductor(es_b_announce_data).json_update_record()

# print(ger_leagueB_announce)
# for j in range(10):
#     print(json_schedule['data'][j]['performer'][0]['name'])
#     print(json_schedule['data'][j]['performer'][1]['name'])