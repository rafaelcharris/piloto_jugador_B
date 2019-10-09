from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class instrucciones(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(
            penalty = Constants.penalty,
            endowment = Constants.endowment
        )

class MyPage(Page):
    form_model = 'player'
    form_fields = ['destroy']

class Results(Page):
    #Estos son espacios que el jugador puede llenar
    form_model = 'player'
    form_fields = ['destroy', 'destroyed']

    #Esta funcion trae al template
    def vars_for_template(self):
        return dict(
            penalty=Constants.penalty
            )

class Belief(Page):
    form_model = 'player'
    form_fields = ['belief']

class ResultsWaitPage(WaitPage):
    #Hacer calculos del payoff
    def after_all_players_arrive(self):
        #Deme el grupo que participó en cada ronda
        group = self.group

        #de este grupo, clasifiqué toma los jugadores por el "tipo" que son dentro del grupo
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        #Determinar si el belief del jugador si es o no correcto
        p1_correct_belief = p1.belief == p2.destroy
        p2_correct_belief = p2.belief == p1.destroy

        print("el jugador 1 destruyó  =  " + str(p1.destroy))
        print("el jugador 2 destruyó = " + str(p2.destroy))

        #Agregar el belief_is_correct a la base
        p1.belief_is_correct = p1_correct_belief
        p2.belief_is_correct = p2_correct_belief

        #agregar si el jugador fue destruido a la base
        #p1.destroyed = p2.destroy
        #p2.destroyed = p1.destroy

        #print("el jugador 1 fue destruido? " + str(p1.destroyed))
        #print("el jugador 2 fue destruido? " + str(p2.destroyed))
        #Mejor función de pago.
        #para no hacer ifs, es mejor usar multiplicación que sea cero si el jugador no tomó la decisión de destruir
        #y así mismo que se active la penalty si yo decidí destruir.
        #El último término suma 1 punto más al pago si el belief es igual al pago del otro jugador.
        p1.payoff = Constants.endowment * (1 - Constants.destruction_factor * int(p2.destroy)) - \
                    (int(p1.destroy) * Constants.penalty) + p1_correct_belief
        print("El pago del jugador 1 es:" + str(p1.payoff))
        p2.payoff = Constants.endowment * (1 - Constants.destruction_factor * int(p1.destroy)) - \
                    (int(p2.destroy) * Constants.penalty) + p2_correct_belief
        print("El pago del jugador 2 es:" + str(p2.payoff))

page_sequence = [
    instrucciones,
    MyPage,
    Belief,
    ResultsWaitPage,
    Results
]

