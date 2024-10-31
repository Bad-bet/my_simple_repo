from common.models.data_parser import DataDBConductorInterface
from common.utils.db_aproach import DataBaseConductor



# data = DataDBConductorInterface(
#     league_idx='ita',
#     date=['25.10,20:30', '25.10,22:45', '26.10,17:00', '26.10,19:00', '26.10,22:45', '27.10,14:30', '27.10,17:00', '27.10,17:00', '27.10,20:00', '27.10,22:45'],
#     host_command=['Удинезе', 'Торино', 'Наполи', 'Болонья', 'Аталанта', 'Парма', 'Лацио', 'Монца', 'Интер', 'Фиорентина'],
#     guest_command=['Кальяри', 'Комо', 'Лечче', 'Милан', 'Верона', 'Эмполи', 'Дженоа', 'Венеция', 'Ювентус', 'Рома'],
#     host_score=[2, 1, 1, 1, 6, 1, 3, 2, 4, 5],
#     guest_score=[0, 0, 0, 2, 1, 1, 0, 2, 4, 1]
# )
#
# DataBaseConductor(data).write_to_db()

a = [(4, 3), (2, 3), (2, 2), (2, 1)]
b = []

print(range(len(a)))

for i in  range(len(a)):
    dict_part = {'score':a[i][0], 'un_score':a[i][1]}
    print(type(dict_part))

