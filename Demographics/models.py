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

def preg_likert(label):
    return models.IntegerField(
        label = label,
        choices = [1,2,3,4,5],
        widget=widgets.Slider,
    )
def preg_cuatro(label):
    return models.StringField(
        label = label,
        choices = ['No', 'Sí, una vez', 'Sí, más de una vez']
    )

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
    riesgo_1 = preg_likert(label = '¿Cómo se considera usted? Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos o intenta evitar tomar riesgos? Por favor conteste usando la siguiente escala de uno a cinco, '
                                   'donde uno indica “totalmente dispuesto a tomar riesgos” y cinco '
                                   '“Totalmente contrario a tomar riesgos”. ')
    riesgo_2 = preg_likert(label = 'Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos de carácter financiero o intenta evitar tomar riesgos financieros? Por favor conteste usando la siguiente escala de uno a cinco,'
                                   ' donde uno indica “totalmente dispuesto a tomar riesgos” y cinco “Totalmente contrario a tomar riesgos”.')
    gasto_no_plan = models.StringField(
        label = 'Si tuviera que conseguir COP 600.000 en una semana para enfrentar un gasto no planeado, ¿qué tanta dificultad cree que tendría en conseguir el dinero?',
        choices = ['No tendría dificultad', 'Tendría alguna dificultad, pero lo conseguiría', 'No sé si lo conseguiría', 'Definitivamente no lo conseguiría' ]
    )
    asalto_fisico = preg_cuatro(
        label = '¿Ha sido objeto de asalto físico en los últimos doce meses?'
    )
    asalto_fisico_numero = models.IntegerField(
        label = 'Por favor, indique cuántas veces:'
    )
    asalto_fisico_familiar = preg_cuatro(
        label = "¿Algún familiar suyo ha sido objeto de asalto físico en los últimos doce meses?"
    )
    asalto_fisico_numero_familiar = models.IntegerField(
        label='Por favor, cuántas veces:'
    )
    confrontacion = preg_cuatro(
        label = '¿Se ha encontrado en medio de una confrontación que involucre el uso de pistolas u otras armas de fuego en los últimos cinco años?'
    )
    confrontacion_numero = models.IntegerField(
        label = 'Por favor, indique cuántas veces:'
    )
    violencia = preg_cuatro(
        label = '¿Ha sido objeto de violencia directa en los últimos doce meses?'
    )
    prob_atraco = preg_likert(
        label = 'Cuál cree que es su probabilidad de ser víctima de un atraco en los próximos 12 meses?'
                'Por favor conteste usando la siguiente escala de uno a cinco, donde uno indica “no muy probable” y 5 indica “muy probable”.'
    )
    barrio_violento = preg_likert(
        label = '¿Está de acuerdo con la afirmación “el barrio donde vivo es violento”?'
                'Por favor, conteste usando la siguiente escala de uno a cinco, donde uno indica “estoy totalmente en desacuerdo” y 5 indica “estoy totalmente de acuerdo”.'
    )
    