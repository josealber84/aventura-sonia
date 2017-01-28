# -*- coding: utf-8 -*-

from sys import exit
from os import system
import math

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
