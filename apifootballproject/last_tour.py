import requests
import json
import html
import re

from common.common import DataParser, JsonConductor, DataBaseConductor, DataBaseConductor
from common.models.main_model import Command, History, Game, League
from common.models.data_parser import DataInterface, DataJsonInterface, DataDBConductorInterface

URLS = [
    'https://soccer365.ru/competitions/12',
    'https://soccer365.ru/competitions/16',
    'https://soccer365.ru/competitions/17',
    'https://soccer365.ru/competitions/15',
]
LEAGUE_NAME = ['en','es','ger','ita']
for i in range(len(URLS)):
    next_games_block = DataParser(DataInterface(url=URLS[i])).get_http_data()
    data=DataInterface(
        text=next_games_block[40290:55994].replace('\t', '').replace('\n', '')
    )
    blank_html = DataParser(data).get_html_for_last_tour()
    crude_json = DataParser(DataInterface(html_text=blank_html)).tag_replacer()
    DataParser(DataInterface(html_text=LEAGUE_NAME[i],text=crude_json)).make_last_tour_data()
    # DataBaseConductor(data=dict_data).write_to_db()
    # LAST_RESULT = League(
    #     league_id=LEAGUE_IDS[i],
    #     commands=Command(
    #         host=dict_data['data'][i]['host_command'],
    #         guest=dict_data['data'][i]['guest_command'],
    #         history=History(
    #             score=dict_data['data'][i]['host_score'],
    #             un_score=dict_data['data'][i]['guest_score']
    #         )
    #     ),
    #     game=Game(
    #         date=dict_data['data'][i]['game']
    #     ),
    # )
    # print (LAST_RESULT)

# data = DataDBConductorInterface(
#     league_idx='en',
#     date=dates['22.09,14:30','22.09,14:30','21.09,14:30','21.09,14:30','21.09,14:30','21.09,14:30','21.09,14:30','21.09,14:30','21.09,14:30','21.09,14:30'],
#     host_command=host_league_commands['МанСити','Брайтон','КристалПэлас','АстонВилла','Тоттенхэм','Саутгемптон','Ливерпуль','ЛестерСити','Фулхэм','ВестХэм'],
#     guest_command=guest_league_commands['Арсенал','НоттингемФорест','МанЮнайтед','Вулверхэмптон','Брентфорд','ИпсвичТаун','Борнмут','Эвертон','Ньюкасл','Челси'],
#     host_score=host_score['2','2','0','3','3','1','3','1','3','0'],
#     guest_score=guest_score['2','2','0','1','1','1','0','1','1','3']
# )


# data = DataDBConductorInterface(
#     league_idx='es',
#     date=['19.08,14:30','19.08,14:30','18.08,14:30','18.08,14:30','17.08,14:30','17.08,14:30','16.08,14:30','16.08,14:30','15.08,14:30','15.08,14:30'],
#     host_command=['Вильярреал','РеалВальядолид','Мальорка','РеалСосьедад','Валенсия','Осасуна','ЛасПальмас','Сельта','Бетис','Атлетик'],
#     guest_command=['АтлетикоМадрид','Эспаньол','РеалМадрид','РайоВальекано','Барселона','Леганес','Севилья','Алавес','Жирона','Хетафе'],
#     host_score=['2','1','1','1','1','1','2','2','1','1'],
#     guest_score=['2','0','1','2','2','1','2','1','1','1']
# )
#
# DataBaseConductor(data).write_to_db()





# 'РеалВальядолид', 'Хетафе', 'РайоВальекано', 'РеалСосьедад', 'Осасуна', 'Сельта', 'Атлетик', 'Бетис', 'АтлетикоМадрид', 'Вильярреал'],
#
# ['Мальорка', 'Алавес', 'Леганес', 'Валенсия', 'Барселона', 'Жирона', 'Севилья', 'Эспаньол', 'РеалМадрид', 'ЛасПальмас'],


