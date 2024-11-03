from common.models.data_parser import DataDBConductorInterface
from common.utils.db_aproach import DataBaseConductor
from common.models.data_parser import DataDBReaderInterface
from common.analytics_data import DataPredictions



# data = DataDBConductorInterface(
#     league_idx='ita',
#     date=['25.10,20:30', '25.10,22:45', '26.10,17:00', '26.10,19:00', '26.10,22:45', '27.10,14:30', '27.10,17:00', '27.10,17:00', '27.10,20:00', '27.10,22:45'],
#     host_command=['Удинезе', 'Торино', 'Наполи', 'Болонья', 'Аталанта', 'Парма', 'Лацио', 'Монца', 'Интер', 'Фиорентина'],
#     guest_command=['Кальяри', 'Комо', 'Лечче', 'Милан', 'Верона', 'Эмполи', 'Дженоа', 'Венеция', 'Ювентус', 'Рома'],
#     host_score=[2, 1, 1, 1, 6, 1, 3, 2, 4, 5],
#     guest_score=[0, 0, 0, 2, 1, 1, 0, 2, 4, 1]
# )
#

command_host = DataDBReaderInterface(
    league_name='es',
    command_name='Севилья'
)

command_guest = DataDBReaderInterface(
    league_name='es',
    command_name='РеалСосьедад'
)


print(DataPredictions(command_host).get_host_predictions())
print('\n',DataPredictions(command_guest).get_guest_predictions())
