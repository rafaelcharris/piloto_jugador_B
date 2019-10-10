from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Rafael'

doc = """
Resumen de los pagos para el participante
"""


class Constants(BaseConstants):
    name_in_url = 'summary_results'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):

    def vars_for_admin_report(self):
        table_rows = []
        for p in self.get_players():
            row = p.participant.vars #quejesto?
            row['participant_code'] = p.participant.code
            row['consent_name'] = p.participant.vars.get('consent_name')
            row['consent_id_number'] = p.participant.vars.get('consent_id_number')
            row['addition_treatment'] = p.participant.vars.get('treatment')
            row['addition_acc_was_correct'] = p.participant.vars.get('addition_acc_was_correct')
            row['addition_acc_acc_payoff'] = p.participant.vars.get('addition_acc_acc_payoff')
            row['addition_final_payoff'] = p.participant.vars.get('addition_final_payoff')
            row['appropriation_task'] = p.participant.vars.get('appr')
            row['joy_destroy'] = p.participant.vars.get('destroy')
            row['joy_was_destroyed'] = p.participant.vars.get('was_destroyed')
            row['joy_belief'] = p.participant.vars.get('belief')
            row['joy_belief_was_correct'] = p.participant.vars.get('belief_was_correct')
            row['joy_payoff'] = p.participant.vars.get('jod_payoff')
            table_rows.append(row)
        return {'table_rows': table_rows}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
