from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivymd.uix.list import ThreeLineListItem,MDList,ThreeLineIconListItem,IconLeftWidget,ImageLeftWidget,ThreeLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.datatables import MDDataTable
from kivy.factory import Factory

Window.size=(300,520)
Builder.load_file('Bar_drawer.kv')

class Root(Widget):
    pass
class DemoApp(MDApp):
    title = "MY APP"
    def build(self):
        #self.theme_cls.primary_palette='Red'
        #screen=Builder.load_string(help)
        return Root()
    def menu_click(self):
        print('hello....')
    def toggle_nav_drawer(self):
        pass

DemoApp().run()