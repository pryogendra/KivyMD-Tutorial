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

user_helper="""
MDTextField:
    hint_text:"Enter Username :"
    helper_text:"username is case sensitive"
    #helper_text_mode:'persistent'
    helper_text_mode:'on_focus'
    icon_right:'android'
    icon_right_color:app.theme_cls.primary_palette
    #icon_left:'android'
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300
"""

class Root(Widget):
    pass
class DemoApp(MDApp):
    title = "MY APP"
    def build(self):
        screen=Screen()
        datatables=MDDataTable(check=True,
                               rows_num=4,
                               use_pagination=True,
            column_data=[
            ('Food',dp(30)),
            ('Calories',dp(30)),
            ('Location',dp(30)),
        ],row_data=[
            ('Milk',123,'Mumbai'),
            ('Burger',13,'Lucknow'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
            ('Pizza',12,'pune'),
        ])
        datatables.bind(on_check_press=self.check_press)
        datatables.bind(on_row_press=self.row_press)
        screen.add_widget(datatables)

        return screen
    def check_press(self,instance_table,current_row):
        print(current_row)
    def row_press(self,instance_table,instance_row):
        print(instance_table,instance_row)

DemoApp().run()