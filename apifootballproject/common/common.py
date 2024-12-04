import html
import re

import requests

from common.models.data_parser import(
    DataInterface, DataJsonInterface,
    DataDBConductorInterface, DataDBReaderInterface
)
from common.utils.db_aproach import DataBaseConductor

from common.utils.utils import get_command_name


class DataParser:
    def __init__(self, data: DataInterface):
        self.data = data

    def get_http_data(self) -> str:
        response = requests.get(self.data.url)
        return response.text


    def tag_replacer(self):
        untag_txt = html.unescape(self.data.html_text)
        tags = re.findall(r'<[^>]+>', untag_txt)
        for tag in tags:
            untag_txt = untag_txt.replace(tag, '')
        return untag_txt


    def get_html_for_last_tour(self) -> str:
        html_body, html_data = '', ''
        bottom_html_pattern =''.join(re.findall('.{333}Бомбардиры.*', self.data.text))
        header_html_pattern =''.join(re.findall('.*<div class="block_body_nopadding">.{118}', self.data.text))
        html_blank = self.data.text.replace(bottom_html_pattern, '').replace(header_html_pattern, '')
        div_class_pattern = re.findall('<div class=".{6}">', html_blank)
        span_class_pattern = re.findall('<span class="\w*">', html_blank)
        for i in div_class_pattern:
            html_body = html_blank.replace(i, '').replace('<div class="gls">', '-').replace(' ','')
        for i in span_class_pattern:
            html_data = (html_body.replace(
                i,'').replace('<divclass="status">', '\n')
                         .replace('<divclass="img16">','\n')
                         )
        return html_data


    def make_next_tour_json(self) -> str:
        main_json = ''
        new_json = re.findall(r'{.*}', self.data.text)
        j = 0
        for i in new_json:
            if j == len(new_json) - 1:
                main_json += f'{i}'
            else:
                main_json += f'{i},'
            j += 1

        new_data = main_json.replace('@', '')
        json_data = '{"data":' + '[' + new_data + ']' + '}'
        return json_data

    def make_my_schedule(self):
        schedule = {}
        data_names = []
        # print(self.data.html_text)
        names = [
            i.replace('title=\"', '').replace('">', '').replace(' ','').replace('ДепортивоЛа-Корунья', 'ДепортивоЛаКорунья')
            for i in re.findall(r'title=\"[А-я][а-я]*.*', self.data.html_text)
        ]
        print(names)
        dates = [
            i.replace('size10">', '').replace('</span></div', '')
            for i in re.findall(r'size10\"*.*<\/div', self.data.html_text)
        ]
        for i in range(len(names)):
            data_names.append({
                'name': names[i],
                'startDate': dates[i],
                'performer': [
                    {'name': str(names[i]).split('-')[0]},
                    {'name': str(names[i]).split('-')[1]}
                ]
            })
        schedule['data'] = data_names
        return schedule

    def make_result_league(self):
        # my_data_1 = '10.11, 19:15->Салернитана0+Бари2 10.11, 17:00->ЮвеСтабия0+Специя3 10.11, 17:00->Реджана 2+Катандзаро2 10.11, 17:00->Читтаделла0+Чезена2 09.11, 19:15->Мантова1+Кремонезе0 09.11, 17:00->Модена2+Каррарезе0 09.11, 17:00->Пиза3+Сампдория0 09.11, 17:00->Зюйдтироль0+Сассуоло1 09.11, 17:00->Брешиа2+Козенца3 08.11, 22:30->Фрозиноне1+Палермо1 12-й --'
        # if self.data.html_text == 'por':
        #     drop_pattern = re.findall(r"function .*\'\+val", self.data.text)
        #     for i in drop_pattern:
        #         self.data.text = self.data.text(i, '')

        dates = [
            i.replace(' ', '') for i in re.findall(r'\d.\.\d., \d.:\d.', self.data.text)
        ]

        a, c, = '', ''
        round_pattern = re.findall(r'тур', self.data.text)
        for i in round_pattern:
            a = self.data.text.replace(i, f'--\n ')
        c = a.replace(':30', ':30->').replace(':00', ':00->').replace(':15', ':15->').replace(':45', ':45->').replace(':35', ':35->')
        host_commands = [
            i.replace('->','')[:-1] for i in re.findall(
                r'->[А-я-ё]*\d|->[А-я-ё]* [А-я-ё]*\d|->[А-я-ё]* [А-я-ё]* [А-ё]*\d', c)
        ]
        host_pattern = re.findall(r'->[А-я-ё]*\d|->[А-я-ё]* [А-я-ё]*\d|->[А-я-ё]* [А-я-ё]* [А-я-ё]*\d', c)
        for i in host_pattern:
            c = c.replace(i, f'{i}+')
        guest_commands = [
            i[2:][:-1] for i in re.findall(
                r'\d\+[А-я-ё]*\d|\d\+[А-я-ё]* [А-я-ё]*\d|\d\+[А-я-ё]* [А-я-ё]* [А-я-ё]*\d', c)
        ]
        host_league_commands = [get_command_name(league_name=self.data.html_text, command_name=i) for i in host_commands]
        guest_league_commands = [get_command_name(league_name=self.data.html_text, command_name=i) for i in guest_commands]
        """
        modify * search score
        """
        d = c
        score_pattern = re.findall(f'->[А-я]*\d|->[А-я]* [А-я]*\d|->[А-я]* [А-я]* [А-я]*\d', c)
        for i in score_pattern:
            d = d.replace(i, ' ')
        print(c)
        host_score = [
            i[:-1] for i in re.findall(r'\d\+', c)
        ]
        if self.data.html_text == 'en-b':
            guest_score = [
                i[1:] for i in re.findall(r'[А-я]\d', d)
            ][2:]
        else:
            guest_score = [
                i[1:] for i in re.findall(r'[А-я]\d', d.replace('ана 1','ана1'))
            ][2:]

        if len(dates) != len(host_score):
            for i in range(len(host_score)-len(dates)):
                dates.append('No Data')

        data_to_db = DataDBConductorInterface(
            league_idx=self.data.html_text,
            date=dates[:-1][1:],
            host_command=host_league_commands,
            guest_command=guest_league_commands,
            host_score=host_score,
            guest_score=guest_score
        )
        if len(guest_score) == 10 and len(dates) == 100 and len(guest_league_commands) == 10:
            DataBaseConductor(data_to_db).write_to_db()
        # print(data_to_db)
        print(dates[:-1][1:], len(dates))
        print(host_league_commands, len(host_league_commands))
        print(guest_league_commands, len(guest_league_commands))
        print(host_score, len(host_score))
        print(guest_score, len(guest_score))


    def make_last_tour_data(self) -> dict:
        dates = re.findall(r'\d.\.\d.,\d.:\d.', self.data.text)
        league_commands = [
            i.replace('-', '')
            for i in re.findall(r'[А-я].*-', self.data.text)
        ]
        scores = [
            i.replace('-', '') for i in re.findall(r'-\d', self.data.text)
        ]
        host_league_commands = DataUtils(league_commands).get_host_data()
        guest_league_commands = DataUtils(league_commands).get_guest_data()
        host_score = DataUtils(scores).get_host_data()
        guest_score = DataUtils(scores).get_guest_data()
        data = DataDBConductorInterface(
            league_idx=self.data.html_text,
            date=dates,
            host_command=host_league_commands,
            guest_command=guest_league_commands,
            host_score=host_score,
            guest_score=guest_score
        )
        if len(dates) != len(host_score):
            for i in range(len(host_score)-len(dates)):
                dates.append('No Data')
        DataBaseConductor(data).write_to_db()


class DataUtils:
    def __init__(self, data: list[str]):
        self.data = data

    def get_host_data(self) -> list[str]:
        host_commands = []
        for i in range(len(self.data)):
            if i % 2 == 0 and self.data[i] != 'Бомбардиры':
                host_commands.append(self.data[i])
        return host_commands

    def get_guest_data(self) -> list[str]:
        guest_commands = []
        for i in range(len(self.data)):
            if not i % 2 == 0 and self.data[i] != 'Бомбардиры':
                guest_commands.append(self.data[i])
        return guest_commands

    def get_scores(self):
        scores = []
        for i in range(len(self.data)):
            dict_part = {'score': self.data[i][0], 'un_score': self.data[i][1]}
            scores.append(dict_part)
        return scores
