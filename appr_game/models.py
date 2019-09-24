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

    appr = models.BooleanField(label = "¿Desea apropiarse del 80% de los puntos obtenidos en la actividad \
    de las sumas por otro participante en el estudio")