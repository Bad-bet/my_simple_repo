
from common.models.data_parser import DataDBReaderInterface
from common.models.main_model import Command, Game, League
from common.common import DataParser, DataUtils
from common.utils.db_aproach import DataBaseReader
from common.utils.utils import get_command_name
from common.analytics_data import DataPredictions
from common.total_predict import TotalPredict

class DataAnnounceMaker:
    def __init__(self, *, data: dict, name:str):
        self.data = data
        self.name = name

    def get_events(self, j) -> League:
        """
        description: строит по шаблону 1 событие
        :param j: принимает int для создания атомарного события
        :return: attrs модель
        """
        host_history_data = DataDBReaderInterface(
            league_name=self.name,
            command_name=get_command_name(
                command_name=self.data['data'][j]['performer'][0]['name'],
                league_name=self.name
            ),
        )
        guest_history_data = DataDBReaderInterface(
            league_name=self.name,
            command_name=get_command_name(
                command_name=self.data['data'][j]['performer'][1]['name'],
                league_name=self.name
            ),
        )

        host_history = DataBaseReader(data=host_history_data).get_host_results()
        # print('\n 1',host_history_data)
        print(get_command_name(
                command_name=self.data['data'][j]['performer'][0]['name'],
                league_name=self.name
            ))
        print('2',guest_history_data)
        guest_history = DataBaseReader(data=guest_history_data).get_guest_results()
        host_analytics_data = DataPredictions(DataDBReaderInterface(
            league_name=self.name,
            command_name=get_command_name(
                command_name=self.data['data'][j]['performer'][0]['name'],
                league_name=self.name
            ),
        )).get_host_predictions(),

        guest_analytics_data = DataPredictions(DataDBReaderInterface(
            league_name=self.name,
            command_name=get_command_name(
                command_name=self.data['data'][j]['performer'][1]['name'],
                league_name=self.name
            ),
        )).get_guest_predictions()

        next_schedule = League(
            league_name=self.name,
            game=Game(
                game=self.data['data'][j]['name'],
                date=self.data['data'][j]['startDate'],
                host_position=self.data['data'][j]['host_position'],
                guest_position=self.data['data'][j]['guest_position']
            ),
            commands=Command(
                host=self.data['data'][j]['performer'][0]['name'],
                guest=self.data['data'][j]['performer'][1]['name'],
                host_analytics_data=host_analytics_data[0],
                guest_analytics_data=guest_analytics_data,
                history_host=DataUtils(host_history).get_scores(),
                history_guest=DataUtils(guest_history).get_scores()
            )
        )
        # print(next_schedule)
        TotalPredict(next_schedule).my_predict()
        return next_schedule

    def build_nine_events(self) -> list[League]:
        """
        description: строит массив событий
        :return: массив attrs моделей
        """
        return [self.get_events(j) for j in range(9)]


    def bild_ten_events(self):
        """
        description: строит массив событий
        :return: массив attrs моделей
        """
        return [self.get_events(j) for j in range(10)]

    def build_eleven_events(self):
        """
        description: строит массив событий
        :return: массив attrs моделей
        """
        return [self.get_events(j) for j in range(11)]

    def build_twelve_events(self):
        """
        description: строит массив событий
        :return: массив attrs моделей
        """
        return [self.get_events(j) for j in range(12)]