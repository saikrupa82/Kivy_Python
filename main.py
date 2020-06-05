from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
import csv
import database as dbp
db = dbp.DataBase_Login("users.txt")
dbd=dbp.DataBase_Files("PlotFiles.txt")
class PlotWindow(Screen):
    plotno=ObjectProperty(None)
    surno=ObjectProperty(None)
    nosy=ObjectProperty(None)
    ownername=ObjectProperty(None)
    remarks=ObjectProperty(None)    
    document=ObjectProperty(None)    
    addressofplot=ObjectProperty(None)    
    buyername=ObjectProperty(None) 
    current = ""

    def PlotDetails(self):
        if self.plotno.text!="" and self.surno.text!="" and self.nosy.text!="" and self.ownername.text!="" and self.document.text!="" and self.addressofplot.text!="" and self.buyername.text!="":
            dbd.add_Data(self.current,self.plotno.text,self.surno.text,self.nosy.text,self.ownername.text,self.document.text,self.buyername.text,self.addressofplot.text,self.remarks.text )
            popup = Popup(title='Document Saved', content=Label(text='Document Has been saved in DataBase'),
                    size_hint=(None, None), size=(400, 400))
            self.reset()
    def reset(self):
        self.plotno.text=""
        self.surno.text=""
        self.nosy.text=""
        self.ownername.text=""
        self.document.text=""
        self.buyername.text=""
        self.addressofplot.text=""
        self.remarks.text=""
class LoginWindow(Screen):
    username = ObjectProperty(None)
    passw = ObjectProperty(None)
    def Login(self):
        
        if db.validate(self.username.text,self.passw.text):  
            popup = Popup(title='Congralations', content=Label(text='Logined in '),
            size_hint=(None, None), size=(400, 400))
            PlotWindow.current = self.username.text
            popup.open()
            self.manager.current="PlotInfo"
        else:
            invalidForm()

def invalidForm():
        popup = Popup(title='Error', content=Label(text='Check with the Input given'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

def build(self):
        box = BoxLayout()
        box.add_widget(Label(text='Registration Completed'))
        box.add_widget(Button(Text="Back"))
        popup = Popup(title='Test popup', content=box, size_hint=(None, None), size=(400, 400))
        return popup


def Registration_Done():
    popup = Popup(title='Registration Saved', content=Label(text='Registration successful'),
                size_hint=(None, None), size=(400, 400))
    popup.open()
    b=Button(text="Back")


class NewUserWindow(Screen):
    username = ObjectProperty(None)
    passw = ObjectProperty(None)
    phonenumber = ObjectProperty(None)
    email_ID = ObjectProperty(None)
    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text='Registration Completed'))
        box.add_widget(Button(text="Back",size_hint=(.6,.25),pos_hint={'x':0.2},on_press = self.popup_exit.dismiss))
        popup = Popup(title='Test popup', content=box, size_hint=(None, None), size=(400, 400))
        return popup

    def Register(self):
        if self.username.text != "" and self.passw.text != "" and self.email_ID.text.count("@") == 1 and self.email_ID.text.count(".") > 0 and len(self.phonenumber.text) > 9 and self.passw != "":
                db.add_user(self.username.text, self.passw.text, self.phonenumber.text, self.email_ID.text)
                self.reset()
        else:
            invalidForm()
                

    def reset(self):
        self.email_ID.text = ""
        self.passw.text = ""
        self.username.text = ""
        self.phonenumber.text = ""



class WindowsManager(ScreenManager):
    pass

sm = WindowsManager()

class MyApp(App):
    def build(self):
        return Builder.load_file('Kivy_kv.kv')


if __name__ == "__main__":
    MyApp().run()
