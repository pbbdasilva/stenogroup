from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


with open('1984.txt', 'r', errors='ignore') as livro:
    label = livro.read()


class Controller(FloatLayout):
    cont = 3000 
    label = label[0:cont]

    m = 0

    def next_page(self):
        self.m = self.m + 1
        print(self.m)
        self.label_wid.text = label[self.cont*self.m:self.cont*(self.m+1)]
        self.pagenum.hint_text = str(self.m + 1)
        self.pagenum.text = str(self.m + 1)

    def last_page(self):
        self.m = self.m - 1
        print(self.m)
        self.label_wid.text = label[self.cont*self.m:self.cont*(self.m+1)]
        self.pagenum.hint_text = str(self.m + 1)
        self.pagenum.text = str(self.m + 1)

    def page(self):
        self.m = int(self.pagenum.text) - 1
        self.label_wid.text = label[self.cont * self.m:self.cont * (self.m + 1)]
        print(self.m)
        self.pagenum.hint_text = str(self.m + 1)
        self.pagenum.text = str(self.m + 1)

class ControllerApp(App):

    def build(self):
        return Controller()

if __name__ == '__main__':
    ControllerApp().run()