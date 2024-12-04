from common.models.main_model import Command, Game, League
from duplicity.commandline import commands


class TotalPredict:
    """
    decription: принимает модель с данными где сравнивает значения для аналитики
    """
    def __init__(self, data: League):
        self.data = data
        self.host_position = data.game.host_position
        self.guest_position = data.game.guest_position
        self.game_data = data.game.game
        self.host_score = data.commands.host_analytics_data['host_data']['host_total_games_score']
        self.host_lost = data.commands.host_analytics_data['host_data']['host_total_game_lost']
        self.host_efficiency = data.commands.host_analytics_data['host_data']['host_total_efficiency']
        self.host_total_efficiency = data.commands.host_analytics_data['host_data']['host_total_efficiency']
        self.should_score_1 = data.commands.host_analytics_data['host_data']['should_score_1']
        self.should_score_1_5 = data.commands.host_analytics_data['host_data']['should_score_1.5']
        self.should_score_2 = data.commands.host_analytics_data['host_data']['should_score_2']
        self.should_lost_1 = data.commands.host_analytics_data['host_data']['should_lost_1']
        self.should_lost_1_5 = data.commands.host_analytics_data['host_data']['should_lost_1.5']
        self.guest_score = data.commands.guest_analytics_data['guest_data']['guest_total_score']
        self.guest_lost = data.commands.guest_analytics_data['guest_data']['guest_total_lost']
        self.guest_efficiency = data.commands.guest_analytics_data['guest_data']['guest_total_efficiency']
        self.guest_total_efficiency = data.commands.guest_analytics_data['guest_data']['guest_total_all_efficiency']
        self.should_guest_score_1 = data.commands.guest_analytics_data['guest_data']['should_score_1']
        self.should_guest_score_1_5 = data.commands.guest_analytics_data['guest_data']['should_score_1.5']
        self.should_guest_score_2 = data.commands.guest_analytics_data['guest_data']['should_score_2']
        self.should_guest_lost_1 = data.commands.guest_analytics_data['guest_data']['should_lost_1']
        self.should_guest_lost_1_5 = data.commands.guest_analytics_data['guest_data']['should_lost_1.5']


    def score_one(self) -> dict:
        """
        descripttion: проверяет может ли гол
        :return: словарь
        """
        one_data = {}
        if (
                int(self.host_position) < int(self.guest_position)
                and abs(int(self.host_position) - int(self.guest_position)) <= 7
                and self.host_score > 1.39
                and self.guest_lost >= 0.82
        ):
            one_data['host_score_one'] = True

        elif (
                int(self.host_position) < int(self.guest_position)
                and abs(int(self.host_position) - int(self.guest_position)) >= 8
                and self.host_score > 1.11
                and self.guest_lost >= 0.73
        ):
            one_data['host_score_one'] = True

        elif (
                int(self.host_position) > int(self.guest_position)
                and abs(int(self.host_position) - int(self.guest_position)) <= 7
                and self.host_score > 1.25
                and self.guest_lost >= 1.04
        ):
            one_data['host_score_one'] = True

        elif (
              int(self.guest_position) < int(self.host_position)
              and (abs(int(self.guest_position) - int(self.host_position))) <= 5
              and self.guest_score >= 1.33
              and self.guest_efficiency >= 1
              and self.host_lost >= 0.96
        ):
            one_data['guest_score_one'] = True

        elif (
                int(self.guest_position) < int(self.host_position)
                and (abs(int(self.guest_position) - int(self.host_position))) >= 6
                and self.guest_score >= 1.21
                and self.host_lost >= 0.74
        ):
            one_data['guest_score_one'] = True

        else:
            one_data['host_score_one'] = 'not-recommended'
        return one_data

    def score_two(self) -> dict:
        """
        descripttion: проверяет может ли быть 1,5
        :return: словарь
        """
        two_data = {}
        if (int(self.host_position) < int(self.guest_position)
                 and abs(int(self.host_position) - int(self.guest_position)) >= 7
                 and self.host_score >= 1.73
                 and self.host_efficiency >= 1.109
                 and self.host_total_efficiency >= 1.1
                 and self.guest_lost >= 1
        ):
            two_data['host_score_2'] = True

        elif (int(self.host_position) < int(self.guest_position)
            and abs(int(self.host_position) - int(self.guest_position)) <= 6
            and self.host_score >= 1.91
            and self.host_efficiency >= 1.48
            and self.guest_lost >= 1.6
        ):
            two_data['host_score_2'] = True

        elif (int(self.guest_position) < int(self.host_position) and
              (abs(int(self.guest_position) - int(self.host_position))) >= 8
              and self.guest_score >= 1.86
              and self.guest_efficiency >= 1.45
              and self.guest_total_efficiency >= 1.1
              and self.host_lost >= 1.39
        ):
            two_data['guest_score_2'] = True

        elif (int(self.host_position) < int(self.guest_position)
                 and abs(int(self.host_position) - int(self.guest_position)) >= 6
                 and self.host_score >= 1.78
                 and self.host_efficiency >= 1.25
                 and self.host_total_efficiency >= 1
                 and self.guest_lost >= 1
        ):
            two_data['host_score_2_risk'] = True


        elif (int(self.guest_position) < int(self.host_position) and
              (abs(int(self.guest_position) - int(self.host_position))) >= 8
              and self.guest_score >= 1.56
              and self.guest_efficiency >= 1.45
              and self.guest_total_efficiency >= 1.1
              and self.host_lost >= 1.39
        ):
            two_data['guest_score_2_risk'] = True
        else:
            two_data['host_score_2'] = 'not-recommended'

        return two_data

    def lower_one_five_risk(self):
        """
        descripttion: проверяет может ли быть мньше 1,5 риск
        :return: словарь
        """
        lower_one_five_data = {}
        if (8 <= abs(int(self.host_position) - int(self.guest_position))
                and int(self.host_position) > int(self.guest_position)
                and self.host_score <= 1.12
        ):
            lower_one_five_data['host_lower_two_risk'] = True

        elif self.host_score < 0.63 and self.host_lost > 0.7:
            lower_one_five_data['host_lower_two_risk'] = True

        elif (8 <= abs(int(self.guest_position) - int(self.host_position))
         and int(self.guest_position) > int(self.host_position)
         and self.guest_score <= 1.12
         ):
            lower_one_five_data['guest_lower_two_risk'] = True

        elif self.guest_score < 0.63 and self.guest_lost > 0.7:
            lower_one_five_data['guest_lower_two_risk'] = True
        else:
            lower_one_five_data['host_lower_two_risk'] = 'not-recommended'
        return lower_one_five_data

    def both_score(self):
        """
        descripttion: проверяет могут обе забить
        :return: словарь
        """
        both_data = {}
        if (4 >= abs(int(self.host_position) - int(self.guest_position))
                and self.host_score > 1.46
                and self.host_lost > 1.1
                and self.host_efficiency > 1.4
                and self.guest_score > 1.53
                and self.guest_lost > 0.78
                and self.guest_efficiency > 1.45
        ):
            both_data['both_score_strong'] = True
        elif (4 <= abs(int(self.host_position) - int(self.guest_position)) <= 8
                and self.host_score > 1.46
                and self.host_lost > 1.32
                and self.guest_score > 1.53
                and self.guest_lost > 1.18
        ):
            both_data['both_score_strong'] = True

        elif (6 <= abs(int(self.host_position) - int(self.guest_position)) <= 13
                and int(self.host_position) > int(self.guest_position)
                and self.host_score > 1.22
                and self.host_lost > 1.03
                and self.guest_score > 1.09
                and self.guest_lost > 1.33
        ):
            both_data['both_score_risk'] = True

        elif (5 >= abs(int(self.host_position) - int(self.guest_position))
                and int(self.host_position) > int(self.guest_position)
                and self.host_score > 1.27
                and self.host_lost > 1.28
                and self.guest_score > 1.15
                and self.guest_lost > 1.24
        ):
            both_data['both_score_risk'] = True

        elif (5 >= abs(int(self.host_position) - int(self.guest_position))
                and int(self.host_position) > int(self.guest_position)
                and self.host_score > 2.01
                and self.host_lost > 1.28
                and self.guest_score > 1.25
                and self.guest_lost > 0.48
        ):
            both_data['both_score_risk'] = True

        elif (5 >= abs(int(self.guest_position) - int(self.host_position))
              and int(self.guest_position) > int(self.host_position)
                and self.host_score > 1.33
                and self.host_lost > 1.05
                and self.guest_score > 1.25
                and self.guest_lost > 1.12
        ):
            both_data['both_score_risk'] = True

        elif (6 <= abs(int(self.guest_position) - int(self.host_position)) <= 13
              and int(self.guest_position) > int(self.host_position)
                and self.host_score > 1.54
                and self.host_lost > 0.78
                and self.guest_score > 1.15
                and self.guest_lost > 1.32
        ):
            both_data['both_score_risk'] = True

        else:
            both_data['both_score'] = 'not-recommended'
        return both_data


    def total_lower_four(self):
        """
        description: в матче меньше 3.5
        :return: словарь
        """
        total_lower_tree = {}
        if (5 >= abs(int(self.host_position) - int(self.guest_position))
                and self.host_score < 0.93
                and self.guest_score < 0.93
        ):
            total_lower_tree['total_lower_four'] = True
        else:
            total_lower_tree['total_lower_four'] = 'not-recommended'

        return total_lower_tree

    def my_predict(self):
        data = {}

        # print(self.score_one(), self.score_two(), self.both_score())
        data.update(self.score_one())
        data.update(self.score_two())
        data.update(self.both_score())
        data.update(self.lower_one_five_risk())
        data.update(self.total_lower_four())
        self.data.commands.total_predict = data
