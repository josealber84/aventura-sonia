# -*- coding: utf-8 -*-

import acciones as a

# -----------------------------------------------------------------------

class Escena(object):

    descripcion = "Cambia esta descripción"
    prompt = "\nS > "

    def run(self):
        print "Implementa el método run de esta escena"



# Escena intro -----------------------------------------------------------------

class Intro(Escena):

    descripcion = """

    UNA INESPERADA AVENTURA

    Las vistas desde lo alto del Preikestolen son preciosas.

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
    a la desesperada, pero no consigue agarrarte.

    """

    def run(self):
        print self.descripcion

# Escena muerte suelo ----------------------------------------------------------

class Muerte_suelo(Escena):

    descripcion = """
    Te estampas contra las afiladas rocas del fondo del fiordo.
    Quizás, después de todo, J tenía razón.

    FIN

    """

    def run(self):
        print self.descripcion
        exit(0)


#  Escena cayendo al vacío -----------------------------------------------------

class Cayendo_al_vacio(Escena):

    descripcion = """
    Caes al vacío. Cuatrocientos metros te separan de las afiladas rocas y de
    una muerte segura. Te quedan 10 segundos de vida.
    ¡A menos que puedas hacer algo!
    """

    acciones = {
        "rezar" : a.rezar(),
        "gritar" : a.gritar(),
        "observar": a.observar1()
    }

    def mostrar_acciones(self):
        print ""
        print "Puedes realizar las siguientes acciones:"
        print self.acciones.keys()
        return raw_input(self.prompt)

    def run(self):

        print self.descripcion

        siguiente_escena = False
        tiempo = 10

        while not siguiente_escena and tiempo > 0:

            accion = self.mostrar_acciones()
            tiempo, siguiente_escena = self.acciones[accion].run(tiempo)

            if tiempo > 0:
                print "Te quedan %s segundos de vida" % tiempo


#  Escena cayendo al vacío -----------------------------------------------------


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
            explorar_bolso.run()
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
            explorar_bolso.run()
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
            explorar_bolso.run()
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
