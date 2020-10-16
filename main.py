from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
import mysql.connector
Window.clearcolor = (0.5, 0.1, 0.5, 1)

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
                MainWindow.current = self.email.text
                self.reset()
                sm.current = "main"
                t = 1
                break

        if t == 0:
            invalidLogin()

    def reset(self):
        self.email.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Usuário Inválido'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()



