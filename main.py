from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager,Screen


Window.clearcolor=(1,1,1,1)

class RowTable(RecycleDataViewBehavior,BoxLayout):
    text=StringProperty()
class scrollPage(RecycleView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        words = ['ww', 'wwkekdkdk', 'saaaadjsj', 'sjdsjco','s','asa',',,gff']
        self.data = [{'text': word} for word in words]



class RowTableOrder(RecycleDataViewBehavior,BoxLayout):
    name = StringProperty()

class tableOrderPage(RecycleView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        print('jsjsj')
        names=['Aidar','Misha','Amir','Ruslan','Arseny']
        self.data=[{'name':name} for name in names]



class PageManager(ScreenManager):
    pass
class TBScreen(Screen):
    pass
class ElScreen(Screen):
    pass

class Page(GridLayout):
    def pageTable(self):
        self.ids.PM.current='table'
    def screen1(self):
        self.ids.PM.current='screen2'

    pass


class ChimstShopApp(App):
    def build(self):
       
        return Page()



if __name__ == "__main__":
    ChimstShopApp().run()