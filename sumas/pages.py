from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['p_solution']

class Results(Page):
    form_model = 'player'
    form_fields = ['p_solution', 'is_correct']

    def vars_for_template(self):
        self.player.check_answer()



page_sequence = [
    MyPage,
    Results
]
