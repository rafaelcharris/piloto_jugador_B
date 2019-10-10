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
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    #primera parte:
    summary_addition_acc_was_correct = models.IntegerField()
    summary_addition_acc_payoff = models.IntegerField()
    summary_addition_final_payoff = models.FloatField()
    #segunda parte:
    summary_appr = models.StringField()
    #tercera parte
    summary_joy_destroy = models.StringField()
    summary_joy_was_destroyed = models.StringField()
    summary_belief = models.StringField()
    summary_belief_was_correct = models.StringField()
    summary_jod_payoff_points = models.CurrencyField()
    summary_jod_payoff_cop = models.CurrencyField()

    #Final
    summary_FINAL_payoff = models.CurrencyField()

    #def vars_for_report(self):
    #    self.participant.vars['payoff_final'] = self.participant.vars.get('jod_payoff_cop') + self.participant.vars.get('addition_final_payoff')

    def push_vars_to_summary(self):
        self.summary_addition_acc_was_correct = self.participant.vars.get('addition_acc_was_correct')
        self.summary_addition_acc_payoff = self.participant.vars.get('addition_acc_payoff')
        self.summary_addition_final_payoff = self.participant.vars.get('addition_final_payoff')

        if self.participant.vars['appr']:
            self.summary_appr = 'Sí'
        else:
            self.summary_appr = 'No'

        if self.participant.vars['destroy']:
            self.summary_joy_destroy = 'Sí'
        else:
            self.summary_joy_destroy = 'No'

        if self.participant.vars['was_destroyed']:
            self.summary_joy_was_destroyed = 'Sí'
        else:
            self.summary_joy_was_destroyed = 'No'

        if self.participant.vars['belief']:
            self.summary_belief = 'Sí'
        else:
            self.summary_belief = 'No'

        if self.participant.vars['belief_was_correct']:
            self.summary_belief_was_correct = 'Sí'
        else:
            self.summary_belief_was_correct = 'No'

        self.summary_jod_payoff_points = self.participant.vars.get('jod_payoff_points')
        self.summary_jod_payoff_cop = self.participant.vars.get('jod_payoff_cop') #no se puede entrar al report antes de que temrinen esta parte. una sol es darle valor de algo al principio

        self.summary_FINAL_payoff = self.participant.vars.get('jod_payoff_cop') + self.participant.vars.get('addition_final_payoff')
        print('el pago final es: ' + str(self.summary_FINAL_payoff))

    def report_summary(self):
        self.participant.vars['FINAL_payoff'] = self.summary_FINAL_payoff

