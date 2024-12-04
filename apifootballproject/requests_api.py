"""Получает данные для лиг"""
from common.models.data_parser import DataInterface, DataJsonInterface
from common.common import DataParser


URL = [
    # 'https://soccer365.ru/competitions/627/results/',
    # 'https://soccer365.ru/competitions/565/results/',
    # 'https://soccer365.ru/competitions/707/results/',
    # 'https://soccer365.ru/competitions/587/results/',
    # 'https://soccer365.ru/competitions/581/results/',
    'https://soccer365.ru/competitions/681/results/'
]
LEAGUE_NAME = [
    # 'ita-b',
    # 'en-b',
    # 'es-b',
    # 'ger-b',
    # 'fr-b',
    'por'
]
for i in range(len(URL)):
    next_games_block = DataParser(DataInterface(url=URL[i])).get_http_data()
    data = DataInterface(html_text=None)
    if LEAGUE_NAME[i] == 'ita-b':
        data = DataInterface(
            html_text=next_games_block[22100:31650].replace('\t', '').replace('\n', '').replace('1919','')
        )
    elif LEAGUE_NAME[i] == 'en-b':
        data = DataInterface(
            html_text=next_games_block[24100:41450].replace('\t', '').replace('\n', '')
        )
    elif LEAGUE_NAME[i] == 'ger-b':
        data = DataInterface(
            html_text=next_games_block[22100:31050].replace('\t', '').replace('\n', '').replace('98','').replace(' 07','').replace('м 1846','м')
        )
    elif LEAGUE_NAME[i] == 'es-b':
        data = DataInterface(
            html_text=next_games_block[22100:37850].replace('\t', '').replace('\n', '')
        )
    elif LEAGUE_NAME[i] == 'fr-b':
        data = DataInterface(
            html_text=next_games_block[44300:63700].replace('\t', '').replace('\n', '')
        )
    elif LEAGUE_NAME[i] == 'por':
        data = DataInterface(
            html_text=next_games_block[26600:36800].replace('\t', '').replace('\n', '')
        )
    crude_json = DataParser(data).tag_replacer()
    new_data = DataInterface(
        html_text=LEAGUE_NAME[i],
        text=crude_json
    )

    DataParser(new_data).make_result_league()

# print(crude_json)

# Запись json'a
# print(my_data)
