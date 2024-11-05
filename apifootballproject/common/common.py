import html
import re

import requests

from common.models.data_parser import(
    DataInterface, DataJsonInterface,
    DataDBConductorInterface, DataDBReaderInterface
)
from common.utils.db_aproach import DataBaseConductor

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


    def make_result_league(self):
        # my_data = '18.08,22:30->Реджана+2=Мантова- 2 18.08,22:30->Фрозиноне+2=Сампдория- 2 18.08,22:30->Козенца+1=Кремонезе- 0 18.08,22:30->Чезена+2=Каррарезе- 1 18.08,22:30->Катандзаро+1=Сассуоло- 1 17.08,22:30->Бари+1=ЮвеСтабия- 3 17.08,22:30->Зюйдтироль+2=Модена- 1 17.08,22:30->Салернитана+2=Читтаделла- 1 17.08,22:30->Пиза+2=Специя- 2 16.08,22:30->Брешиа+1=Палермо- 0 '
        my_data_1 = '28.10, 22:30->++++РасингФерроль+1=Тенерифе1 27.10, 23:00->++++Гранада+++++++1============Леванте2 27.10, 20:30->++++Альбасете++++++3=========СпортингХихон3 27.10, 20:30->++++Уэска++++++2=========Альмерия2 27.10, 18:15->++++Депортиво+1=Расинг2 27.10, 18:15->++++Эльче+++++++1============Бургос0 27.10, 16:00->++++Малага++++++1============Эйбар0 26.10, 20:30->++++Кордоба++++++2=========Эльденсе0 26.10, 20:30->++++Сарагоса++++++1============Кастельон2 26.10, 18:15->++++Кадис+++++++2=========РеалОвьедо0 26.10, 18:15->++++Мирандес+++++++3=========Картахена1 11-й --'
        ab = my_data_1[:-6]
        dc = ab.replace(8*'=', '').replace(', ',',').replace(2*'=', '=').replace(3*'=','=').replace('->++++','->')
        my_data = dc.replace(6*'+', '+').replace(2*'=','=').replace(4*'+', '+').replace(2*'+', '+')
        my_pattern = re.findall(r'=[А-я]*', my_data)
        for i in my_pattern:
            my_data = my_data.replace(i, f'{i}- ')
        print(my_data)
        dates = re.findall(r'\d.\.\d.,\d.:\d.', my_data)
        host_league_commands = [
            i.replace('>','') for i in re.findall(r'>[А-я]*', my_data)
        ]
        guest_league_commands = [
            i.replace('=', '') for i in re.findall(r'=[А-я]*', my_data)
        ]
        host_score = [
            i.replace('+', '') for i in re.findall(r'\+\d', my_data)
        ]
        guest_score = [
            i.replace('- ', '') for i in re.findall(r'- \d', my_data)
        ]
        # a, c = '', ''
        # round_pattern = re.findall(r'тур', self.data.text)
        # for i in round_pattern:
        #     a = self.data.text.replace(i, f'--\n ')
        # c = a.replace(':30', ':30->').replace(':00', ':00->').replace(':15', ':15->').replace(' 1919', '')
        # host_pattern = re.findall(f'->[А-я]*', c)
        # for i in host_pattern:
        #     c = c.replace(i, f'{i}+')
        # host_score = re.findall(r'\+\d', c)
        # for i in host_score:
        #     c = c.replace(i,f'{i}=')
        # c = c.replace('==============', '')
        # with open('seriaB.txt', 'w') as f:
        #     f.write(c)

        data_to_db = DataDBConductorInterface(
            league_idx='es-b',
            date=dates,
            host_command=host_league_commands,
            guest_command=guest_league_commands,
            host_score=host_score,
            guest_score=guest_score
        )
        DataBaseConductor(data_to_db).write_to_db()
        print(dates, len(dates))
        print(host_league_commands, len(host_league_commands))
        print(guest_league_commands, len(guest_league_commands))
        print(host_score, len(host_score))
        print(guest_score, len(guest_score))


    def make_last_tour_data(self) -> dict:
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
        data = DataDBConductorInterface(
            league_idx=self.data.html_text,
            date=dates,
            host_command=host_league_commands,
            guest_command=guest_league_commands,
            host_score=host_score,
            guest_score=guest_score
        )
        print(data)
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
