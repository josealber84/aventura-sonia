# -*- coding: utf-8 -*-

class Accion(object):

    def __init__(self):
        self.estado = 0
        self.efectos = []
        self.args = []

    def run(self):
        if self.args[self.estado] is not None:
            self.efectos[self.estado](self.args[self.estado])
        else:
            self.efectos[self.estado]()

        self.estado += 1

        if self.estado > (len(self.efectos) - 1):
            self.estado = (len(self.efectos) - 1)

    def add_efecto(self, efecto, arg = None):
        self.efectos.append(efecto)
        self.args.append(arg)

    def reset_estado(self):
        self.estado = 0

# -----------------------------------------------------------------------

class Sonia(object):

    def __init__(self):
        self.tiempo = 0
        self.altura = 0
        self.prompt = "\nS > "

    def set_tiempo(self, tiempo):
        self.tiempo = tiempo

    def set_altura(self, altura):
        self.altura = altura
        self.tiempo = math.ceil(math.sqrt(altura * 2 / 9.8))

    def tiempo_restante(self):
        print """
        Quedan %s segundos para el impacto.
        """ % self.tiempo

    def mostrar_asterisco(self):
        self.prompt = "\nS*> "

    def ocultar_asterisco(self):
        self.prompt = "\nS > "


# -----------------------------------------------------------------------

class Escena(object):

    def __init__(self, descripcion = None):
        self.escena_inicial = False
        self.escena_final = False
        self.descripcion = descripcion

    def run(self):
        if self.escena_inicial:
            system("clear")

        if self.descripcion is not None:
            print self.descripcion

        if self.escena_final:
            exit(0)

    def set_escena_inicial(self):
        self.escena_inicial = True

    def set_escena_final(self):
        self.escena_final = True
