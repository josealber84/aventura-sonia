# -*- coding: utf-8 -*-
import math
import clases as c
from os import system
from sys import exit


# Sonia -----------------------------------------------------------------------

sonia = c.Sonia()
sonia.set_altura(400) # 400 metros de caída

# Gritar -----------------------------------------------------------------------

gritar = c.Accion()

def efecto1(persona):
    print """
    Gritas con todas tus fuerzas, pero el ruido de la montaña
    desgarrándose impide que nadie te oiga. Estás sola.
    """
    persona.tiempo -= 0.5

def efecto2(persona):
    print """
    Gritas de nuevo. Nadie te oye.
    """
    persona.tiempo -= 0.5

def efecto3(persona):
    print """
    '¡AYUDAAA!' Te estás quedando afónica.
    """
    persona.tiempo -= 0.5

gritar.add_efecto(efecto1, sonia)
gritar.add_efecto(efecto2, sonia)
gritar.add_efecto(efecto3, sonia)

# Rezar -----------------------------------------------------------------------

rezar = c.Accion()

def efecto1(persona):
    print """
    Cierras los ojos y comienzas a rezar.
    'Padre nuestro, que estás en los cielos...'
    Los momentos más importantes de tu vida pasan por delante de
    tus ojos, pero pronto algo interrumpe tus pensamientos.
    'No puedes rendirte, ¡haz algo!'
    """
    persona.tiempo -= 1

def efecto2(persona):
    print """
    Intentas rezar de nuevo, pero no te sale. ¡No puedes rendirte!
    """
    persona.tiempo -= 1

def efecto3(persona):
    print """
    Te concentras con todas tus fuerzas y tratas de hablar con Dios.
    'Dios, estoy en una situación complicada. Por favor, ayúdame.'
    Nada ocurre, pero de alguna manera te sientes más tranquila.
    """
    persona.tiempo -= 1

def efecto4(persona):
    muerte_iluminacion.run()

rezar.add_efecto(efecto1, sonia)
rezar.add_efecto(efecto2, sonia)
rezar.add_efecto(efecto3, sonia)
rezar.add_efecto(efecto4, sonia)

# Acción desconocida -----------------------------------------------------------

accion_desconocida = c.Accion()

def efecto1():
    print """
    No es momento, Sonia, no es momento.
    """

def efecto2():
    print """
    No sé a qué te refieres.
    """

def efecto3(accion):
    print """
    Lo siento, no entiendo lo que dices.
    Para ver las acciones disponibles, escribe 'ayuda'.
    """
    accion.reset_estado()

accion_desconocida.add_efecto(efecto1)
accion_desconocida.add_efecto(efecto2)
accion_desconocida.add_efecto(efecto3, accion_desconocida)

# Escena intro -----------------------------------------------------------------

descripcion = """

UNA INESPERADA AVENTURA

Las vistas desde los alto del Preikestolen son preciosas.

Estás sentada en el borde, masticando un delicioso sandwich de salchichón.
J, tumbado en el suelo detrás de ti, te agarra de la camiseta
pensando que hay posibilidades de que te caigas. Qué mono. Y qué miedica.
'¿Cómo voy a caerme, si estoy sentada?'

La suave brisa de julio revuelve levemente tu pelo. A lo lejos, una
ligera niebla difumina el imponente paisaje.

Debajo, rocas afiladas como cuchillas te observan espectantes,
casi salivando, esperando el próximo traspiés de un turista patoso.

Después de más de media hora en la cima, llega el momento de bajar.
J está más tranquilo, leyendo su guía en busca de algún sitio donde pasar
la noche. Le miras y te hace la señal de '¿nos vamos?'. Asientes y guardas
el papel albal en tu bolso. Te levantas, te pones la chaquetilla rosa y te
cuelgas el bolso al hombro.

Se escucha un rumor durante dos segundos. No es un sonido desagradable,
pero todos los presentes os quedáis quietos. El sonido es grave, profundo,
extraño. Es como si a la montaña le hubiese dado un retortijón.
J levanta una ceja. 'Es sólo un barco lejano', piensas.

Das dos pasos y el suelo empieza a moverse. ¿Te estás mareando? Te agachas
para no caerte, pero el movimiento es intenso y tropiezas. Alguien grita:
"¡TERREMOTOOOOOO!"

Todo parece pasar muy despacio. Mueves hacia atrás el pie izquiedo en busca
de un apoyo, pero sólo hay aire. El suelo sigue moviéndose. J estira un brazo
a la desesperada, pero no consigue agarrarte. Caes al vacío. %s metros
de caída libre te separan de la muerte. Te quedan %s segundos de vida.
¡A menos que puedas hacer algo!

(Escribe 'ayuda' siempre que haya un asterisco tras tu nombre para ver
 qué nuevas acciones puedes realizar)

""" % (ALTURA, sonia.tiempo)

