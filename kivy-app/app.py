# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Juego(App):

    def click1(self, event):
        self.pantalla.text = "El perro te mira, contento."

    def click2(self, event):
        self.pantalla.text = "El perro te muerde."

    def click3(self, event):
        self.pantalla.text = "El perro te ignora."

    def click4(self, event):
        if self.opcion4.text == "Ocultar botones":
            self.old_y_1 = self.opcion1.y
            self.opcion1.y = 1000
            self.old_y_2 = self.opcion2.y
            self.opcion2.y = 1000
            self.old_y_3 = self.opcion3.y
            self.opcion3.y = 1000
            self.opcion4.text = "Mostrar botones"
        else:
            self.opcion1.y = self.old_y_1
            self.opcion2.y = self.old_y_2
            self.opcion3.y = self.old_y_3
            self.opcion4.text = "Ocultar botones"

    def build(self):

        layout = GridLayout(cols = 1)

        self.pantalla = Label(text = "Encuentras un perro.")
        layout.add_widget(self.pantalla)

        self.opcion1 = Button(text = "Le acaricias", size_hint_y = None, height = 50, on_press = self.click1)
        layout.add_widget(self.opcion1)

        self.opcion2 = Button(text = "Le pegas", size_hint_y = None, height = 50, on_press = self.click2)
        layout.add_widget(self.opcion2)

        self.opcion3 = Button(text = "Le ignoras", size_hint_y = None, height = 50, on_press = self.click3)
        layout.add_widget(self.opcion3)

        self.opcion4 = Button(text = "Ocultar botones", size_hint_y = None, height = 50, on_press = self.click4)
        layout.add_widget(self.opcion4)

        return layout

if __name__ == '__main__':
    Juego().run()
