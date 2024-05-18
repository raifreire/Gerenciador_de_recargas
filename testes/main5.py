'''from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import json

Window.size = (300, 500)

class Manager(ScreenManager):
    pass

class BeforeOfCreateWindow(Screen):
   pass  
class Menu(Screen):
    def checkStatus(self):    
        try:
            with open('status.json','r') as fileJson:
                contentFile = json.load(fileJson)
        except:
            with open("status.json", "w") as fileJson:
                contentFile = {'Status': 1}
                json.dump(contentFile, fileJson)

        if contentFile['Status'] == 1:
            App.get_running_app().root.transition.direction = "left"
            App.get_running_app().root.current = "beforeofcreatewindow"


class CreateWindow(Screen):
    pass
      

class NewRegister(Screen):
    pass   
        

class MyApp(App):
    def build(self):
        return Manager()
    


MyApp().run()'''