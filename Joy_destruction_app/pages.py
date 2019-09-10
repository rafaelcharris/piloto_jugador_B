from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class instrucciones(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(
            penalty = Constants.penalty
        )

class MyPage(Page):
    form_model = 'player'
    form_fields = ['destroy']

class Results(Page):
    #Estos son espacios que el jugador puede llenar
    form_model = 'player'
    form_fields = ['destroy']

    #Esta funcion trae al template
    def vars_for_template(self):
        self.player.get_payoff()
        return dict(
            penalty=Constants.penalty
            )

class ResultsWaitPage(WaitPage):
    #Hacer calculos del payoff
    def after_all_players_arrive(self):
        #Deme el grupo que participó en cada ronda
        group = self.group

        #de este grupo, clasifiqué toma los jugadores por el "tipo" que son dentro del grupo
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        #Mejor función de pago.
        #para no hacer ifs, es mejor usar multiplicación que sea cero si el jugador no tomó la decisión de destruir
        #y así mismo que se active la penalty si yo decidí destruir.
        p1.payoff = Constants.endowment * (1 - Constants.destruction_factor * int(p2.destroy)) - \
                    (int(p1.destroy) * Constants.penalty)
        p2.payoff = Constants.endowment * (1 - Constants.destruction_factor * int(p1.destroy)) - \
                    (int(p2.destroy) * Constants.penalty)

page_sequence = [
    instrucciones,
    MyPage,
    ResultsWaitPage,
    Results
]

