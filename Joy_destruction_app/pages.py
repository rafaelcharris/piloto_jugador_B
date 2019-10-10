from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class instrucciones(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(
            penalty = Constants.penalty,
            endowment = Constants.endowment,
            orden = self.session.config['orden_1']
        )

class MyPage(Page):
    form_model = 'player'
    form_fields = ['destroy']

class Belief(Page):
    form_model = 'player'
    form_fields = ['belief']

    def before_next_page(self):
        self.player.report_joy()


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

        #Agregar el belief_is_correct a la base y a participants
        p1.belief_is_correct = p1_correct_belief
        p2.belief_is_correct = p2_correct_belief
        p1.participant.vars['belief_was_correct'] = p1_correct_belief
        p2.participant.vars['belief_was_correct'] = p2_correct_belief

        #agregar si el jugador fue destruido a la base y a participants
        p1.was_destroyed = p2.destroy
        p2.was_destroyed = p1.destroy
        p1.participant.vars['was_destroyed'] = p2.destroy
        p2.participant.vars['was_destroyed'] = p1.destroy

        #Mejor función de pago.
        #para no hacer ifs, es mejor usar multiplicación que sea cero si el jugador no tomó la decisión de destruir
        #y así mismo que se active la penalty si yo decidí destruir.
        #El último término suma 1 punto más al pago si el belief es igual al pago del otro jugador.
        p1.payoff = Constants.endowment * (1 - Constants.destruction_factor * int(p2.destroy)) - \
                    (int(p1.destroy) * Constants.penalty) + p1_correct_belief
        p1.participant.vars['jod_payoff'] = p1.payoff

        p2.payoff = Constants.endowment * (1 - Constants.destruction_factor * int(p1.destroy)) - \
                    (int(p2.destroy) * Constants.penalty) + p2_correct_belief
        p2.participant.vars['jod_payoff'] = p2.payoff

        print("el payoff del jugador 1 es " + str(p1.participant.vars['jod_payoff']))
        print("el payoff del jugador 2 es " + str(p1.participant.vars['jod_payoff']))


page_sequence = [
    instrucciones,
    MyPage,
    Belief,
    ResultsWaitPage
]

