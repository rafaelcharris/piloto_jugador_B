from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class resumen(Page):
    def vars_for_template(self):
      self.player.push_vars_to_summary()
      self.player.report_summary()
      return dict(
          orden = self.session.config['orden_1']
      )


page_sequence = [resumen]
