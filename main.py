from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.lang import Builder

# Load the KV file
Builder.load_file('kv/main.kv')

class MyBoxLayout(BoxLayout):
    def on_button1_click(self):
        print("Button 1 clicked!")

    def on_button2_click(self):
        print("Button 2 clicked!")

class MyKivyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyKivyApp().run()
