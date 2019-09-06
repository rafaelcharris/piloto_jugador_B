from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random as rm

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
                               choices=[["A:", "perdida segura de 8000 pesos"], ["B:", "probabilidad de 20% de "
                                                                                       "perder 0 y 80% de perder 9000"]]
                               )
    #Función que define los pagos
    def set_payoffs(self):
        if self.lotto == "B:":
            #esto le asigna a prob un número enter 0 y 1
            prob = rm.random()
            #Si ese número es menor de 0.8 (la probabilidad es igual o menor que 80%) entonces reste 9000
            if prob <= 0.8:
                self.payoff = Constants.endowment - Constants.perdida_80
            #Si no, haga que no pierda nada.
            else:
                self.payoff = Constants.endowment
        else:
            self.payoff = Constants.endowment - Constants.perdida_segura

    appr = models.BooleanField(label = "¿desea tomar el 80% de las ganancias de otro jugador?")