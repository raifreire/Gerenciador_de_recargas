from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp #display pixels
import sqlite3
from datetime import datetime

class GerenciarTelas(ScreenManager):
    pass
class Home(Screen):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("db.kv")
    
    #create Databse Or Connect to one
    conn = sqlite3.connect("database.db")

    #create a cursor
    c = conn.cursor()

    #create table
    c.execute("""CREATE TABLE IF NOT EXISTS customers(
        number text, 
        ultima_recarga text,
        data_hora text)""")

    #commit changes
    conn.commit()

    #close connection
    conn.close()
    
    def submit(self):
        #create Databse Or Connect to one
        conn = sqlite3.connect("database.db")

        #create a cursor
        c = conn.cursor()
        #add data to the table
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO customers VALUES (:number, :ultima_recarga, :data_hora)",
                  {
                      'number': self.root.ids.word_input.text,
                      'ultima_recarga': self.root.ids.word2_input.text,
                      'data_hora': data_hora
                  })
        #Add a little message
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text} added"
        self.root.ids.word2_label.text = f"{self.root.ids.word2_input.text} \nadded at: {data_hora}"

        #clear input
        self.root.ids.word_input.text = ""
        self.root.ids.word2_input.text = ""

        #commit changes
        conn.commit()

        #close connection
        conn.close()

    def show_records(self):
        #create Databse Or Connect to one
        conn = sqlite3.connect("database.db")

        #create a cursor
        c = conn.cursor()

        #Grab records from database
        c.execute("""SELECT * FROM customers""")
        records = c.fetchall()
        word = ''

        #loop through results
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        #commit changes
        conn.commit()

        #close connection
        conn.close()

    
MainApp().run()