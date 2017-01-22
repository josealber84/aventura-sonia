# -*- coding: utf-8 -*-

class accion(object):

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

    def __init__(self, tiempo):
        self.tiempo = tiempo
        self.prompt = "\nS > "

    def tiempo_restante(self):
        print """
        Quedan %s segundos para el impacto.
        """ % self.tiempo

    def mostrar_asterisco(self):
        self.prompt = "\nS*> "

    def ocultar_asterisco(self):
        self.prompt = "\nS > "
