from common.models.data_parser import DataDBReaderInterface
from common.utils.db_aproach import DataBaseReader


class DataPredictions:
    def __init__(self, data: DataDBReaderInterface):
        self.data = data

    def get_host_predictions(self) -> dict:
        new_data = {}
        host_total_games_score = 0
        host_total_game_lost = 0
        host_guest_total_score = 0
        host_guest_total_lost = 0


        host_history_data = DataDBReaderInterface(
            league_name=self.data.league_name,
            command_name=self.data.command_name
        )
        guest_history_data = DataDBReaderInterface(
            league_name=self.data.league_name,
            command_name=self.data.command_name
        )
        host_history = DataBaseReader(data=host_history_data).get_host_results()
        guest_history = DataBaseReader(data=guest_history_data).get_guest_results()

        for i in range(len(host_history)):
            host_total_games_score += host_history[i][0]
            host_total_game_lost += host_history[i][1]

        for i in range(len(guest_history)):
            host_guest_total_score += guest_history[i][1]
            host_guest_total_lost += guest_history[i][0]

        new_data['host_total_games_score'] = host_total_games_score/len(host_history)
        new_data['host_total_game_lost'] = host_total_game_lost/len(host_history)
        new_data['host_guest_total_score'] = host_guest_total_score/len(guest_history)
        new_data['host_guest_total_lost'] = host_guest_total_lost/len(guest_history)
        new_data['host_total_efficiency'] = host_total_games_score/host_total_game_lost
        new_data['host_total_all_efficiency'] = (host_total_games_score + host_guest_total_score)/(host_total_game_lost + host_guest_total_lost)

        if new_data['host_total_games_score'] > 1 and new_data['host_total_games_score'] > 1.502 and new_data['host_total_games_score'] >= 2:
            new_data['should_score_1'] = True
            new_data['should_score_1.5'] = True
            new_data['should_score_2'] = True
            new_data['prediction_score'] = 'total - 1.5 +'
        elif 1.12 < new_data['host_total_games_score'] > 1.52:
            new_data['should_score_1'] = True
            new_data['should_score_1.5'] = True
            new_data['should_score_2'] = False
            new_data['prediction_score'] = 'total - 1.5 -'
        elif 1.12 < new_data['host_total_games_score'] > 1.38:
            new_data['should_score_1'] = True
            new_data['should_score_1.5'] = False
            new_data['should_score_2'] = False
            new_data['prediction_score'] = 'score - 1'
        else:
            new_data['should_score_1'] = False
            new_data['should_score_1.5'] = False
            new_data['should_score_2'] = False
            new_data['prediction_score'] = 'not_score'

        if new_data['host_total_game_lost'] > 1.2 and new_data['host_total_game_lost'] > 1.5:
            new_data['should_lost_1'] = True
            new_data['should_lost_1.5'] = True
            new_data['prediction_lost'] = 'lost 1.5 +'
        elif 1 <= new_data['host_total_game_lost'] < 1.5:
            new_data['should_lost_1'] = True
            new_data['should_lost_1.5'] = False
            new_data['prediction_lost'] = 'lost 1'
        else:
            new_data['should_lost_1'] = False
            new_data['should_lost_1.5'] = False
            new_data['prediction_lost'] = 'not lost'

        analytic_data = {'host_data': new_data}
        return analytic_data

#___________________________________________________________
    def get_guest_predictions(self) -> dict:
        new_data = {}
        guest_total_score = 0
        guest_total_lost = 0
        guest_total_host_score = 0
        guest_total_host_lost = 0


        host_history_data = DataDBReaderInterface(
            league_name=self.data.league_name,
            command_name=self.data.command_name
        )
        guest_history_data = DataDBReaderInterface(
            league_name=self.data.league_name,
            command_name=self.data.command_name
        )
        host_history = DataBaseReader(data=host_history_data).get_host_results()
        guest_history = DataBaseReader(data=guest_history_data).get_guest_results()

        for i in range(len(host_history)):
            guest_total_host_score += host_history[i][0]
            guest_total_host_lost += host_history[i][1]

        for i in range(len(guest_history)):
            guest_total_score += guest_history[i][1]
            guest_total_lost += guest_history[i][0]


        new_data['guest_total_score'] = guest_total_score/len(host_history)
        new_data['guest_total_lost'] = guest_total_lost/len(host_history)
        new_data['guest_total_host_score'] = guest_total_host_score/len(guest_history)
        new_data['guest_total_host_lost'] = guest_total_host_lost/len(guest_history)
        new_data['guest_total_efficiency'] = guest_total_score/guest_total_lost
        new_data['guest_total_all_efficiency'] = (guest_total_score + guest_total_host_score)/(guest_total_host_lost + guest_total_host_lost)

        if new_data['guest_total_score'] > 1 and new_data['guest_total_score'] > 1.5 and new_data['guest_total_score'] >= 2:
            new_data['should_score_1'] = True
            new_data['should_score_1.5'] = True
            new_data['should_score_2'] = True
            new_data['prediction_score'] = 'total - 1.5 +'
        elif 1.12 < new_data['guest_total_score'] > 1.52:
            new_data['should_score_1'] = True
            new_data['should_score_1.5'] = True
            new_data['should_score_2'] = False
            new_data['prediction_score'] = 'total - 1.5 -'
        elif 1.12 < new_data['guest_total_score'] > 1.38:
            new_data['should_score_1'] = True
            new_data['should_score_1.5'] = False
            new_data['should_score_2'] = False
            new_data['prediction_score'] = 'score - 1'
        else:
            new_data['should_score_1'] = False
            new_data['should_score_1.5'] = False
            new_data['should_score_2'] = False
            new_data['prediction_score'] = 'not_score'

        if new_data['guest_total_lost'] > 1.2 and new_data['guest_total_lost'] > 1.5:
            new_data['should_lost_1'] = True
            new_data['should_lost_1.5'] = True
            new_data['prediction_lost'] = 'lost 1.5 +'
        elif 1 <= new_data['guest_total_lost'] < 1.5:
            new_data['should_lost_1'] = True
            new_data['should_lost_1.5'] = False
            new_data['prediction_lost'] = 'lost 1'
        else:
            new_data['should_lost_1'] = False
            new_data['should_lost_1.5'] = False

        analytic_data = {'guest_data': new_data}
        return analytic_data
