from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivymd.uix.list import ThreeLineListItem,MDList,ThreeLineIconListItem,IconLeftWidget,ImageLeftWidget,ThreeLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView

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
        #self.theme_cls.theme_style="Dark" #Dark theme
        button=MDRectangleFlatButton(text="SHOW",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                     on_release=self.clicked
                                     )
        self.username=Builder.load_string(user_helper)
        #screen.add_widget(self.username)
        #screen.add_widget(button)
        #return screen
        list_view=MDList()
        scroll=ScrollView()
        scroll.add_widget(list_view)
        for i in range(1,30):
            icon = IconLeftWidget(icon='android')
            #image = ImageLeftWidget(source='image.jpg')   #for using image as icon
            item=ThreeLineIconListItem(text='item '+str(i),secondary_text="Second line",tertiary_text='Third line')
            #item=ThreeLineAvatarIconListItem(text='item '+str(i),secondary_text="Second line",tertiary_text='Third line')  #for image as icon
            item.add_widget(icon)
            #item.add_widget(image)
            list_view.add_widget(item)
        screen.add_widget(scroll)
        return screen







    def clicked(self,obj):
        if self.username.text=="":
            check_string='Please enter Username'
        else:
            check_string=self.username.text+' not exists'
        close=MDFlatButton(text='Close',on_release=self.close_dialog)
        more=MDFlatButton(text='More')
        self.dialog=MDDialog(title='Username Check ',text=check_string,size_hint=(0.5,1),
                        buttons=[close,more])
        #print(self.username.text)
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

DemoApp().run()