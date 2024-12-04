"""
получаает данные для лиг
"""
from common.common import DataParser
from common.models.data_parser import DataInterface

URLS = [
    # 'https://soccer365.ru/competitions/12',
    # 'https://soccer365.ru/competitions/16',
    # 'https://soccer365.ru/competitions/17',
    'https://soccer365.ru/competitions/15',
    # 'https://soccer365.ru/competitions/18/'
]
LEAGUE_NAME = [
    # 'en',
    # 'es',
    # 'ger',
    'ita',
    # 'fr'
]
for i in range(len(URLS)):
    next_games_block = DataParser(DataInterface(url=URLS[i])).get_http_data()
    data=DataInterface(
        text=next_games_block[40290:55994].replace('\t', '').replace('\n', '')
    )
    blank_html = DataParser(data).get_html_for_last_tour()
    crude_json = DataParser(DataInterface(html_text=blank_html)).tag_replacer()
    DataParser(DataInterface(html_text=LEAGUE_NAME[i],text=crude_json)).make_last_tour_data()
