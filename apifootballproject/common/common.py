import html
import re
import requests
import json
from common.models.data_parser import DataInterface, DataJsonInterface


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
                         .replace('<divclass="img16">','\n'))
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


    def make_last_tour_data(self) -> str:
        new_data = ''
        dates = re.findall(r'\d.\.\d.,\d.:\d.', self.data.text)
        league_commands = [
            i.replace('-', '') for i in re.findall(r'[А-я].*-', self.data.text)
        ]
        scores = [
            i.replace('-', '') for i in re.findall(r'-\d', self.data.text)
        ]
        host_league_commands = DataUtils(league_commands).get_host_data()
        guest_league_commands = DataUtils(league_commands).get_guest_data()
        host_score = DataUtils(scores).get_host_data()
        guest_score = DataUtils(scores).get_guest_data()
        if len(dates) != len(host_score):
            for i in range(len(host_score)-len(dates)):
                dates.append('No Data')
        j = 0
        for i in range(len(host_score)):
            if j == len(host_score) - 1:
                new_data += ('{"game": "'+dates[i]+'", "host_command": "'+host_league_commands[i]+'", "host_score": '+host_score[i]+', "guest_command": "'+guest_league_commands[i]+', "guest_score": '+guest_score[i]+'"}')
            else:
                new_data += ('{"game": "'+dates[i]+'", "host_command": "'+host_league_commands[i]+'", "host_score": '+host_score[i]+', "guest_command": "'+guest_league_commands[i]+', "guest_score": '+guest_score[i]+'"},')
            j += 1

        json_data = '{"data":' + '[' + new_data + ']' + '}'
        return json_data


class JsonConductor:
    def __init__(self, data: DataJsonInterface):
        self.data = data

    def json_record(self):
        with open(self.data.write_json_data, 'w', encoding='utf8') as f:
            f.write(self.data.json_next_tour_name)

    def get_from_json(self) -> dict:
        with open(self.data.json_next_tour_name, 'r') as f:
            json_schedule = json.load(f)
            return json_schedule


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