
from common.models.data_parser import DataDBReaderInterface
from common.models.main_model import Command, Game, League
from common.common import DataParser, DataUtils
from common.utils.db_aproach import DataBaseReader
from common.utils.utils import get_command_name

class DataAnnounceMaker:
    def __init__(self, *, data: dict, name:str):
        self.data = data
        self.name = name

    def get_events(self, j) -> League:
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
        guest_history = DataBaseReader(data=guest_history_data).get_guest_results()

        next_schedule = League(
            league_name=self.name,
            game=Game(
                game=self.data['data'][j]['name'],
                date=self.data['data'][j]['startDate']
            ),
            commands=Command(
                host=self.data['data'][j]['performer'][0]['name'],
                guest=self.data['data'][j]['performer'][1]['name'],
                history_host=DataUtils(host_history).get_scores(),
                history_guest=DataUtils(guest_history).get_scores()
            )
        )
        return next_schedule

    def build_nine_events(self) -> list[League]:
        """
        make results data schedule list for 9 events
        """
        return [self.get_events(j) for j in range(9)]


    def bild_ten_events(self):
        """
        make results data schedule list for 10 events
        """
        return [self.get_events(j) for j in range(10)]