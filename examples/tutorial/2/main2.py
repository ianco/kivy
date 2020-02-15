from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

#Builder.load_string("""
#<KivyButton>:
#    Button:
#        text: "Hello Button!"
#        size_hint: .12, .12
#        Image:
#            source: 'kivy.jpg'
#            center_x: self.parent.center_x
#            center_y: self.parent.center_y  
#""")

Builder.load_file("main2.kv")

class KivyButton(App, BoxLayout):
    
    def build(self):
        return self
    
if __name__ == '__main__':
    KivyButton().run()
