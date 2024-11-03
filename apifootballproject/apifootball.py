import json

import attrs

from common.utils.utils import ready_announce_10, ready_announce_9
from common.common import DataParser
from common.utils.utils import JsonConductor
from common.models.data_parser import DataInterface, DataJsonInterface
from common.data_maker import DataAnnounceMaker


URLS = [
    'https://soccer365.ru/competitions/12',
    'https://soccer365.ru/competitions/16',
    'https://soccer365.ru/competitions/17',
    'https://soccer365.ru/competitions/15',
]
LEAGUE_NAME = ['en','es','ger','ita']
england_announce = []
spain_announce = []
germany_announce = []
italy_announce = []

es_announce_data = {}
ger_announce_data = {}
ita_announce_data = {}

for i in range(len(URLS)):
    next_games_block = DataParser(DataInterface(url=URLS[i])).get_http_data()
    data = DataInterface(
        html_text=next_games_block[28900:47350]
    )
    crude_json = DataParser(data).tag_replacer()

    for_json_data = DataJsonInterface(
        write_json_data=DataParser(DataInterface(text=crude_json)).make_next_tour_json(),
        json_next_tour_name=f'next_tour_{LEAGUE_NAME[i]}_json.json'
    )
    # Запись json'a
    JsonConductor(for_json_data).json_record()
    json_schedule = JsonConductor(DataJsonInterface(
        json_next_tour_name=for_json_data.json_next_tour_name)
    ).get_from_json()

    if LEAGUE_NAME[i] == 'en':
        england_announce = DataAnnounceMaker(data=json_schedule, name=LEAGUE_NAME[i]).bild_ten_events()
    elif LEAGUE_NAME[i] == 'es':
        spain_announce = DataAnnounceMaker(data=json_schedule, name=LEAGUE_NAME[i]).bild_ten_events()
    elif LEAGUE_NAME[i] == 'ger':
        germany_announce = DataAnnounceMaker(data=json_schedule, name=LEAGUE_NAME[i]).build_nine_events()
    elif LEAGUE_NAME[i] == 'ita':
        italy_announce = DataAnnounceMaker(data=json_schedule, name=LEAGUE_NAME[i]).bild_ten_events()




print()


en_announce_data = DataJsonInterface(
    write_json_data=json.dumps(ready_announce_10(england_announce), ensure_ascii=False),
    json_next_tour_name=f'announce_next_tour_en.json'
)
JsonConductor(en_announce_data).json_update_record()

en_announce_data = DataJsonInterface(
    write_json_data=json.dumps(ready_announce_10(spain_announce), ensure_ascii=False),
    json_next_tour_name=f'announce_next_tour_es.json'
)
JsonConductor(en_announce_data).json_update_record()

en_announce_data = DataJsonInterface(
    write_json_data=json.dumps(ready_announce_10(italy_announce), ensure_ascii=False),
    json_next_tour_name=f'announce_next_tour_ita.json'
)
JsonConductor(en_announce_data).json_update_record()

en_announce_data = DataJsonInterface(
    write_json_data=json.dumps(ready_announce_9(germany_announce), ensure_ascii=False),
    json_next_tour_name=f'announce_next_tour_ger.json'
)
JsonConductor(en_announce_data).json_update_record()