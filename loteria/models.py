from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
author = 'Rafael'

doc = """
Loteria en framing de perdida para inducir a que 
tomen en la siguiente tarea y tener medida de preferencias hacia el riesgo 
"""


class Constants(BaseConstants):
    name_in_url = 'loteria'
    players_per_group = None
    num_rounds = 1

    endowment = 100

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    lotto = models.BooleanField(label = "A")