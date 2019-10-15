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
        label = "Por favor piense cuidadosamente su decisión."
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

    was_destroyed = models.BooleanField(widget=widgets.HiddenInput()) #este widget sirve para ocultar en form.fields =

    def report_joy(self):
        self.participant.vars['destroy'] = self.destroy
        self.participant.vars['belief'] = self.belief

    belief_shock = models.IntegerField(label = '¿Cuál de los dos eventos posibles que se podían enfrentar en la primera parte de la actividad cree usted que el\
        participante con el que interactuó enfrentó?',
        choices=[
            (1, 'Creo que sus ganancias acumuladas no se vieron afectadas de ninguna manera'),
            (2, 'Creo que el 80% de sus ganancias acumuladas fueron destruidas')
        ]
    )

    belief_shock_is_correct = models.BooleanField()