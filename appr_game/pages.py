from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class appropriation(Page):
    form_fields = ['appr']
    form_model = 'player'

class Results(Page):
    form_fields = ['appr']
    form_model = 'player'

page_sequence = [
    appropriation,
    Results
]
