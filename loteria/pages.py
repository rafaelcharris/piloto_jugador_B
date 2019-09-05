from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class pregunta(Page):
    form_fields = 'player'
    form_model = ['player']

class Results(Page):

    def vars_for_template(self):
        return(

        )
    pass

page_sequence = [
    pregunta,
    Results
]
