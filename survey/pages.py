from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):

    form_model = 'player'

    form_fields = [
        'gender',
        'gender_other',
        'age',
        'citizen',
        'english',
        'race',
        'race_other',
        'income',
        'education',
        'employment',
        'comments',
    ]

    def age_error_message(self, value):
        if value < 18:
           return "You must be 18 years or older to complete this study."


page_sequence = [Survey]
