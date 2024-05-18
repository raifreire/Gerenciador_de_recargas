from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
'''ObjectProperty - Ao criar varias telas não consigo acessar o elemento root
pela classe principal, a funcionalidade ObjectProperty ajuda a repassar os 
elementos necessario de classe que possui o elemento root para as outras...'''
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout  # Importar o GridLayout
from kivy.uix.boxlayout import BoxLayout #Importar BoxLayout
from kivy.uix.label import Label  # Importar o módulo Label
from kivy.core.window import Window
import json
import sqlite3
from datetime import datetime

Window.size = (500, 500)

class Manager(ScreenManager):
    pass

class BeforeOfCreateWindow(Screen):
    pass  

class Menu(Screen):
    '''Classe que representa a tela de menu'''
    def checkStatus(self):    
        try:
            with open('status.json','r') as fileJson:
                contentFile = json.load(fileJson)
        except:
            with open("status.json", "w") as fileJson:
                contentFile = {'Status': 1}
                json.dump(contentFile, fileJson)

        if contentFile['Status'] == 1:
            MDApp.get_running_app().root.transition.direction = "left"
            MDApp.get_running_app().root.current = "beforeofcreatewindow"

class CreateWindow(Screen):
    pass

class NewRegister(Screen):
    word_input = ObjectProperty(None)
    word2_input = ObjectProperty(None)

class DisplayWindow(Screen):
    '''Classe que representa a tela de exibição dos registros'''
    def on_enter(self, *args):
        self.display_records()

    def display_records(self):
        # Conecta ao banco de dados
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        
        # Recupera os registros
        c.execute("SELECT * FROM registers")
        records = c.fetchall()
        
        # Fecha a conexão
        conn.close()
        
        # Atualiza a interface com os registros
        records_table = self.ids.records_table
        records_table.clear_widgets()
        
        # Adicionando cabeçalhos
        headers = ["Numero", "Ultima Recarga", "Data/Hora"]
        for header in headers:
            records_table.add_widget(Label(text=header, bold=True, color=(0, 0, 0, 1)))
        
        for record in records:
            for field in record:
                records_table.add_widget(Label(text=str(field), color=(0, 0, 0, 1)))

    # def show_records(self):
    #     '''Função utilizada anteriormente para repassar os resultados, em formato 
    #     Str() para um label de teste...'''
    #     #create Databse Or Connect to one
    #     conn = sqlite3.connect("data.db")

    #     #create a cursor
    #     c = conn.cursor()

    #     #Grab records from database
    #     c.execute("""SELECT * FROM registers""")
    #     records = c.fetchall()
    #     word = ''

    #     #loop through results
    #     for record in records:
    #         print(record)
    #         word = f'{word}\n{record[2]}'
    #         self.ids.data_label.text = word

    #     #commit changes
    #     conn.commit()

    #     #close connection
    #     conn.close()

class MyApp(MDApp):
    '''Classe principal do aplicativo'''
    def build(self):
        # Carrega o arquivo KV
        self.root = Builder.load_file('tela.kv')
        return self.root

    def submit(self, word_input_text, word2_input_text):
        # Conecta ao banco de dados
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        
        # Adiciona dados à tabela
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO registers (number, ultima_recarga, data_hora) VALUES (?, ?, ?)",
                  (word_input_text, word2_input_text, data_hora))
        
        # Limpa os campos de input
        new_register_screen = self.root.get_screen('newregister')
        new_register_screen.ids.word_input.text = ''
        new_register_screen.ids.word2_input.text = ''
        
        # Comita mudanças e fecha conexão
        conn.commit()
        conn.close()

if __name__ == '__main__':
    MyApp().run()
