from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import ftplib
from kivy.utils import platform


if platform == "android":
    from android.permissions import request_permissions, Permission
    from android.storage import primary_external_storage_path
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])
    direc = primary_external_storage_path()
    download_dir_path = os.path.join(direc, 'steno_dir')
else:
    download_dir_path = os.path.join('.', 'steno_dir')


main_path = os.path.join(download_dir_path, 'imagens')

class WindowManager(ScreenManager):
    pass

class LoginWindow(Screen):
    pass

class Menu(Screen):
    ftp = None

    def ftp_connect(self, button_id):
        self.ftp = ftplib.FTP(host='192.168.4.1')
        self.ftp.set_debuglevel(2)
        self.ftp.login('pi', 'honeyimehome')
        self.ftp.cwd('/files/livros')
        os.chdir(download_dir_path)
        with open('1984.txt', 'wb') as fp:
            self.ftp.retrbinary('RETR 1984.txt', fp.write)
        os.chdir(os.path.join(download_dir_path, 'imagens'))
        with open('1984.jpg', 'wb') as fp:
            self.ftp.retrbinary('RETR 1984.jpg', fp.write)

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



class ImageButton(ButtonBehavior, Image):
    pass


class Texto(Screen):
    cont = 2120
    m = 0
    label = ''
    try:
        with open(os.path.join(download_dir_path, "1984.txt"), 'r', errors='ignore') as livro:
            livro_todo = livro.read()
        if m == 0:
            # aqui é a primeira página
            label = livro_todo[m:cont]
        def next_page(self):
            self.m = self.m + 1
            self.label = self.livro_todo[self.m*self.cont:(self.m + 1)*self.cont]
            self.label_wid.text = self.label
            self.pagenum.hint_text = str(self.m + 1)
            self.pagenum.text = str(self.m + 1)

        def last_page(self):
            self.m = self.m - 1
            self.label = self.livro_todo[self.m * self.cont:(self.m + 1) * self.cont]
            self.label_wid.text = self.label
            self.pagenum.hint_text = str(self.m + 1)
            self.pagenum.text = str(self.m + 1)

        def page(self):
            self.m = int(self.pagenum.text) - 1
            self.label = self.livro_todo[self.m * self.cont:(self.m + 1) * self.cont]
            self.label_wid.text = self.label
            self.pagenum.hint_text = str(self.m + 1)
            self.pagenum.text = str(self.m + 1)
    except FileNotFoundError:
        pass




kv = Builder.load_file("v4.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), Menu(name="menu"), Biblioteca(name="main"), Texto(name="tex")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"



class v4(App):
    def build(self):
        self.icon = 'logo/logo.png'
        return sm


if __name__ == "__main__":
    v4().run()
