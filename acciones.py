# -*- coding: utf-8 -*-

import random

# Gritar -----------------------------------------------------------------------

class gritar(object):

    def __init__(self):
        self.contador = 0

    def run(self, tiempo):

        siguiente_escena = False

        if self.contador == 0:
            print """
            Gritas con todas tus fuerzas, pero el ruido de la montaña
            desgarrándose impide que nadie te oiga. Estás sola.
            """
            self.contador += 1
            return tiempo - 0.5, siguiente_escena

        elif self.contador == 1:
            print """
            Gritas de nuevo. Nadie te oye.
            """
            self.contador += 1
            return tiempo - 0.5, siguiente_escena

        else:
            print """
            '¡AYUDAAA!' Te estás quedando afónica.
            """
            return tiempo - 0.5, siguiente_escena



# Rezar -----------------------------------------------------------------------

class rezar(object):

    def __init__(self):
        self.contador = 0

    def run(self, tiempo):

        siguiente_escena = False

        if self.contador == 0:
            print """
            Cierras los ojos y comienzas a rezar.
            'Padre nuestro, que estás en los cielos...'
            Los momentos más importantes de tu vida pasan por delante de
            tus ojos, pero pronto algo interrumpe tus pensamientos.
            'No puedes rendirte, ¡haz algo!'
            """
            tiempo -= 1
            self.contador += 1
            return tiempo, siguiente_escena

        elif self.contador == 1:
            print """
            Intentas rezar de nuevo, pero no te sale. ¡No puedes rendirte!
            """
            tiempo -= 1
            self.contador += 1
            return tiempo, siguiente_escena

        elif self.contador == 2:
            print """
            Te concentras con todas tus fuerzas y tratas de hablar con Dios.
            'Dios, estoy en una situación complicada. Por favor, ayúdame.'
            Nada ocurre, pero de alguna manera te sientes más tranquila.
            """
            tiempo -= 1
            self.contador += 1
            return tiempo, siguiente_escena

        else:
            print """
            Vuelves a rezar. Cada vez estás más tranquila. Aceptas que vas a morir,
            y lo cierto es que no es tan malo como lo pintan. Observas tu entorno
            mientras caes. El mundo es precioso. Hay pequeños pájaros volando cerca
            de ti que no habías visto hasta ahora. Una pequeña nube con forma de
            hoja flota en el inmenso cielo azul. Sonríes. Estás en paz.
            Cierras los ojos.

            FIN

            """
            exit(0)


# Observar (1) -----------------------------------------------------------------

class observar1(object):

    def __init__(self):
        self.contador = 0

    def run(self, tiempo):

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
        tiempo -= 0.2
        siguiente_escena = True
        return tiempo, siguiente_escena


# Acción desconocida -----------------------------------------------------------

class accion_desconocida(object):

    respuesta1 = """
    No es momento, Sonia, no es momento.
    """

    respuesta2 = """
    No sé a qué te refieres.
    """

    respuesta3 = """
    Lo siento, no entiendo lo que dices.
    Para ver las acciones disponibles, escribe 'ayuda'.
    """

    respuestas = [respuesta1, respuesta2, respuesta3]

    def run(self):
        r = random.randint(1,3)
        print respuestas[r]



# Explorar bolso ---------------------------------------------------------------
#
# explorar_bolso = c.Accion()
#
# def efecto1(persona):
#     print """
#     Coges el bolso con las manos y tratas desesperadamente de buscar
#     algo dentro que pueda ayudarte, pero la cremallera está cerrada
#     y no consigues abrirla.
#     """
#     persona.tiempo -= 1
#
# def efecto2(persona):
#     print """
#     No puedes abrir el bolso.
#     """
#     persona.tiempo -= 1
#
# explorar_bolso.add_efecto(efecto1)
# explorar_bolso.add_efecto(efecto2)
