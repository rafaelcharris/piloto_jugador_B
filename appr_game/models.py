from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random as rm

author = 'Rafael'

doc = """
Juego de apropiación
"""


class Constants(BaseConstants):
    name_in_url = 'appr_game'
    players_per_group = None
    num_rounds = 1
    #Constantes iniciales
    endowment = c(10000)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    appr = models.BooleanField(
        label = "¿Desea robar el 80% de las ganancias de otro participante del estudio de otra sesión?",
        initial=True,
        choices=[
            [True, "Sí"], #Esto hace que pueda usar el boolean, pero cambio las opciones que ve el jugador
            [False, "No"]
        ]
    )
    def report_at(self):
        self.participant.vars['appr'] = self.appr
