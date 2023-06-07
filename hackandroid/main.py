import requests
from typing import Any
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import *
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import *
from kivy.core.window import Window
from kivymd.uix.floatlayout import *
from kivymd.uix.gridlayout import * 
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import *
from kivymd.uix.textfield import *
from kivymd.uix.button import *
from kivymd.uix.navigationdrawer import *
from kivymd.uix.selectioncontrol import * 
from kivymd.uix.scrollview import *
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import *
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (380, 700)


class Sign_in(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self):
        self.layout = MDFloatLayout()

        anim1 = Animation(pos_hint = {"center_x":.83, "center_y":.85}, opacity = 1)
        anim2 = Animation(pos_hint = {'center_x':.5, 'center_y':.65}, opacity = 1)
        anim3 = Animation(pos_hint = {'center_x':.5, 'center_y':.5}, opacity = 1)
        anim4 = Animation(pos_hint = {'center_x':.5, 'center_y':.35}, opacity = 1)
        anim5 = Animation(pos_hint = {'center_x':.5, 'center_y':.25}, opacity = 1)

        text_sign_in = MDLabel()
        text_sign_in.text = 'Вход'
        text_sign_in.font_size = 75
        text_sign_in.pos_hint = {"center_x":.83, "center_y":1}
        text_sign_in.opacity = .5

        anim1.start(text_sign_in)

        self.text_error = MDLabel()
        self.text_error.pos_hint = {"center_x":.6, "center_y":.75}

        self.input_name = MDTextField()
        self.input_name.size_hint_max_x = 300
        self.input_name.hint_text = 'Билеть'
        self.input_name.font_size = 25
        self.input_name.pos_hint = {'center_x':.3, 'center_y':.65}
        self.input_name.mode = "rectangle"
        self.input_name.line_color_focus = '#008000'
        self.input_name.text_color_focus = '#008000'
        self.input_name.hint_text_color_focus = '#008000'
        self.input_name.opacity = .5

        anim2.start(self.input_name)

        self.input_pass = MDTextField()
        self.input_pass.size_hint_max_x = 300
        self.input_pass.hint_text = 'Пароль'
        self.input_pass.font_size = 25
        self.input_pass.pos_hint = {'center_x':.7, 'center_y':.5}
        self.input_pass.mode = "rectangle"
        self.input_pass.line_color_focus = '#008000'
        self.input_pass.text_color_focus = '#008000'
        self.input_pass.hint_text_color_focus = '#008000'
        self.input_pass.opacity = .5

        anim3.start(self.input_pass)

        btn_sign_in = MDFillRoundFlatButton()
        btn_sign_in.text = 'Вход'
        btn_sign_in.md_bg_color = '#008000'
        btn_sign_in.font_size = 30
        btn_sign_in.pos_hint = {'center_x':.4, 'center_y':.35}
        btn_sign_in.on_press = self.func_sign_in
        btn_sign_in.opacity = .5

        anim4.start(btn_sign_in)

        btn_sign_up = MDFillRoundFlatButton()
        btn_sign_up.text = 'Авторизация'
        btn_sign_up.md_bg_color = '#556B2F'
        btn_sign_up.font_size = 30
        btn_sign_up.pos_hint = {'center_x':.7, 'center_y':.25}
        btn_sign_up.on_press = self.func_sign_up
        btn_sign_up.opacity = .5

        anim5.start(btn_sign_up)

        self.layout.add_widget(text_sign_in)
        self.layout.add_widget(self.text_error)
        self.layout.add_widget(self.input_name)
        self.layout.add_widget(self.input_pass)
        self.layout.add_widget(btn_sign_in)
        self.layout.add_widget(btn_sign_up)

        self.add_widget(self.layout)

    def func_sign_in(self):
        if self.input_name.text != '' and self.input_pass.text != '':
            url = f'http://127.0.0.1:8000/sign_in/{self.input_name.text}/{self.input_pass.text}'
            data = requests.get(url).json()
            if data["sign_in"] == True:
                sm.sm.current = 'menu'
            elif data["sign_in"] == False:
                self.text_error.opacity = .5
                self.text_error.text = 'Вы вели неверный номер или пароль'
                self.text_error.color = '#FF0000'
        elif self.input_name.text == '':
            self.input_name.focus = True
        elif self.input_pass.text == '':
            self.input_pass.focus = True 

    def func_sign_up(self):
        sm.sm.current = 'sign_up'

    def on_leave(self, *args):
        self.layout.clear_widgets()


