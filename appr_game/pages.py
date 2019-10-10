from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class appropriation(Page):
    form_fields = ['appr']
    form_model = 'player'
    def vars_for_template(self):
        return dict(orden = self.session.config['orden_1'])

class Results(Page):
    form_fields = ['appr']
    form_model = 'player'

    def before_next_page(self):
        self.player.report_at()

page_sequence = [
    appropriation,
    Results
]
