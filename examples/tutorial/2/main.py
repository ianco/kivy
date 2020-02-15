from kivy.app import App
from kivy.uix.button import Button
from functools import partial
 
class KivyButton(App):
    
    def disable(self, instance, *args):
        instance.disabled = True
 
    def update(self, instance, *args):
        instance.text = "I am Disabled!"

    def build(self):
        mybtn = Button(text="Welcome to LikeGeeks!", pos=(300,350), size_hint = (.25, .18))
        mybtn.bind(on_press=partial(self.disable, mybtn))
        mybtn.bind(on_press=partial(self.update, mybtn))
        return mybtn
    
if __name__ == '__main__':
    KivyButton().run()
