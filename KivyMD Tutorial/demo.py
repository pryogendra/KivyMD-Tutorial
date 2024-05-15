from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

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
class DemoApp(MDApp):
    title = "MY APP"
    def build(self):
        screen=Screen()
        self.theme_cls.primary_palette="Blue"  #change the whole colors
        #self.theme_cls.primary_hue='A700' # color brightness
        self.theme_cls.theme_style="Dark" #Dark theme
        label=MDLabel(text="Hello",halign='center',theme_text_color='Custom',text_color=(1,0,1,1),
                      font_style='Button')
        icon_label=MDIcon(icon='language-python',halign='center')
        button=MDFlatButton(text="Hello World",pos_hint={'center_x':0.5,'center_y':0.5})
        button2=MDRectangleFlatButton(text="Hello World",pos_hint={'center_x':0.5,'center_y':0.5})
        button_icon=MDIconButton(icon="android",pos_hint={'center_x':0.5,'center_y':0.5})
        button_icon2=MDFloatingActionButton(icon="language-python",pos_hint={'center_x':0.5,'center_y':0.5})
        #username1=MDTextField(text="Enter username",pos_hint={'center_x':0.5,'center_y':0.5},size_hint_x=None,width=300)
        username=Builder.load_string(user_helper)
        screen.add_widget(username)
        return screen

DemoApp().run()