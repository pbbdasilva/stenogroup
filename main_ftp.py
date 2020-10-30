from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import ftplib


class Controller(FloatLayout):
    ftp = None

    def ftp_connect(self, button_id):

        self.ftp = ftplib.FTP(host='192.168.4.1')
        self.ftp.set_debuglevel(2)
        self.ftp.login('pi','honeyimehome')
        self.ftp.cwd('/files/')
        with open('teste.txt', 'wb') as fp:
            self.ftp.retrbinary('RETR teste.txt', fp.write)


class ControllerApp(App):
    def build(self):
        return Controller()


if __name__ == "__main__":
    ControllerApp().run()
