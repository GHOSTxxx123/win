from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import *
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import *
from kivymd.uix.gridlayout import *
from kivy.animation import Animation
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
import requests

Window.size = (350, 600)



class Win(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        animation = Animation(opacity = 1, pos_hint = {"center_y":.5, 'center_x':.5} )
    
        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'
        self.scroll.pos_hint = {"center_y":.43, 'center_x':.43}
        self.scroll.opacity = .5

        animation.start(self.scroll)

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.spacing = 40
        self.card_layout.size_hint = (1, None)
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 75

        url = "http://127.0.0.1:8000/export"

        data = requests.get(url).json()
        

        for i in data:
            self.card = MDCard()
            self.card.focus_behavior = True
            self.card.focus_color = '#009988'
            self.card.line_color=(0.2, 0.2, 0.2, 0.8)
            self.card.style = 'elevated'
            self.card.padding = "4dp"
            self.card.size_hint = (None, None)
            self.card.size = ("250dp", "450dp")
            self.card.unfocus_color = "#008888"
            self.card.md_bg_color = "#008888"
            self.card.shadow_softness = 2
            self.card.shadow_offset = (0, 1)

        
            self.reval = MDRelativeLayout()
        
            self.image = AsyncImage()
            #self.image.source = f"http://127.0.0.1:8000/uploads/{i['cover']}"
            #"https://images4.alphacoders.com/766/thumb-1920-766744.jpg"
            #"https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg" 
            #'http://fotorelax.ru/wp-content/uploads/2017/03/Mesmerizing-nature-photography-by-Eric-Bunting-24.jpg'
            self.image.size_hint = (None, None)
            self.image.size = (363, 250)
            self.image.pos_hint = {'top':1}
            self.image.opacity = .4
        
            self.label = MDLabel()
            self.label.text=i['title']
            self.label.adaptive_size=True
            self.label.color="white"
            self.label.font_size = 30
            self.label.pos_hint = {'top':.63, 'center_x':.5}
        
            self.label_body = MDLabel()
            self.label_body.text=i['description']
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

            self.btn_best = MDFillRoundFlatIconButton()
            self.btn_best.icon = f'star'
            self.btn_best.pos_hint = {'center_x':.5, 'center_y':.5}
            self.btn_best.theme_icon_color = 'Custom'
            self.btn_best.icon_color = 'gold'
            self.btn_best.text = str(i['rating'])
        
            self.reval.add_widget(self.image)
            self.reval.add_widget(self.label)
            self.reval.add_widget(self.label_body)
            self.reval.add_widget(self.btn)
            self.reval.add_widget(self.btn_best)

            self.card.add_widget(self.reval)

            self.card_layout.add_widget(self.card)

        self.scroll.add_widget(self.card_layout)
        
    def build(self):
        return self.scroll


Win().run()