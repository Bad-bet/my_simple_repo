from common.models.data_parser import DataDBConductorInterface
from common.utils.db_aproach import DataBaseConductor
from common.models.data_parser import DataDBReaderInterface
from common.analytics_data import DataPredictions



# data = DataDBConductorInterface(
#     league_idx='es',
#     date=['01.11,23:00', '02.11,16:00', '02.11,18:15', '03.11,16:00', '03.11,18:15', '03.11,20:30', '03.11,23:00', '04.11,23:00'],
#     host_command=['Алавес', 'Осасуна', 'Жирона', 'АтлетикоМадрид', 'Барселона', 'Севилья', 'Атлетик', 'Сельта'],
#     guest_command=['Мальорка', 'РеалВальядолид', 'Леганес3', 'ЛасПальмас', 'Эспаньол', 'РеалСосьедад', 'Бетис', 'Хетафе'],
#     host_score=['1', '1', '4', '2', '3', '0', '1', '1'],
#     guest_score=['0', '0', '3', '0', '1', '2', '1', '0']
# )
# DataBaseConductor(data).write_to_db()
#


command_host = DataDBReaderInterface(
    league_name='es',
    command_name='Сельта'
)

command_guest = DataDBReaderInterface(
    league_name='es',
    command_name='Хетафе'
)


print(DataPredictions(command_host).get_host_predictions())
print('\n',DataPredictions(command_guest).get_guest_predictions())
