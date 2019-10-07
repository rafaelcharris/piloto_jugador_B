from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        import random
            #dele click a la página de las instrucciones
        yield pages.appropriation, dict(appr = bool(random.getrandbits(1)))
            #juege la última página
        yield pages.Results
