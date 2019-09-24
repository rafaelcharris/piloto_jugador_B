from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#Estew codigo funciona. Solo falta cuadrar la diapositiva de resultados.
#escribir mejor las instrucciones
author = 'Rafael'

doc = """
Joy of destruction
"""


class Constants(BaseConstants):
    name_in_url = 'Joy_destruction_app'
    players_per_group = 2
    num_rounds = 1
    endowment = 0
    #constantes iniciales
    endowment = 10
    destruction_factor = 1/2
    penalty = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Acá el usuario escribe si decide o no destruir
    destroy = models.BooleanField(
        label = "¿Usted quiere pagar una moneda experimental para reducir la \
        dotación inicial de la persona con la que fue emparejado?"
    )

    belief = models.BooleanField(
        label = "Mi expectativa es que la otra persona decidió dejar mi dotación inicial tal y como está"
    )
