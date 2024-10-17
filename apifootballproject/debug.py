from common.common import DataBaseReader
from common.models.data_parser import DataDBReaderInterface

data = DataDBReaderInterface(
    league_name='es',
    command_name='Валенсия',
)

DataBaseReader(data=data).get_guest_results()
DataBaseReader(data=data).get_host_results()
#
