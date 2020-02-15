from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder


class MainPanel(TabbedPanel):
    pass


class FauxnApp(App):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    FauxnApp().run()
