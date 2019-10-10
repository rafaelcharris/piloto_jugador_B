from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1000.00,
    'participation_fee': 0,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'Orden_1',
        'display_name': "Orden_1",
        'num_demo_participants': 2,
        'app_sequence': ['app_0_consent','app_1_addition', 'appr_game', 'Joy_destruction_app', 'summary_results', 'Demographics','app_9_report'],
        'time_limit': 60*4,
        'use_browser_bots': False,
        'orden_1': True,
    },
    {
        'name': 'Orden_2',
        'display_name': "Orden_2",
        'num_demo_participants': 2,
        'app_sequence': ['app_0_consent','app_1_addition','Joy_destruction_app', 'appr_game', 'summary_results','Demographics','app_9_report'],
        'time_limit': 60 * 4,
        'use_browser_bots': False,
        'orden_1': False,
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es-co'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = True

ROOMS = [
{
'name': 'Estudio',
'display_name': 'Estudio',
}
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3(@^ry%cbk4)p6#7&*-uk$zblq&b_c!t!(^nkz-4wwey-=_nl('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
