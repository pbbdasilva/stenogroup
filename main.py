from kivy.app import App
from kivy.app import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput


class PaginaInicial(Screen):
    pass


class SegundaPagina(Screen):
    pass


class ScreenManagement(ScreenManager):
    def switch_to_segundaPagina(self):
        self.current = 'segundaPagina'

    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'



class kivyWizardApp(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root




if __name__ == '__main__':
    kivyWizardApp().run()