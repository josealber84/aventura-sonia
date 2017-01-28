# -*- coding: utf-8 -*-

import escenas as e

def jugar():

    escena_intro = e.Intro()
    escena_caida = e.Cayendo_al_vacio()
    
    escena_intro.run()
    escena_caida.run()

jugar()
