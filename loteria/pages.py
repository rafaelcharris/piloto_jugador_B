from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class pregunta(Page):

    form_fields = ['lotto']
    form_model = 'player'

class Results(Page):
    form_fields = ['lotto']
    form_model = 'player'

    def vars_for_template(self):
        payoff = self.player.set_payoffs()

page_sequence = [
    pregunta,
    Results
]
