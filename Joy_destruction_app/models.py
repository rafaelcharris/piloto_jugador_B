from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Rafael'

doc = """
Joy of destruction
"""


class Constants(BaseConstants):
    name_in_url = 'Joy_destruction_app'
    players_per_group = 2
    num_rounds = 1

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
        label = "Mi expectativa es:",
        choices = [ #Estas opciones hacen que los jugadores vean una string, pero que su respuesta se guarde como True o False
            [True, " que la otra persona decidió reducir mi dotación inicial"],
        [False, "que la otra persona decidió dejar mi dotación inicial tal y como está"]
        ]
    )

    #agregar si el belief es correcto
    belief_is_correct = models.BooleanField()

    #destroyed = models.BooleanField(widget=widgets.HiddenInput()) #este widget sirve para ocultar en form.fields =