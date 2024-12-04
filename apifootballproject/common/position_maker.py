import re

from common.models.data_parser import DataInterface
from common.common import DataParser

class PositionMaker:
    def __init__(self, *, data: dict, name:str):
        self.data = data
        self.name = name
        self.URLS = [
            'https://soccer365.ru/competitions/627/',
            'https://soccer365.ru/competitions/587/',
            'https://soccer365.ru/competitions/565/',
            'https://soccer365.ru/competitions/581/',
            'https://soccer365.ru/competitions/707/',
            'https://soccer365.ru/competitions/681/',
            'https://soccer365.ru/competitions/12',
            'https://soccer365.ru/competitions/16',
            'https://soccer365.ru/competitions/17',
            'https://soccer365.ru/competitions/15',
            'https://soccer365.ru/competitions/18/'
        ]

    def get_position(self) -> dict:
        """
        description: ходит за данными по урлам в зависимости от лиги
        :return: словарь позиций
        """
        command_position = []
        command_name = []
        data = {}
        next_games_block, a = '', ''

        if self.name == 'fr-b':
            next_games_block += DataParser(DataInterface(url=self.URLS[3])).get_http_data()
            a = next_games_block[20000:36000].replace('\t', '')
        elif self.name == 'en-b':
            next_games_block += DataParser(DataInterface(url=self.URLS[2])).get_http_data()
            a = next_games_block[20000:42000].replace('\t', '')
        elif self.name == 'ita-b':
            next_games_block += DataParser(DataInterface(url=self.URLS[0])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '').replace('1919', '')
        elif self.name == 'ger-b':
            next_games_block += DataParser(DataInterface(url=self.URLS[1])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'es-b':
            next_games_block += DataParser(DataInterface(url=self.URLS[4])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'por':
            next_games_block += DataParser(DataInterface(url=self.URLS[5])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'en':
            next_games_block += DataParser(DataInterface(url=self.URLS[6])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'es':
            next_games_block += DataParser(DataInterface(url=self.URLS[7])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'ger':
            next_games_block += DataParser(DataInterface(url=self.URLS[8])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'ita':
            next_games_block += DataParser(DataInterface(url=self.URLS[9])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')
        elif self.name == 'fr':
            next_games_block += DataParser(DataInterface(url=self.URLS[10])).get_http_data()
            a = next_games_block[17000:40000].replace('\t', '')

        my_position = re.findall(r'<div class="plc.*\n.*', a)
        my_position = [i.replace('{"contentAsHTML":true}','') for i in my_position]
        my_position = [i.replace('ucl has-tip" title="Повышение" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('uclq has-tip" title="Повышение - плей-офф" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('rel has-tip" title="Понижение" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('relpo has-tip" title="Понижение - плей-офф" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('clr3 has-tip" title="Повышение - 1/2 финала" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('ucl has-tip" title="Лига чемпионов УЕФА - общий этап" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('eulq has-tip" title="Лига Европы УЕФА - общий этап" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('lightgreen has-tip" title="Лига конференций УЕФА - раунд плей-офф" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('lightblue has-tip" title="Лига чемпионов УЕФА - квалификация" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('green has-tip" title="Лига конференций УЕФА - квалификация" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('clr5 has-tip" title="Лига Европы УЕФА - квалификация" data-tooltipster=', '') for i in my_position]
        my_position = [i.replace('н 07</a>', 'н</a>') for i in my_position]
        my_position = [i.replace('м 1846</a>', 'м</a>') for i in my_position]
        my_position = [i.replace('т 98</a>', 'т</a>') for i in my_position]
        my_position = [i.replace(" ''", '+') for i in my_position]
        my_position = [i.replace('+', '"') for i in my_position]
        # my_position = [i.replace('-', '') for i in my_position]

        # print(my_position[2])
        # print(my_position[19])
        for i in my_position:
            string = ''.join(re.findall(r'plc..\d.', i))
            command_position.append(
                string.replace('plc">', '').replace('<', ''))
        for i in my_position:
            string = ''.join(re.findall(r'.>[А-я-ё]*<.\w>|.>[А-я-ё]* [А-я-ё]*<.\w>|.>[А-я-ё]* [А-я-ё]* [А-я-ё]*<.\w>', i))
            command_name.append(
                string.replace(' ','')
                .replace('</a>', '').replace('">',''))

        for i in range(len(command_name)):
            data[f'{command_name[i]}'] = command_position[i]
        return data

    def make_result(self) -> dict:
        """
        description мутирует исходный словарь с новым туром добавляет позицию команд в турнирной таблице
        :return: json_schedule
        """
        positions = self.get_position()
        print(positions)
        print(len(self.data['data']))
        for i in range(len(self.data['data'])):

            self.data['data'][i]['host_position'] = positions[''.join(self.data['data'][i]['performer'][0]['name'])
            .replace(' ','').replace('1919', '').replace('н07', 'н')
            .replace('м1846', 'м').replace('т98', 'т')]

            self.data['data'][i]['guest_position'] = positions[''.join(self.data['data'][i]['performer'][1]['name'])
            .replace(' ','').replace('1919', '').replace('н07', 'н')
            .replace('м1846', 'м').replace('т98', 'т')]
        return self.data