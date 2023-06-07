import requests
import cv2
import numpy as np

from kivy.metrics import dp
from typing import Any
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import *
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import *
from kivymd.uix.textfield import *
from kivymd.uix.label import *
from kivymd.uix.card import *
from kivymd.uix.relativelayout import *
from kivy.uix.image import *
from kivy.uix.scrollview import *
from kivymd.uix.gridlayout import *
from kivymd.uix.selection import *
from kivy.animation import Animation
from kivymd.uix.swiper import *
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.list import TwoLineAvatarListItem



Window.size = (380, 700)
Window.md_bg_color = "#ffffff"

class MyItem(TwoLineAvatarListItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = "Two-line item with avatar"
        self.secondary_text = "Secondary text here"
        self._no_ripple_effect = True

        #self.icon = Image()
        self.icon = MDIconButton()
        self.icon.icon = "account" 
        #"data/logo/kivy-icon-256.png"
        self.icon.pos_hint = {'center_x':.1, 'center_y':.5}
        self.icon.size_hint = (.9, .9)
        
        self.add_widget(self.icon)

class BaseNavigationDrawerItem(MDNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.text_color = "#4a4939"
        self.icon_color = "#4a4939"
        self.focus_color = "#AD2622"


class DrawerClickableItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_color = "#c5bdd2"
        self.selected_color = "#0c6c4d"

class CardBook(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.focus_behavior = True
        self.focus_color = '#e0ffff'
        self.line_color=(0.2, 0.2, 0.2, 0.8)
        self.style = 'elevated'
        self.padding = "4dp"
        self.size_hint = (None, None)
        self.size = ("300dp", "480dp")
        self.unfocus_color = "#f9f9f9"
        self.md_bg_color = "#ffffff"
        #self.shadow_softness = 2
        self.shadow_color = '#e0ffff'
        #self.line_color = ''
        #self.line_width = 1.3
        self.shadow_offset = (0, 1)

        self.reval = MDRelativeLayout()

        self.image = AsyncImage()
        self.image.source = "https://itsourcecode.com/wp-content/uploads/2021/02/Python-Books-for-Beginners-and-Advanced.png"
        #"https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg" 
        #'http://fotorelax.ru/wp-content/uploads/2017/03/Mesmerizing-nature-photography-by-Eric-Bunting-24.jpg'
        self.image.size_hint = (1, None)
        self.image.size = (1, 250)
        self.image.pos_hint = {'top':1.07}
        self.image.opacity = .4
        
        self.label = MDLabel()
        self.label.text='Python'
        self.label.adaptive_size=True
        self.label.color="black"
        self.label.font_size = 30
        self.label.pos_hint = {'top':.6, 'center_x':.5}
        
        self.label_body = MDLabel()
        self.label_body.text='Best Python Books. For Beginners and advanced programmers. '
        self.label_body.adaptive_size=True
        self.label_body.color="black"
        self.label_body.size_hint = (None, None)
        self.label_body.size = (250, 250)
        self.label_body.text_size = self.label_body.size
        self.label_body.font_size = 20
        self.label_body.pos_hint = {'center_y':.42, 'center_x':.55}
        
        self.btn = MDFillRoundFlatIconButton()
        self.btn.text = 'Читать'
        self.btn.icon = 'book'
        self.btn.pos_hint = {'center_y':.07, 'center_x':.4}

        self.btn_save = MDIconButton()
        self.btn_save.icon = 'content-save'
        self.btn_save.pos_hint = {'center_y':.07, 'center_x':.7}

        self.btn_bron = MDIconButton()
        self.btn_bron.icon = 'lock'
        self.btn_bron.pos_hint = {'center_y':.07, 'center_x':.9}

        self.btn_best_card = MDFillRoundFlatIconButton()
        self.btn_best_card.icon = 'star'
        self.btn_best_card.text = '4,5'
        self.btn_best_card.pos_hint = {'center_x':.5, 'center_y':.45}
        self.btn_best_card.theme_icon_color = 'Custom'
        self.btn_best_card.icon_color = 'gold'

        self.reval.add_widget(self.btn_save)
        self.reval.add_widget(self.btn_bron)
        self.reval.add_widget(self.image)
        self.reval.add_widget(self.label)
        self.reval.add_widget(self.label_body)
        self.reval.add_widget(self.btn)
        self.reval.add_widget(self.btn_best_card)

        self.add_widget(self.reval)



class ContentNavigationDrawer(MDNavigationLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.toolbar = MDTopAppBar()
        #self.toolbar.elevation=4
        self.toolbar.size_hint = (.1, .1)
        self.toolbar.radius = (25, 25, 25, 25)
        self.toolbar.pos_hint={"top":.98, 'center_x':.08}
        self.toolbar.md_bg_color = "#bbbbf00"
        self.toolbar.shadow_color = '#ffffff'
        self.toolbar.specific_text_color="red"
        self.toolbar.left_action_items=[['menu', lambda x: self.nav_drawer_open()]]      

        self.navigdraw = MDNavigationDrawer()
        self.navigdraw.id="nav_drawer"
        self.navigdraw.radius=(0, 16, 16, 0)

        self.navig_menu = MDNavigationDrawerMenu()

        self.navig_draw_manu_header = MDNavigationDrawerHeader()
        self.navig_draw_manu_header.title="Header title"
        self.navig_draw_manu_header.title_color="#4a4939"
        self.navig_draw_manu_header.spacing="4dp"
        self.navig_draw_manu_header.padding=("12dp", 0, 0, "56dp")

        self.line_header = MDNavigationDrawerDivider()

        self.service = MDNavigationDrawerLabel()
        self.service.text = 'Сервисы'

        self.service_0 = DrawerClickableItem()
        self.service_0.icon="newspaper-variant-outline"
        self.service_0.text_right_color="#4a4939"
        self.service_0.text="Новости"
        self.service_0.on_release = self.func_ser_0_news

        self.service_1 = DrawerClickableItem()
        self.service_1.icon="book"
        self.service_1.text_right_color="#4a4939"
        self.service_1.text="Библиотека"
        self.service_1.on_release = self.func_ser_1_lib

        self.service_2 = DrawerClickableItem()
        self.service_2.icon="et"
        self.service_2.text_right_color="#4a4939"
        self.service_2.text="Столовая"
        self.service_2.on_release = self.func_ser_2_sto

        self.service_3 = DrawerClickableItem()
        self.service_3.icon="laptop"
        self.service_3.text_right_color="#4a4939"
        self.service_3.text="Приемная по вопросам"
        self.service_3.on_release = self.func_ser_3_pre

        self.service_4 = DrawerClickableItem()
        self.service_4.icon="bed"
        self.service_4.text_right_color="#4a4939"
        self.service_4.text="Общежитие"
        self.service_4.on_release = self.func_ser_4_obs

        self.line_service = MDNavigationDrawerDivider()

        self.setting = DrawerClickableItem()
        self.setting.icon="screwdriver"
        self.setting.text_right_color="#4a4939"
        self.setting.text="Настройка"

        self.navig_menu.add_widget(self.navig_draw_manu_header)
        self.navig_menu.add_widget(self.line_header)
        self.navig_menu.add_widget(self.service)
        self.navig_menu.add_widget(self.service_0)
        self.navig_menu.add_widget(self.service_1)
        self.navig_menu.add_widget(self.service_2)
        self.navig_menu.add_widget(self.service_3)
        self.navig_menu.add_widget(self.service_4)
        self.navig_menu.add_widget(self.line_service)
        self.navig_menu.add_widget(self.setting)


        self.navigdraw.add_widget(self.navig_menu)


        self.add_widget(self.toolbar)
        self.add_widget(self.navigdraw)

    def nav_drawer_open(self, *args):
        self.navigdraw.set_state("open")

    def func_ser_0_news(self):
        sm.sm.current = 'news'

    def func_ser_1_lib(self):
        sm.sm.current = 'lib'

    def func_ser_2_sto(self):
        sm.sm.current = 'sto'

    def func_ser_3_pre(self):
        sm.sm.current = 'pre'

    def func_ser_4_obs(self):
        sm.sm.current = 'obs'

class MySwiper(MDSwiperItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.image = AsyncImage()
        self.image.source = "https://itsourcecode.com/wp-content/uploads/2021/02/Python-Books-for-Beginners-and-Advanced.png"
        self.image.size_hint = (1, None)
        self.image.size = (1, 200)
        self.image.pos_hint = {'top':1.07}
        self.image.opacity = .4

        self.spacing = 10

        self.add_widget(self.image)

class News(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        self.layout = MDFloatLayout()

        self.content_navig_draw = ContentNavigationDrawer()

        self.body = ScrollView()
        self.body.pos_hint = {'center_y':.5}
        self.body.size_hint_y = None
        self.body.height = 570

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.size_hint = (1, None)
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 43
        self.card_layout.pos_hint = {"center_y":.0, 'center_x':.5}

        self.swip = MDSwiper()
        self.swip.size_hint_y = None
        self.swip.height = 200
        self.swip.pos_hint = {'top':.87}
        self.swip.items_spacing = 20


        self.swip_item_1 = MySwiper()
        self.swip_item_1.image.source = 'http://fotorelax.ru/wp-content/uploads/2017/03/Mesmerizing-nature-photography-by-Eric-Bunting-24.jpg'

        self.swip_item_2 = MySwiper()
        self.swip_item_2.image.source = "https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg"

        self.swip_item_3 = MySwiper()
        self.swip_item_3.image.source = "http://192.168.8.103:8000/uploads/default.jpg"

        self.swip_item_4 = MySwiper()

        self.swip_item_5 = MySwiper()
        self.swip_item_6 = MySwiper()

        self.swip.add_widget(self.swip_item_1)
        self.swip.add_widget(self.swip_item_2)
        self.swip.add_widget(self.swip_item_3)
        self.swip.add_widget(self.swip_item_4)
        self.swip.add_widget(self.swip_item_5)
        self.swip.add_widget(self.swip_item_6)

        self.card_layout.add_widget(self.swip)

        self.body.add_widget(self.card_layout)

        self.layout.add_widget(self.body)
        self.layout.add_widget(self.content_navig_draw)

        self.add_widget(self.layout)

    def on_leave(self, *args):
        self.clear_widgets()


class Liberry(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):


        self.layout = MDFloatLayout()

        self.scroll = ScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'
        self.scroll.pos_hint = {"center_y":.4, 'center_x':.5}

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.size_hint = (1, None)
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 43
        self.card_layout.pos_hint = {"center_y":.0, 'center_x':.5}

        self.navbar = MDFloatLayout()
        self.navbar.md_bg_color = "#ffffff"
        self.navbar.line_color = "red"
        self.navbar.line_width = 1
        self.navbar.size_hint = (1, .1)
        self.navbar.pos_hint = {'center_x':.5, 'center_y':.056}

        self.button_home = MDIconButton()
        self.button_home.icon = 'home'
        self.button_home.pos_hint = {'center_x':.2, 'center_y':.5}

        self.button_save = MDIconButton()
        self.button_save.icon = 'star'
        self.button_save.pos_hint = {'center_x':.5, 'center_y':.5}

        self.button_bron = MDIconButton()
        self.button_bron.icon = 'lock'
        self.button_bron.pos_hint = {'center_x':.8, 'center_y':.5}

        self.content_navig_draw = ContentNavigationDrawer()

        self.search = MDTextField()
        self.search.hint_text_color_focus = 'red'
        self.search.hint_text = 'Поиск'
        self.search.color_mode = 'custom'
        self.search.line_color_focus = 'red'
        self.search.radius = (25, 25, 25, 25)
        self.search.mode = "rectangle"
        self.search.font_size = 17
        self.search.size_hint = (.6, .085)
        self.search.pos_hint = {'right':.85, 'top':.98}

        self.card_book = CardBook()

        self.navbar.add_widget(self.button_home)
        self.navbar.add_widget(self.button_save)
        self.navbar.add_widget(self.button_bron)

        self.card_layout.add_widget(self.card_book)

        self.scroll.add_widget(self.card_layout)

        self.layout.add_widget(self.scroll)
        self.layout.add_widget(self.search)
        self.layout.add_widget(self.navbar)
        self.layout.add_widget(self.content_navig_draw)

        self.add_widget(self.layout)
    
    def on_leave(self, *args):
        self.clear_widgets()


class Stolo(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        self.layout = MDFloatLayout()
    
        self.content_navig_draw = ContentNavigationDrawer()

        self.button_layout = MDFloatLayout()
        self.button_layout.pos_hint = {'center_x':.5, 'center_y':.5}

        self.button_exlent = MDRaisedButton()
        self.button_exlent.text = "Отлично"
        self.button_exlent.on_press =lambda :self.func_golos_anim(golos=self.button_exlent.text)
        self.button_exlent.size_hint = (.8, .08)
        self.button_exlent.font_size = 30
        self.button_exlent.pos_hint = {'center_x':.5, 'center_y':.7}

        self.button_good = MDRaisedButton()
        self.button_good.text = "Хорошо"
        self.button_good.on_release = lambda :self.func_golos_anim(golos=self.button_good.text)
        self.button_good.size_hint = (.8, .08)
        self.button_good.font_size = 30
        self.button_good.pos_hint = {'center_x':.5, 'center_y':.6}

        self.button_normal = MDRaisedButton()
        self.button_normal.text = "Нормально"
        self.button_normal.on_release = lambda :self.func_golos_anim(golos=self.button_normal.text)
        self.button_normal.size_hint = (.8, .08)
        self.button_normal.font_size = 30
        self.button_normal.pos_hint = {'center_x':.5, 'center_y':.5}

        self.button_extesend = MDRaisedButton()
        self.button_extesend.text = 'Плохо'
        self.button_extesend.on_release = lambda :self.func_golos_anim(golos=self.button_extesend.text)
        self.button_extesend.size_hint = (.8, .08)
        self.button_extesend.font_size = 30
        self.button_extesend.pos_hint = {'center_x':.5, 'center_y':.4}

        self.button_bad = MDRaisedButton()
        self.button_bad.text = "Отвратительное"
        self.button_bad.font_size = 30
        self.button_bad.on_release = lambda :self.func_golos_anim(golos=self.button_bad.text)
        self.button_bad.size_hint = (.8, .08)
        self.button_bad.pos_hint = {'center_x':.5, 'center_y':.3}


        self.button_layout.add_widget(self.button_exlent)
        self.button_layout.add_widget(self.button_good)
        self.button_layout.add_widget(self.button_normal)
        self.button_layout.add_widget(self.button_extesend)
        self.button_layout.add_widget(self.button_bad)

        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.content_navig_draw)

        self.add_widget(self.layout)

    def func_golos_anim(self, golos):
        def lora(q):
            self.clear_widgets()
            self.lbl.opacity=0
            self.on_enter()
        

        anim = Animation(
            opacity=1,
            d=1.5
        )

        self.layout.clear_widgets()

        self.lbl = MDLabel()
        self.lbl.text="Спасибо за голос!"
        self.lbl.opacity=0
        self.lbl.pos_hint={'center_x':.5,'center_y':.5}
        self.lbl.font_size=43
        
        self.layout.add_widget(self.lbl)
        anim.start(self.lbl)
        anim += Animation(
                opacity=0,
                d=1
            )
        anim.start(self.lbl)

        anim.on_complete=lora


    def on_leave(self, *args):
        self.clear_widgets()




class Prem(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        self.layout = MDFloatLayout()

        self.navbar = MDFloatLayout()
        self.navbar.md_bg_color = "#ffffff"
        self.navbar.line_color = "red"
        self.navbar.line_width = 1
        self.navbar.size_hint = (1, .1)
        self.navbar.pos_hint = {'center_x':.5, 'center_y':.056}

        self.content_navig_draw = ContentNavigationDrawer()

        self.button_home = MDIconButton()
        self.button_home.icon = 'home'
        self.button_home.pos_hint = {'center_x':.3, 'center_y':.5}

        self.button_chat = MDIconButton()
        self.button_chat.icon = 'chat'
        self.button_chat.pos_hint = {'center_x':.7, 'center_y':.5}

        self.scroll = ScrollView()
        self.scroll.pos_hint = {'center_y':.5}
        self.scroll.size_hint_y = None
        self.scroll.height = 570

        self.select = MDSelectionList()
        self.select.spacing = "12dp"
        self.select.size_hint = (1, None)
        self.select.size = (1, 200)
        self.select.overlay_color = sm.overlay_color[:-1] + [.2]
        self.select.icon_bg_color = sm.overlay_color

        self.derect = MyItem()
        self.derect.text = "Директор"

        self.zam_1 = MyItem()
        self.zam_1.text = "Зам 1"

        self.zam_2 = MyItem()
        self.zam_2.text = "Зам 2"

        self.zam_3 = MyItem()
        self.zam_3.text = "Зам 3"

        self.zam_4 = MyItem()
        self.zam_4.text = "Зам 4"

        self.zam_5 = MyItem()
        self.zam_5.text = "Зам 5"

        self.zam_6 = MyItem()
        self.zam_6.text = "Зам 6"

        self.prem = MyItem()
        self.prem.text = "Приемная комиссия"

        self.select.add_widget(self.derect)
        self.select.add_widget(self.zam_1)
        self.select.add_widget(self.zam_2)
        self.select.add_widget(self.zam_3)
        self.select.add_widget(self.zam_4)
        self.select.add_widget(self.zam_5)
        self.select.add_widget(self.zam_6)
        self.select.add_widget(self.prem)

        self.scroll.add_widget(self.select)

        self.navbar.add_widget(self.button_home)
        self.navbar.add_widget(self.button_chat)

        self.layout.add_widget(self.scroll)
        self.layout.add_widget(self.navbar)
        self.layout.add_widget(self.content_navig_draw)

        self.add_widget(self.layout)

    def on_leave(self, *args):
        self.clear_widgets()


class Obshe(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        self.layout = MDFloatLayout()

        self.navbar = MDFloatLayout()
        self.navbar.md_bg_color = "#ffffff"
        self.navbar.line_color = "red"
        self.navbar.line_width = 1
        self.navbar.size_hint = (1, .1)
        self.navbar.pos_hint = {'center_x':.5, 'center_y':.056}

        self.content_navig_draw = ContentNavigationDrawer()

        self.layout.add_widget(self.navbar)
        self.layout.add_widget(self.content_navig_draw)

        self.add_widget(self.layout)

    def on_leave(self, *args):
        self.clear_widgets()


class App(MDApp):

    overlay_color = get_color_from_hex("#6042e4")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sm = ScreenManager()
        self.sm.add_widget(News(name='news'))
        self.sm.add_widget(Liberry(name='lib'))
        self.sm.add_widget(Stolo(name='sto'))
        self.sm.add_widget(Prem(name='pre'))
        self.sm.add_widget(Obshe(name='obs'))


    def build(self):
        return self.sm
    
    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.root.ids.selection_list.unselected_all(),
                ]
            ]
            right_action_items = [["trash-can"], ["dots-vertical"]]
        else:
            md_bg_color = (0, 0, 0, 1)
            left_action_items = [["menu"]]
            right_action_items = [["magnify"], ["dots-vertical"]]
            self.root.ids.toolbar.title = "Inbox"

        Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
        self.root.ids.toolbar.left_action_items = left_action_items
        self.root.ids.toolbar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.root.ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )

    

sm = App()
sm.run()