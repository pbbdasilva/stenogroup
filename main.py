from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import mysql.connector
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
import os

main_path = "./imagens"


class LoginWindow(Screen):
    email = ObjectProperty(None)

    def loginBtn(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="gugugustavo9",
            database="gg",
        )
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT name FROM users")
        t = 0
        for name in my_cursor:
            if self.email.text == name[0]:
                Biblioteca.current = self.email.text
                self.reset()
                sm.current = "main"
                t = 1
                break

        if t == 0:
            invalidLogin()

    def reset(self):
        self.email.text = ""



class Biblioteca(Screen):
    n = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""


    def logOut(self):
        sm.current = "login"


    def VerLivros(self):
        for root, subFolder, filename in os.walk(main_path):
            for uniqueFile in filename:
                texto = "imagens/" + uniqueFile
                self.ids.box.add_widget(ImageButton(source=texto))
    def RemoverLivros(self):
        self.ids.box.clear_widgets()



class titulo(Label):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class Texto(Screen):
    pass

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Usuário Inválido'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), Biblioteca(name="main"), Texto(name="tex")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"



class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()