from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Rafael'

doc = """
Encuesta demográfica
"""


class Constants(BaseConstants):
    name_in_url = 'Demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sexo =models.StringField(
        label= '¿Cuál es su sexo',
        choices =["Masculino", "Femenino", "Otro"])
    edad = models.IntegerField(label = '¿Cuál es su edad?')
    e_civil = models.StringField(label = '¿Cuál es su estado civil?')
    facultad = models.StringField(label = '¿Facultad?')
    carrera = models.StringField(label = 'Carrera')
    times_matriculado = models.IntegerField(label = "¿Cuántas veces se ha matriculado contando el actual semestre?")
    ed_padre = models.StringField(label = "¿Cuál es el máximo nivel de educación alcanzado por su padre?")
    ed_madre = models.StringField(label = "¿Cuál es el máximo nivel de educación alcanzado por su madre?")
    estrato = models.IntegerField(
        label = "De acuerdo con las facturas de sus servicios públicos, ¿cuál es el estrato de la vivienda actual donde reside?",
        choices = [1,2,3,4,5,6]
    )
    ingresos = models.IntegerField( #dar choices?
        label = "¿Cuál es el valor aproximado de sus ingresos mensuales en Salarios Mínimos (SMMLV=COP 828,116)?"
    )
    localidad = models.StringField(
        label = '¿Cuál es la localidad en la que usted reside?',
        choices = ["No vivo en Bogotá", "Usaquén", "Chapinero", "Santa fé", "La Candelaria",
                   "Antonio Nariño", "San Cristobal", "Usme", "Sumapaz", "Suba", "Barrios Unidos", "Engativá",
                   "Teusaquillo", "Fontibón", "Martires", "Puente Aranda", "Kennedy", "Bosa", "Rafael Uribe Uribe", "Tunjuelito",
                   "Ciudad Bolivar"
                   ]
    )
    peso = models.IntegerField(label = "¿Cuál es su peso en kilogramos?")
    altura = models.IntegerField(label = "¿Cuál es su altura en centímetros?")
    
