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

def england_league_b(command_name: str) -> str:
    if command_name == 'ПрестонНортЭнд':
        return 'Престон'
    elif command_name == 'ШеффилдЮнайтед':
        return 'ШеффилдЮтд'
    elif command_name == 'ОксфордЮнайтед':
        return 'ОксфордЮ'
    elif command_name == 'КуинзПаркРейнджерс':
        return 'КПР'
    elif command_name == 'ЛидсЮнайтед':
        return 'Лидс'
    return command_name.replace('-', '').replace(' ','')

def italy_b_league(command_name: str) -> str:
    if command_name =='Реджана1919':
        return 'Реджана'
    my_command = command_name.replace('-', '').replace(' ','')
    return my_command

def germany_b_league(command_name: str) -> str:
    if command_name == 'Ульм1846':
        return 'Ульм'
    elif command_name == 'Дармштадт98':
        return 'Дармштадт'
    elif command_name == 'Кёльн':
        return 'Кельн'
    elif command_name == 'Падерборн07':
        return  'Падерборн'
    my_command = command_name.replace('-', '').replace(' ', '')
    return my_command

def portugal_league(command_name: str) -> str:
    if command_name == 'Эшторил-Прая':
        return 'Эшторил'
    return command_name.replace('-', '').replace(' ','')

def italy_league(command_name: str) -> str:
    return command_name.replace('-', '').replace(' ','')

def spain_league(command_name: str) -> str:
    return command_name.replace('-', '').replace(' ','')

def spain_b_league(command_name: str) -> str:
    return command_name.replace('-', '').replace(' ','')

def get_command_name(*, command_name: str, league_name: str) -> str:
    """
    мапит название комманд для лиг используя адаптеры для лиг
    :param command_name: название атомарной команды которая будет смаплена согласно данным в БД
    :param league_name: название лиги
    :return: атомарное название команды с устранением пробелов и -
    """
    if league_name == 'en':
        return england_league(command_name)
    elif league_name == 'ger':
        return germany_league(command_name)
    elif league_name == 'es':
        return spain_league(command_name)
    elif league_name == 'ita-b':
        return italy_b_league(command_name)
    elif league_name == 'ger-b':
        return germany_b_league(command_name)
    elif league_name == 'en-b':
        print(command_name)
        return england_league_b(command_name)
    elif league_name == 'por':
        return portugal_league(command_name)
    elif league_name == 'es-b':
        return spain_b_league(command_name)
    else:
        return italy_league(command_name)


def ready_announce_10(league_data: list[League]) -> dict:
    """
    description: строит словарь моделей анонса тура для i встреч
    :param league_data: принимает массив моделей
    :return: словарь анонсов
    """
    if len(league_data) == 10:
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
    else:
        print('len----- ',len(league_data))
        raise 'ConditionError'
    return data

def ready_announce_9(league_data: list[League]) -> dict:
    """
    description: строит словарь моделей анонса тура для i встреч
    :param league_data: принимает массив моделей
    :return: словарь анонсов
    """
    if len(league_data) == 9:
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
    else:
        print('len- ',len(league_data))
        raise f'ConditionError'
    return data

def ready_announce_12(league_data: list[League]) -> dict:
    """
    description: строит словарь моделей анонса тура для i встреч
    :param league_data: принимает массив моделей
    :return: словарь анонсов
    """
    if len(league_data) == 12:
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
                attrs.asdict(league_data[9]),
                attrs.asdict(league_data[10]),
                attrs.asdict(league_data[11]),
            ]
        }
    else:
        print('len- ',len(league_data))
        raise f'ConditionError'
    return data

def ready_announce_11(league_data: list[League]) -> dict:
    """
    description: строит словарь моделей анонса тура для i встреч
    :param league_data: принимает массив моделей
    :return: словарь анонсов
    """
    if len(league_data) == 11:
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
                attrs.asdict(league_data[9]),
                attrs.asdict(league_data[10]),
            ]
        }
    else:
        print('len- ',len(league_data))
        raise f'ConditionError'
    return data