intro = Escena(descripcion)
intro.set_escena_inicial()

# Escena muerte suelo ----------------------------------------------------------

descripcion = """
Te estampas contra las afiladas rocas del fondo del fiordo.
Quizás, después de todo, J tenía razón.

FIN

"""

muerte_suelo = Escena(descripcion)
muerte_suelo.set_escena_final()

# Escena muerte iluminación ----------------------------------------------------

descripcion = """
Vuelves a rezar. Cada vez estás más tranquila. Aceptas que vas a morir,
y lo cierto es que no es tan malo como lo pintan. Observas tu entorno
mientras caes. El mundo es precioso. Hay pequeños pájaros volando cerca
de ti que no habías visto hasta ahora. Una pequeña nube con forma de
hoja flota en el inmenso cielo azul. Sonríes. Estás en paz.
Cierras los ojos.

FIN

"""

muerte_iluminacion = Escena(descripcion)
muerte_suelo.set_escena_final()

#  -----------------------------------------------------------------------


def explorar_bolso():
    global EXPLORAR_BOLSO
    if EXPLORAR_BOLSO == 0:
        print """
        Coges el bolso con las manos y tratas desesperadamente de buscar
        algo dentro que pueda ayudarte, pero la cremallera está cerrada
        y no consigues abrirla.
        """
        EXPLORAR_BOLSO += 1
    else:
        print """
        No puedes abrir el bolso.
        """


def estado0():
    """Cayendo al vacío. No sabes nada"""

    siguiente = False

    while not siguiente and sonia.tiempo > 0:

        accion = raw_input(sonia.prompt)

        if accion == 'ayuda':
            print """
            Puedes 'observar', 'rezar' o 'gritar'
            """
            sonia.ocultar_asterisco()
        elif accion == "rezar":
            rezar.run()
        elif accion == 'gritar':
            gritar.run()
        elif accion == 'observar':
            print """
            Miras hacia abajo. Las vistas impresionan. Una pared de piedra cae
            verticalmente hasta el agua. Abajo, el oleaje es suave. Justo
            debajo de donde estás, la escasa profundidad del agua permite
            ver las afiladas rocas.
            La pared rocosa tiene algunas ramas retorcidas aquí y allá.
            Vas vestida con unos vaqueros, una camiseta, la chaquetilla y
            tu bolso. Estás descalza, aunque no sabes por qué.
            Arriba no ves a nadie que pueda ayudarte.
            """
            sonia.tiempo -= 0.2
            siguiente = True
        else:
            accion_desconocida.run()

        if sonia.tiempo > 0:
            sonia.tiempo_restante()
def estado1():
    """Has visto el bolso y las ramas"""

    sonia.mostrar_asterisco()
    siguiente = False

    while not siguiente and sonia.tiempo > 0:

        accion = raw_input(sonia.prompt)

        if accion == 'ayuda':
            print """
            Puedes 'rezar', 'gritar', 'agarrar ramas' o 'explorar bolso'
            """
            sonia.ocultar_asterisco()
        elif accion == "rezar":
            rezar.run()
        elif accion == 'gritar':
            gritar.run()
        elif accion == 'agarrar ramas':
            print """
            Lanzas las manos para agarrar una de las ramas que sobresalen.
            Consigues agarrarte, pero vas demasiado deprisa y la rama
            resbala, rasgándote gravemente la mano derecha.
            """
            sonia.tiempo -= 0.2
            siguiente = True
        elif accion == 'explorar bolso':
            explorar_bolso()
            sonia.tiempo -= 1
        else:
            accion_desconocida.run()
            sonia.tiempo -= 0.2

        if sonia.tiempo > 0:
            sonia.tiempo_restante()
