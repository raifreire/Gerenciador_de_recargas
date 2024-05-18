from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class Menu(Screen):
    pass

class CreateWindow(Screen):
    pass

class NewRegister(Screen):
    pass

class BeforeOfCreateWindow(Screen):
    pass

class Manager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        # Carrega o arquivo KV
        Builder.load_file('telas.kv')
        root_widget = Manager()
        print("Root widget:", root_widget)
        return root_widget

    def submit(self, word_input_text, word2_input_text):
        print(f"Numero: {word_input_text}")
        print(f"Ultima Recarga: {word2_input_text}")

if __name__ == '__main__':
    MyApp().run()
