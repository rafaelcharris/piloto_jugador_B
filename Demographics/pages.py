from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Cuestionario(Page):
    form_fields = ['player']
    form_model = 'player'

page_sequence = [
    Cuestionario,
]
