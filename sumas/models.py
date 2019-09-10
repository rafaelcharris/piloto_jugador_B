from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random as rm

author = 'Rafael'

doc = """
Juego sumar cinco números de dos dígitos
"""


class Constants(BaseConstants):
    name_in_url = 'sumas'
    players_per_group = None
    num_rounds = 1

    #generate one problem: Esto no se recomienda. Mejor cambiarlo a subsession, pero no pude. Revisar.
    problem = [rm.randint(10,99) for x in range(5)]
    solution = sum(problem)
    print(solution)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Uso esto para poder imprimir el problem como una list al player
    player_problem = map(str, Constants.problem)

    p_solution = models.IntegerField(label = ("+".join(player_problem)))

    #Esto es para guardar en la base de datos si la respuesta fue correcta o no (de hecho creo que me toca es guaradare l numero de corrects)
    is_correct = models.BooleanField()

    def check_answer(self):
        self.is_correct = (self.p_solution == Constants.solution)
