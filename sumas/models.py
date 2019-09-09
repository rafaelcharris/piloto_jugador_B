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

class Subsession(BaseSubsession):
    # generate one problem
    def creating_session(self):
        for player in self.get_players():
                player.problem = [rm.randint(10,99) for x in range(5)]
                solution = sum(player.problem)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Uso esto para poder imprimir el problem como una list al player
    def get_problems(self):
        self.subsession.creating_sessions(self)
        player_problem = map(str, self.problem)
        p_solution = models.IntegerField(label = ("+".join(player_problem)))

    #Esto es para guardar en la base de datos si la respuesta fue correcta o no (de hecho creo que me toca es guaradare l numero de corrects)
    is_correct = models.BooleanField()

    def check_answer(self):
        self.is_correct = (self.p_solution == self.subsession.solution)