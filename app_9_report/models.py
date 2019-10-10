from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels
from django.core.validators import EmailValidator


author = 'Your name here'

doc = """
Reporte de resultados, pero para nostros
"""


class UnalEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        if domain_part != 'unal.edu.co':
            return False
        return True
    message = "Por favor ingrese un correo con dominio @unal.edu.co"


class Constants(BaseConstants):
    name_in_url = 'app_9_report'
    players_per_group = None
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
            row['joy_payoff_points'] = p.participant.vars.get('jod_payoff_points')
            row['payoff_final'] = p.participant.vars.get('FINAL_payoff')
            table_rows.append(row)
        return {'table_rows': table_rows}


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    e_mail = djmodels.EmailField(verbose_name='Correo Electrónico', validators=[UnalEmailValidator()])

#    def report_vars_for_database(self):
#        self.report_participant_code = self.participant.code
#        vars_fields = [
#            'participant_code',
#            'consent_name',
#            'consent_id_number',
#            'addition_acc_was_correct',
#            'addition_acc_acc_payoff',
#            'addition_final_payoff',
#            'trust_metarole',
#            'trust_paying_round',
#            'trust_t_final_payoff',
#            'trust_b_final_payoff',
#        ]
#
#        for field in vars_fields:
#            setattr(self, 'report_{}'.format(field), self.participant.vars.get(field))
#