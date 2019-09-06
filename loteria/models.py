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
    endowment = 10000
    perdida_segura = 8000
    perdida_80 = 9000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    lotto = models.StringField(widget=widgets.RadioSelectHorizontal,
                               choices=[["A:", "perdida segura de 8000"], ["B:", "prob 20 de 0 y 80 de 9000"]]
                               )
    #es posbile que me toca quitar todos los player de acá, es redunante
    def set_payoffs(self):
        if self.lotto == "B":
            import random as rm
            prob = rm.random[0.0, 1.0]
            if prob <= 0.8:
                self.payoff = Constants.endowment - Constants.perdida_80
            else:
                self.payoff = Constants.endowment
        else:
            self.payoff = Constants.endowment - Constants.perdida_segura
