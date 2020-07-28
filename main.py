from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import json
import datetime

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MyApp(MDApp):
    with open('data.json') as f:
        data = json.loads(f.read())

    def write_to_file(self):
        with open('data.json', 'w') as f:
            f.write(json.dumps(self.data))

    def save_settings(self, instance):
        pass
        if self.root.ids.five.active:
            self.data["botles"] = 300
        if self.root.ids.three.active:
            self.data["botles"] = 500
        if self.root.ids.seven.active:
            self.data["botles"] = 214
        """if self.root.ids.counter.active:
            self.data["counter"] = True
        else:
            self.data["counter"] = False"""
        self.write_to_file()
        self.root.ids.label1.text = f"Botles drunk: {self.data['drunk']}"
        self.root.ids.label2.text = f"Botles left: {self.data['botles']-self.data['drunk']}"
        self.root.ids.screen_manager.current = "main"

    def reset_result(self):
        self.data['drunk'] = 0
        self.write_to_file()

        self.root.ids.label1.text = f"Botles drunk: {self.data['drunk']}"
        self.root.ids.label2.text = f"Botles left: {self.data['botles']-self.data['drunk']}"

    def add_to_result(self):
        if self.data['botles'] - self.data['drunk'] > 0:
            self.data['drunk'] += 1
            self.data[str(self.data['day'])] += 1
            self.write_to_file()

            if self.data['day']==1:
                self.root.ids.mon.text = f"Monday: {self.data['1']}"
            elif self.data['day']==2:
                self.root.ids.tue.text = f"Tuesday: {self.data['2']}"
            elif self.data['day']==3:
                self.root.ids.wed.text = f"Wednesday: {self.data['3']}"
            elif self.data['day']==4:
                self.root.ids.thu.text = f"Thursday: {self.data['4']}"
            elif self.data['day']==5:
                self.root.ids.fri.text = f"Friday: {self.data['5']}"
            elif self.data['day']==6:
                self.root.ids.sat.text = f"Saturday: {self.data['6']}"
            else:
                self.root.ids.sun.text = f"Sunday: {self.data['7']}"
            self.root.ids.label.text = f"Today botles: {self.data[str(self.data['day'])]}"
            self.root.ids.label1.text = f"Botles drunk: {self.data['drunk']}"
            self.root.ids.label2.text = f"Botles left: {self.data['botles']-self.data['drunk']}"

        else:
            pop = Popup(title='Filter info', content=Label(text="It\'s time to change filter!"),size_hint=(.7,.7))
            pop.open()

    def build(self):
        return

    def on_start(self):
        self.day = datetime.datetime.now().weekday()
        if self.data["day"]!=self.day+1:
            self.data["day"]=self.day+1
            self.write_to_file()
        if self.data['day']==1 and self.data[str(self.day+1)]>0 and self.data[str(self.day+2)]>0:
            for i in range(1,8):
                self.data[str(i)]=0
            self.write_to_file()

        #self.root.ids.screen_manager.current="settings"

MyApp().run()