class Sign_up(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def on_enter(self):
        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'

        self.layout = MDGridLayout()
        self.layout.cols = 1
        self.layout.col_force_default = False
        self.layout.spacing = dp(40) 
        self.layout.size_hint = (1, None)
        self.layout.adaptive_height = True
        self.layout.padding = dp(75)

        text_sign_up = MDLabel()
        text_sign_up.text = 'Авторизация'
        text_sign_up.font_size = 48

        self.text_error = MDLabel()
        self.text_error.text = ''

        self.input_name = MDTextField()
        self.input_name.hint_text = 'Имя'
        self.input_name.font_size = 25
        self.input_name.mode = "rectangle"
        self.input_name.line_color_focus = '#008000'
        self.input_name.text_color_focus = '#008000'
        self.input_name.hint_text_color_focus = '#008000'

        self.input_first = MDTextField()
        self.input_first.hint_text = 'Фамилия'
        self.input_first.font_size = 25
        self.input_first.mode = "rectangle"
        self.input_first.line_color_focus = '#008000'
        self.input_first.text_color_focus = '#008000'
        self.input_first.hint_text_color_focus = '#008000'

        self.input_gmail = MDTextField()
        self.input_gmail.hint_text = 'Gmail'
        self.input_gmail.font_size = 25
        self.input_gmail.mode = "rectangle"
        self.input_gmail.line_color_focus = '#008000'
        self.input_gmail.text_color_focus = '#008000'
        self.input_gmail.hint_text_color_focus = '#008000'

        self.input_read_bilet = MDTextField()
        self.input_read_bilet.hint_text = 'Читательский билет'
        self.input_read_bilet.font_size = 25
        self.input_read_bilet.mode = "rectangle"
        self.input_read_bilet.line_color_focus = '#008000'
        self.input_read_bilet.text_color_focus = '#008000'
        self.input_read_bilet.hint_text_color_focus = '#008000'

        self.input_pass = MDTextField()
        self.input_pass.hint_text = 'Пароль'
        self.input_pass.font_size = 25
        self.input_pass.mode = "rectangle"
        self.input_pass.line_color_focus = '#008000'
        self.input_pass.text_color_focus = '#008000'
        self.input_pass.hint_text_color_focus = '#008000'

        self.input_kyrs = MDTextField()
        self.input_kyrs.hint_text = 'Курс'
        self.input_kyrs.font_size = 25
        self.input_kyrs.max_text_length = 1
        self.input_kyrs.mode = "rectangle"
        self.input_kyrs.line_color_focus = '#008000'
        self.input_kyrs.text_color_focus = '#008000'
        self.input_kyrs.hint_text_color_focus = '#008000'

        self.btn_sign_up = MDFillRoundFlatButton()
        self.btn_sign_up.text = 'Авторизация'
        self.btn_sign_up.md_bg_color = '#008000'
        self.btn_sign_up.font_size = 30
        self.btn_sign_up.on_press = self.func_sign_up
        self.btn_sign_in = MDFillRoundFlatButton()
        self.btn_sign_in.text = 'Вход'
        self.btn_sign_in.md_bg_color = '#556B2F'
        self.btn_sign_in.font_size = 30
        self.btn_sign_in.on_press = self.func_sign_in

        self.layout.add_widget(text_sign_up)
        self.layout.add_widget(self.text_error)
        self.layout.add_widget(self.input_name)
        self.layout.add_widget(self.input_first)
        self.layout.add_widget(self.input_gmail)
        self.layout.add_widget(self.input_read_bilet)
        self.layout.add_widget(self.input_pass)
        self.layout.add_widget(self.input_kyrs)
        self.layout.add_widget(self.btn_sign_up)
        self.layout.add_widget(self.btn_sign_in)

        self.scroll.add_widget(self.layout)

        self.add_widget(self.scroll)

    def func_sign_up(self):
        name = self.input_name.text
        first = self.input_first.text
        gmail = self.input_gmail.text
        read = self.input_read_bilet.text
        passw = self.input_pass.text
        kyrs = self.input_kyrs.text
        if name != '' and first != '' and gmail != '' and read != '' and passw != '' and kyrs != '':
            url = f'http://127.0.0.1:8000/sign_up/{name}/{first}/{gmail}/{read}/{passw}/{kyrs}'
            data = requests.get(url).json()
            if data["sign_up"] == True:
                sm.sm.current = 'sign_in'
            else:
                self.text_error.text = f'{data["sign_up"]}'
                self.text_error.color = "#FF0000"
                self.text_error.opacity = .5
                print(data["sign_up"])

    def func_sign_in(self):
        sm.sm.current = 'sign_in'

    def on_leave(self, *args):
        self.scroll.clear_widgets()


class Magnify(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self):

        animation = Animation(pos_hint = {'center_y':.06, 'center_x':.5}, opacity = 1)
        animation1 = Animation(opacity = 1, pos_hint = {"center_y":.46, 'center_x':.5})
        animation2 = Animation(pos_hint = {'center_y':.95, 'center_x':.5}, opacity = 1)

        self.layout = MDFloatLayout()

        self.navbar = MDFloatLayout()
        self.navbar.md_bg_color = '#008000'
        self.navbar.radius = (25, 25, 25, 25)
        self.navbar.size_hint_max_y = 80
        self.navbar.pos_hint = {'center_y':.03, 'center_x':.03}
        self.navbar.opacity = .5

        self.search_layout = MDFloatLayout()
        self.search_layout.size_hint_max_y = 100
        #self.search_layout.md_bg_color = '#008000'
        self.search_layout.pos_hint = {'center_y':.90, 'center_x':.03}
        self.search_layout.opacity = .5


        animation.start(self.navbar)
        animation2.start(self.search_layout) 

        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'
        self.scroll.pos_hint = {"center_y":.4, 'center_x':.4}
        self.scroll.opacity = .5

        animation1.start(self.scroll)

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.spacing = 40
        self.card_layout.size_hint = (1, None)
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 75
        self.card_layout.pos_hint = {"center_y":.0, 'center_x':.3}
        self.card_layout.opacity = .5
        

        self.card = MDCard()
        self.card.focus_behavior = True
        self.card.focus_color = '#009988'
        self.card.line_color=(0.2, 0.2, 0.2, 0.8)
        self.card.style = 'elevated'
        self.card.padding = "4dp"
        self.card.size_hint = (None, None)
        self.card.size = ("250dp", "450dp")
        self.card.unfocus_color = "#008000"
        self.card.md_bg_color = "#008000"
        self.card.shadow_softness = 2
        self.card.shadow_offset = (0, 1)

        animation.start(self.card_layout)
        
        self.reval = MDRelativeLayout()
        
        self.image = AsyncImage()
        self.image.source = "https://images4.alphacoders.com/766/thumb-1920-766744.jpg"
        #"https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg" 
        #'http://fotorelax.ru/wp-content/uploads/2017/03/Mesmerizing-nature-photography-by-Eric-Bunting-24.jpg'
        self.image.size_hint = (None, None)
        self.image.size = (363, 250)
        self.image.pos_hint = {'top':1}
        self.image.opacity = .4
        
        self.label = MDLabel()
        self.label.text='SASAS'
        self.label.adaptive_size=True
        self.label.color="white"
        self.label.font_size = 30
        self.label.pos_hint = {'top':.63, 'center_x':.5}
        
        self.label_body = MDLabel()
        self.label_body.text='asdjkashdkasjldasujdkl\nasjdl;asjdkashdkashjdhaskdhsakldhaslkdhkaslhdlaskjhdjklasgdjkasgdkjashdkjasgdjkgasdjkagsjkdgasdgasjkdgasjk'
        self.label_body.adaptive_size=True
        self.label_body.color="white"
        self.label_body.size = (250, 250)
        self.label_body.text_size = self.label_body.size
        self.label_body.font_size = 20
        self.label_body.pos_hint = {'top':.6, 'center_x':.5}
        
        self.btn = MDFillRoundFlatIconButton()
        self.btn.text = 'Читать'
        self.btn.icon = 'book'
        self.btn.pos_hint = {'center_y':.1, 'center_x':.5}

        self.btn_best_card = MDIconButton()
        self.btn_best_card.icon = 'star'
        self.btn_best_card.pos_hint = {'center_x':.5, 'center_y':.52}
        self.btn_best_card.theme_icon_color = 'Custom'
        self.btn_best_card.icon_color = 'gold'  

        self.body = MDFloatLayout()
        self.body.md_bg_color = '#ffffff'
        self.body.adaptive_size = True

        self.searcher = MDTextField()
        self.searcher.icon_left = 'magnify'
        self.searcher.mode = "rectangle"
        self.searcher.size_hint_max_x = 370
        self.searcher.line_color_focus = '#008000'
        self.searcher.text_color_focus = '#008000'
        self.searcher.hint_text_color_focus = '#008000'
        self.searcher.pos_hint = {'center_y':.4, 'center_x':.5}

        self.btn_home = MDIconButton()
        self.btn_home.icon = 'home'
        self.btn_home.pos_hint = {'center_x':.1, 'center_y':.5}
        self.btn_home.theme_icon_color = 'Custom'
        self.btn_home.icon_color = 'white'
        self.btn_home.on_press = self.func_btn_home

        self.btn_search = MDIconButton()
        self.btn_search.pos_hint = {'center_x':.36, 'center_y':.5}
        self.btn_search.icon = 'magnify'
        self.btn_search.theme_icon_color = 'Custom'
        self.btn_search.icon_color = 'white'
        self.btn_search.md_bg_color = '#006400'
        self.btn_search.on_press = self.func_btn_search

        self.btn_best = MDIconButton()
        self.btn_best.pos_hint = {'center_x':.63, 'center_y':.5}
        self.btn_best.icon = 'star'
        self.btn_best.theme_icon_color = 'Custom'
        self.btn_best.icon_color = 'white'
        self.btn_best.on_press = self.func_btn_best

        self.btn_logout = MDIconButton()
        self.btn_logout.pos_hint = {'center_x':.9, 'center_y':.5}
        self.btn_logout.icon = 'logout'
        self.btn_logout.theme_icon_color = 'Custom'
        self.btn_logout.icon_color = 'white'
        self.btn_logout.on_press = self.func_btn_logout

        self.search_layout.add_widget(self.searcher)

        self.reval.add_widget(self.image)
        self.reval.add_widget(self.label)
        self.reval.add_widget(self.label_body)
        self.reval.add_widget(self.btn)
        self.reval.add_widget(self.btn_best_card)

        self.card.add_widget(self.reval)

        
        self.card_layout.add_widget(self.card)

        self.scroll.add_widget(self.card_layout)

        self.navbar.add_widget(self.btn_home)
        self.navbar.add_widget(self.btn_search)
        self.navbar.add_widget(self.btn_best)
        self.navbar.add_widget(self.btn_logout)

        self.layout.add_widget(self.scroll)
        self.layout.add_widget(self.search_layout) 
        self.layout.add_widget(self.navbar)

        self.add_widget(self.layout)

    def func_btn_home(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'menu'

    def func_btn_search(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'magnify'

    def func_btn_best(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'star'

    def func_btn_logout(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'sign_in'


    def on_leave(self, *args):
        self.layout.clear_widgets()

class Star(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self):

        animation = Animation(pos_hint = {'center_y':.06, 'center_x':.5}, opacity = 1)

        self.layout = MDFloatLayout()

        self.navbar = MDFloatLayout()
        self.navbar.md_bg_color = '#008000'
        self.navbar.radius = (25, 25, 25, 25)
        self.navbar.size_hint_max_y = 80
        self.navbar.pos_hint = {'center_y':.03, "center_x":.03}
        self.navbar.opacity = .5

        animation.start(self.navbar)

        self.body = MDFloatLayout()
        self.body.md_bg_color = '#ffffff'

        self.btn_home = MDIconButton()
        self.btn_home.icon = 'home'
        self.btn_home.pos_hint = {'center_x':.1, 'center_y':.5}
        self.btn_home.theme_icon_color = 'Custom'
        self.btn_home.icon_color = 'white'
        self.btn_home.on_press = self.func_btn_home

        self.btn_search = MDIconButton()
        self.btn_search.pos_hint = {'center_x':.36, 'center_y':.5}
        self.btn_search.icon = 'magnify'
        self.btn_search.theme_icon_color = 'Custom'
        self.btn_search.icon_color = 'white'
        self.btn_search.on_press = self.func_btn_search

        self.btn_best = MDIconButton()
        self.btn_best.pos_hint = {'center_x':.63, 'center_y':.5}
        self.btn_best.icon = 'star'
        self.btn_best.theme_icon_color = 'Custom'
        self.btn_best.icon_color = 'white'
        self.btn_best.md_bg_color = '#006400'
        self.btn_best.on_press = self.func_btn_best

        self.btn_logout = MDIconButton()
        self.btn_logout.pos_hint = {'center_x':.9, 'center_y':.5}
        self.btn_logout.icon = 'logout'
        self.btn_logout.theme_icon_color = 'Custom'
        self.btn_logout.icon_color = 'white'
        self.btn_logout.on_press = self.func_btn_logout

        self.navbar.add_widget(self.btn_home)
        self.navbar.add_widget(self.btn_search)
        self.navbar.add_widget(self.btn_best)
        self.navbar.add_widget(self.btn_logout)

        self.layout.add_widget(self.body) 
        self.layout.add_widget(self.navbar)

        self.add_widget(self.layout)

    def func_btn_home(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'menu'

    def func_btn_search(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'magnify'

    def func_btn_best(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'star'

    def func_btn_logout(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'sign_in'

    def on_leave(self, *args):
        self.layout.clear_widgets()


class My_Wind(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self):

        animation = Animation(pos_hint = {'center_y':.06, 'center_x':.5}, opacity = 1)
        animation1 = Animation(opacity = 1, pos_hint = {"center_y":.5, 'center_x':.5})

        self.layout = MDFloatLayout()

        self.navbar = MDFloatLayout()
        self.navbar.md_bg_color = '#008000'
        self.navbar.radius = (25, 25, 25, 25)
        self.navbar.size_hint_max_y = 80
        self.navbar.pos_hint = {'center_y':.03, 'center_x':.03}
        self.navbar.opacity = .5

        animation.start(self.navbar)

        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'
        self.scroll.pos_hint = {"center_y":.43, 'center_x':.43}
        self.scroll.opacity = .5

        animation1.start(self.scroll)

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.spacing = 40
        self.card_layout.size_hint = (1, None)
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 75
        self.card_layout.pos_hint = {"center_y":.03, 'center_x':.3}
        self.card_layout.opacity = .5
        

        self.card = MDCard()
        self.card.focus_behavior = True
        self.card.focus_color = '#009988'
        self.card.line_color=(0.2, 0.2, 0.2, 0.8)
        self.card.style = 'elevated'
        self.card.padding = "4dp"
        self.card.size_hint = (None, None)
        self.card.size = ("250dp", "450dp")
        self.card.unfocus_color = "#008000"
        self.card.md_bg_color = "#008000"
        self.card.shadow_softness = 2
        self.card.shadow_offset = (0, 1)

        animation.start(self.card_layout)
        
        self.reval = MDRelativeLayout()
        
        self.image = AsyncImage()
        self.image.source = "https://images4.alphacoders.com/766/thumb-1920-766744.jpg"
        #"https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg" 
        #'http://fotorelax.ru/wp-content/uploads/2017/03/Mesmerizing-nature-photography-by-Eric-Bunting-24.jpg'
        self.image.size_hint = (None, None)
        self.image.size = (363, 250)
        self.image.pos_hint = {'top':1}
        self.image.opacity = .4
        
        self.label = MDLabel()
        self.label.text='SASAS'
        self.label.adaptive_size=True
        self.label.color="white"
        self.label.font_size = 30
        self.label.pos_hint = {'top':.63, 'center_x':.5}
        
        self.label_body = MDLabel()
        self.label_body.text='asdjkashdkasjldasujdkl\nasjdl;asjdkashdkashjdhaskdhsakldhaslkdhkaslhdlaskjhdjklasgdjkasgdkjashdkjasgdjkgasdjkagsjkdgasdgasjkdgasjk'
        self.label_body.adaptive_size=True
        self.label_body.color="white"
        self.label_body.size = (250, 250)
        self.label_body.text_size = self.label_body.size
        self.label_body.font_size = 20
        self.label_body.pos_hint = {'top':.6, 'center_x':.5}
        
        self.btn = MDFillRoundFlatIconButton()
        self.btn.text = 'Читать'
        self.btn.icon = 'book'
        self.btn.pos_hint = {'center_y':.1, 'center_x':.5}

        self.btn_best_card = MDIconButton()
        self.btn_best_card.icon = 'star'
        self.btn_best_card.pos_hint = {'center_x':.5, 'center_y':.52}
        self.btn_best_card.theme_icon_color = 'Custom'
        self.btn_best_card.icon_color = 'gold'

        self.body = MDFloatLayout()
        self.body.md_bg_color = '#ffffff'

        self.btn_home = MDIconButton()
        self.btn_home.icon = 'home'
        self.btn_home.pos_hint = {'center_x':.1, 'center_y':.5}
        self.btn_home.theme_icon_color = 'Custom'
        self.btn_home.icon_color = 'white'
        self.btn_home.md_bg_color = '#006400'
        self.btn_home.on_press = self.func_btn_home

        self.btn_search = MDIconButton()
        self.btn_search.pos_hint = {'center_x':.36, 'center_y':.5}
        self.btn_search.icon = 'magnify'
        self.btn_search.theme_icon_color = 'Custom'
        self.btn_search.icon_color = 'white'
        self.btn_search.on_press = self.func_btn_search

        self.btn_best = MDIconButton()
        self.btn_best.pos_hint = {'center_x':.63, 'center_y':.5}
        self.btn_best.icon = 'star'
        self.btn_best.theme_icon_color = 'Custom'
        self.btn_best.icon_color = 'white'
        self.btn_best.on_press = self.func_btn_best

        self.btn_logout = MDIconButton()
        self.btn_logout.pos_hint = {'center_x':.9, 'center_y':.5}
        self.btn_logout.icon = 'logout'
        self.btn_logout.theme_icon_color = 'Custom'
        self.btn_logout.icon_color = 'white'
        self.btn_logout.on_press = self.func_btn_logout


        self.reval.add_widget(self.image)
        self.reval.add_widget(self.label)
        self.reval.add_widget(self.label_body)
        self.reval.add_widget(self.btn)
        self.reval.add_widget(self.btn_best_card)

        self.card.add_widget(self.reval)

        
        self.card_layout.add_widget(self.card)

        self.scroll.add_widget(self.card_layout)

        self.navbar.add_widget(self.btn_home)
        self.navbar.add_widget(self.btn_search)
        self.navbar.add_widget(self.btn_best)
        self.navbar.add_widget(self.btn_logout)

        self.layout.add_widget(self.scroll) 
        self.layout.add_widget(self.navbar)

        self.add_widget(self.layout)

    def func_btn_home(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'menu'

    def func_btn_search(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'magnify'

    def func_btn_best(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'star'

    def func_btn_logout(self):
        sm.sm.transition.direction = 'right'
        sm.sm.current = 'sign_in'

    def on_leave(self, *args):
        self.layout.clear_widgets()


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()
        #self.sm.add_widget(Sign_in(name='sign_in'))
        #self.sm.add_widget(Sign_up(name='sign_up'))
        self.sm.add_widget(My_Wind(name='menu'))
        self.sm.add_widget(Magnify(name='magnify'))
        self.sm.add_widget(Star(name='star'))
    def build(self):
        return self.sm


sm = MainApp()
sm.run()
