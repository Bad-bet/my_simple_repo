import json
from common.models.data_parser import DataJsonInterface


class JsonConductor:
    def __init__(self, data: DataJsonInterface):
        self.data = data

    def json_record(self) -> None:
        # print(self.data.json_next_tour_name)
        with open(self.data.json_next_tour_name, 'w+', encoding='utf8') as f:
            f.write(self.data.write_json_data)

    def get_from_json(self) -> dict:
        with open(self.data.json_next_tour_name, 'r') as f:
            json_data = json.load(f)
            return json_data


def germany_league(command_name: str) -> str:
    if command_name == 'Боруссия Мёнхенгладбах':
        return 'БоруссияМ'
    my_command = command_name.replace('-', '').replace(' ','')
    return my_command

def england_league(command_name: str) -> str:
    if command_name == 'Манчестер Сити':
        return 'МанСити'
    my_command = command_name.replace('-', '').replace(' ','')
    return my_command

def italy_league(command_name: str) -> str:
    return command_name.replace('-', '').replace(' ','')

def spain_league(command_name: str) -> str:
    return command_name.replace('-', '').replace(' ','')

def get_command_name(*, command_name: str, league_name: str) -> str:
    if league_name == 'en':
        return england_league(command_name)
    elif league_name == 'ger':
        return germany_league(command_name)
    elif league_name == 'es':
        return spain_league(command_name)
    else:
        return italy_league(command_name)