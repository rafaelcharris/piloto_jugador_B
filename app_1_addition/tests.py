from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import time


class PlayerBot(Bot):

    def play_round(self):


        answer_set =   [287, 205, 235, 219, 338, 271, 280, 203, 239, 182, 235, 226, 190, 244, 335, 283, 282, 303, 288,
                        296, 235, 264, 366, 257, 321, 337, 366, 301, 307, 261, 244, 162, 219, 239, 290, 291, 276, 323,
                        230, 346,]

        answer = answer_set[self.player.round_number - 1]

        if self.player.round_number == 1:
            yield pages.app_1_addition_intro
            yield pages.app_1_addition_task, dict(answer = answer)
        else:
            if self.player.participant.vars['expiry'] - time.time() > 0:
                yield pages.app_1_addition_task, dict(answer = answer)
            else:
                yield pages.app_1_addition_announcement
        if self.round_number == Constants.num_rounds:
            yield pages.app_1_addition_announcement