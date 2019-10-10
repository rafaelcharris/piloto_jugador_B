from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        import random
            #dele click a la página de las instrucciones
        yield pages.instrucciones
            #Juegue jod: elija aleatoriamente un número entre 1 y 0
        yield pages.MyPage, dict(destroy = True)
            #juege la página de creencias
        yield pages.Belief, dict(belief = False)