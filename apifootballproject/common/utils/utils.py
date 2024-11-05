import json

import attrs
from common.models.data_parser import DataJsonInterface
from common.models.main_model import League


class JsonConductor:
    def __init__(self, data: DataJsonInterface):
        self.data = data

    def json_record(self) -> None:
        # print(self.data.json_next_tour_name)
        with open(self.data.json_next_tour_name, 'w+', encoding='utf8') as f:
            f.write(self.data.write_json_data)

    def json_update_record(self) -> None:
        # print(self.data.json_next_tour_name)
        with open(self.data.json_next_tour_name, 'a') as f:
            f.write(self.data.write_json_data)

    def get_from_json(self) -> dict:
        with open(self.data.json_next_tour_name, 'r') as f:
            json_data = json.load(f)
            return json_data


def germany_league(command_name: str) -> str:
    if command_name == 'Боруссия Мёнхенгладбах':
        return 'БоруссияМ'
    elif command_name == 'Унион Берлин':
        return 'УнионБерлин'
    my_command = command_name.replace('-', '').replace(' ','')
    return my_command

def england_league(command_name: str) -> str:
    if command_name == 'Манчестер Сити':
        return 'МанСити'
    elif command_name == 'Манчестер Юнайтед':
        return 'МанЮнайтед'

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


def ready_announce_10(league_data: list[League]) -> dict:
    data = {
        'data':[
            attrs.asdict(league_data[0]),
            attrs.asdict(league_data[1]),
            attrs.asdict(league_data[2]),
            attrs.asdict(league_data[3]),
            attrs.asdict(league_data[4]),
            attrs.asdict(league_data[5]),
            attrs.asdict(league_data[6]),
            attrs.asdict(league_data[7]),
            attrs.asdict(league_data[8]),
            attrs.asdict(league_data[9]),
        ]
    }
    return data

def ready_announce_9(league_data: list[League]) -> dict:
    data = {
        'data':[
            attrs.asdict(league_data[0]),
            attrs.asdict(league_data[1]),
            attrs.asdict(league_data[2]),
            attrs.asdict(league_data[3]),
            attrs.asdict(league_data[4]),
            attrs.asdict(league_data[5]),
            attrs.asdict(league_data[6]),
            attrs.asdict(league_data[7]),
            attrs.asdict(league_data[8]),
        ]
    }
    return data