'''import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3
import os
from datetime import datetime


class MeuAplicativo(App):
    def build(self):
        # Criar layout principal
        layout_principal = BoxLayout(orientation='vertical')

        # Criar rótulo para nome
        rotulo_nome = Label(text='Nome:')
        layout_principal.add_widget(rotulo_nome)

        # Criar campo de entrada para nome
        campo_nome = TextInput()
        layout_principal.add_widget(campo_nome)

        # Criar rótulo para email
        rotulo_email = Label(text='Email:')
        layout_principal.add_widget(rotulo_email)

        # Criar campo de entrada para email
        campo_email = TextInput()
        layout_principal.add_widget(campo_email)

        # Criar botão para enviar
        botao_enviar = Button(text='Enviar')
        botao_enviar.bind(on_press=self.enviar_dados)
        layout_principal.add_widget(botao_enviar)

        return layout_principal
    
     #create Databse Or Connect to one
    conn = sqlite3.connect("my_database.db")

    #create a cursor
    c = conn.cursor()

    #create table
    c.execute("""CREATE TABLE IF NOT EXISTS contatos(
        number text,
        ultima_recarga text,
        data_hora text)""")

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    def enviar_dados(self, instance):
        # Obter dados do formulário
        nome = self.campo_nome.text
        email = self.campo_email.text

        # Validar dados (opcional)

        # Conectar ao banco de dados
        conexao = sqlite3.connect('my_database.db')
        cursor = conexao.cursor()

        # Preparar consulta SQL para inserir dados
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        consulta = """
            INSERT INTO contatos (number, ultima_recarga, data_hora)
            VALUES (?, ?, ?)
        """

        # Executar consulta e inserir dados
        cursor.execute(consulta, (nome, email, data_hora))
        conexao.commit()

        # Fechar conexão com o banco de dados
        conexao.close()

        # Mostrar mensagem de sucesso
        alert = kivy.uix.popup.Popup(title='Dados enviados!',
                                      content=Label(text='Os dados foram enviados com sucesso!'),
                                      size_hint=(0.8, 0.3))
        alert.open()

        # Limpar campos do formulário
        self.campo_nome.text = ''
        self.campo_email.text = ''

MeuAplicativo().run()'''