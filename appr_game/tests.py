from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    import random
        #dele click a la página de las instrucciones
    yield pages.appropriation, dict(random.randint(1,0))
        #juege la última página
    yield pages.Results
