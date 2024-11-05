import sqlite3
from common.models.data_parser import(
    DataDBConductorInterface, DataDBReaderInterface
)



class DataBaseReader:
    def __init__(self, data: DataDBReaderInterface):
        self.data = data

    def get_host_results(self):
        get_data = []
        connect = sqlite3.connect('./common/data_base/football_stats.db')
        cursor = connect.cursor()
        if self.data.league_name == 'en':
            cursor.execute(
                f'SELECT score, un_score FROM England_League WHERE command="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()

        elif self.data.league_name == 'es':
            cursor.execute(
                f'SELECT score, un_score FROM Spain_League WHERE command="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()

        elif self.data.league_name == 'ger':
            cursor.execute(
                f'SELECT score, un_score FROM Germany_League WHERE command="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()

        elif self.data.league_name == 'ita':
            cursor.execute(
                f'SELECT score, un_score FROM Italy_League WHERE command="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()
        cursor.close()
        return get_data

    def get_guest_results(self):
        connect = sqlite3.connect('./common/data_base/football_stats.db')
        cursor = connect.cursor()
        if self.data.league_name == 'en':
            cursor.execute(
                f'SELECT score, un_score FROM England_League WHERE command_guest="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()

        elif self.data.league_name == 'es':
            cursor.execute(
                f'SELECT score, un_score FROM Spain_League WHERE command_guest="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()

        elif self.data.league_name == 'ger':
            cursor.execute(
                f'SELECT score, un_score FROM Germany_League WHERE command_guest="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()

        elif self.data.league_name == 'ita':
            cursor.execute(
                f'SELECT score, un_score FROM Italy_League WHERE command_guest="{self.data.command_name}" GROUP by ROWID'
            )
            get_data = cursor.fetchall()
        cursor.close()
        return get_data


class DataBaseConductor:
    def __init__(self, data: DataDBConductorInterface):
        self.data = data

    """
    INSERT INTO Commands (league_id, command_id, command_name) VALUES(1, 'Ньюкасл')
    INSERT INTO History (command_id, date_game, score, un_score) VALUES(1, '28.09,14:30', 1, 1)
    SELECT Commands.command_name, History.date_game, History.score, History.un_score FROM Commands
    JOIN History ON Commands.command_id = History.command_id

    SELECT League.league_name, Commands.command_name, History.date_game, History.score, History.un_score FROM Commands
    JOIN History ON Commands.command_name = 'МанСити' AND History.command_id = 2
    JOIN League ON League.league_name='England_League'
    England_League, Spain_league, Germany_league, Italy_league
    """

    def write_to_db(self):
        print(self.data)
        connect = sqlite3.connect('./common/data_base/football_stats.db')
        cursor = connect.cursor()
        for i in range(len(self.data.date)):
            if self.data.league_idx == 'en':
                cursor.execute(
                    f'INSERT INTO England_League (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
            elif self.data.league_idx == 'es':
                cursor.execute(
                    f'INSERT INTO Spain_League (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
            elif self.data.league_idx == 'ger':
                cursor.execute(
                    f'INSERT INTO Germany_League (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
            elif self.data.league_idx == 'ita':
                cursor.execute(
                    f'INSERT INTO Italy_League (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
            elif self.data.league_idx == 'ita-b':
                cursor.execute(
                    f'INSERT INTO Italy_League_B (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
            elif self.data.league_idx == 'en-b':
                cursor.execute(
                    f'INSERT INTO En_Championship (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
            elif self.data.league_idx == 'es-b':
                cursor.execute(
                    f'INSERT INTO Spain_Segundo (command, date_game, score, un_score, command_guest) VALUES('
                    f'"{self.data.host_command[i]}", "{self.data.date[i]}", {self.data.host_score[i]},'
                    f'{self.data.guest_score[i]}, "{self.data.guest_command[i]}")'
                )
        connect.commit()
        cursor.close()
