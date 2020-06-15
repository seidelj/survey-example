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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.IntegerField(
        label='What is your gender?',
        choices = [
            [0, 'Female'],
            [1, 'Male'],
            [2, 'Other, please specify'],
            [3, 'Prefer not to answer'],
        ],
    )

    gender_other = models.StringField(
        label="If you selected other, please specify",
        blank=True
    )

    age = models.IntegerField(
        label="Enter your age",
    )

    citizen = models.IntegerField(
        label = 'Are you a citizen or permanent resident of the United States?',
        choices = [
            [0, 'No'],
            [1, 'Yes'],
        ]
    )

    english = models.IntegerField(
        label="Rate your English",
        choices = [
            [0, 'Native'],
            [1, 'Fluent'],
            [2, 'Proficient'],
        ]
    )

    race = models.IntegerField(
        label = "What race/ethnicity do you identify yourself as?",
        choices = [
            [0, "American Indian and Alaska Native (having origins in any of the original peoples of North, Central, or South America and maintaining tribal affiliation or community attachment)"],
            [1, "Asian (having origins in any of the original people of the Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam)"],
            [2, "Black or African (having origins in any of the Black racial groups of Africa)"],
            [3, "Hispanic (having origins in Mexico, Central or South America)"],
            [4, "White (having origins in any of the original peoples of Europe, the Middle East, or North Africa)"],
            [5, "Native Hawaiian and other pacific islander (having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands)"],
            [6, "Some other race, please specify"],
            [7, "Prefer not to answer"]
        ]
    )

    race_other = models.StringField(
        label = "If you selected other, please specify",
        blank = True
    )

    income = models.IntegerField(
        label = "What is the total (gross) income last year of your household?",
        choices = [
            [0, '$0 to less than $25,000'],
            [1, '$25,0000 to less than $50,000'],
            [2, '$50,000 to less than $75,000'],
            [3, '$75,000 to less than $100,000'],
            [4, '$100,000 to less than $125,000'],
            [5, '$125,000 to less than $150,000'],
            [6, '$150,000 or more'],
            [7, 'Prefer not to answer'],
        ]
    )

    education = models.IntegerField(
        label = "What is your highest level of education?",
        choices = [
            [0, 'Some high school'],
            [1, 'Completed high school'],
            [2, 'Some college'],
            [3, 'Completed college'],
            [4, 'Some grad/professional school'],
            [5, 'Completed grad/professional school'],
            [6, 'Prefer not to answer'],
        ]
    )


    employment = models.IntegerField(
        label = "Please indicate your employment status",
        choices = [
            [0, 'Employed, full-time'],
            [1, 'Employed, part-time'],
            [2, 'Not employed, looking for work'],
            [3, 'Not employed, not looking for work'],
            [4, 'Retired'],
            [5, 'Student'],
            [6, 'Prefer not to answer'],
        ]
    )

    comments = models.LongStringField(
        label = "You may add any comments here",
        blank = True,
    )