def estado2():
    """Has intentado agarrarte a las ramas"""



    sonia.mostrar_asterisco()

    siguiente = False

    while not siguiente and sonia.tiempo > 0:

        accion = raw_input(sonia.prompt)

        if accion == 'ayuda':
            print """
            Puedes 'rezar', 'gritar', 'agarrar ramas con bolso' o 'explorar bolso'
            """
            sonia.ocultar_asterisco()
        elif accion == "rezar":
            rezar.run()
        elif accion == 'gritar':
            gritar.run()
        elif accion == 'agarrar ramas con bolso':
            print """
            Realizas un esfuerzo colosal tratando de enganchar el bolso con
            alguna de las ramas que pasan a tu lado. El asa se engancha
            parcialmente en una rama, pero es demasiado fina y se rompe
            enseguida, desequilibrándote en el aire.
            """
            sonia.tiempo -= 0.5
            siguiente = True
        elif accion == 'explorar bolso':
            explorar_bolso()
            sonia.tiempo -= 1
        else:
            accion_desconocida.run()

        if sonia.tiempo > 0:
            sonia.tiempo_restante()
def estado3():
    """Has intentado agarrarte a las ramas con el bolso"""


    sonia.ocultar_asterisco()
    siguiente = False

    while not siguiente and sonia.tiempo > 0:

        accion = raw_input(sonia.prompt)

        if accion == 'ayuda':
            print """
            Puedes 'rezar', 'gritar', 'agarrar ramas con bolso' o 'explorar bolso'
            """
        elif accion == "rezar":
            rezar.run()
        elif accion == 'gritar':
            gritar.run()
        elif accion == 'agarrar ramas con bolso':
            print """
            Lo intentas de nuevo. Esta vez el asa se engancha a un saliente de
            piedra. El tirón es muy fuerte, y sientes que te descoyuntas, pero
            consigues mantenerte enganchada. El bolso cruje, pero
            afortunadamente ha aguantado el tirón.
            """
            siguiente = True
        elif accion == 'explorar bolso':
            explorar_bolso()
            sonia.tiempo -= 1
        else:
            accion_desconocida.run()
            sonia.tiempo -= 0.2

        if sonia.tiempo > 0 and siguiente == False:
            sonia.tiempo_restante()
def estado4():
    """Cuelgas de un saliente de roca"""


    sonia.mostrar_asterisco()

    siguiente = False

    while not siguiente and sonia.tiempo > 0:

        gritos = 0
        accion = raw_input(sonia.prompt)

        if accion == 'ayuda':
            print """
            Puedes 'rezar', 'gritar', 'esperar', 'observar', 'soltarme'
            """
            sonia.ocultar_asterisco()
        elif accion == "rezar":
            print """
            'Por favor, Dios mío, échame una mano...'
            """
        elif accion == 'gritar':
            if gritos == 0:
                print """
                '¡AYUDAAAA!'
                """
            else:
                print """
                '¡AYUDAAAAAAAAA!', te estás quedando afónica.
                """
        elif accion == 'esperar':
            print """
            Colgando del acantilado, te das unos segundos para descansar y
            recomponerte.
            """
        elif accion == 'observar':
            print """
            Estás colgando en el vacío. Tus brazos se entrelazan, agarrando el
            bolso de Hello Kitty con fuerza. ¡Menos mal que no es de los chinos!
            El asa del bolso se ha enganchado a un saliente rocoso. No puedes
            ver si se ha enganchado con fuerza o no desde tu posición, así que
            no te mueves mucho.
            """
        else:
            accion_desconocida.run()

def jugar():
  """Ejecuta esta función para que comience el juego"""

  config()
  intro.run()
  estado0()
  estado1()
  estado2()
  estado3()
  estado4()

  if(sonia.tiempo <= 0):
      muerte_suelo.run()

jugar()
