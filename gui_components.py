from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel
from gui_themes import Fonts
from kivy.uix.popup import Popup


class ThButton(Button):
    def __init__(self, **kwargs):
        super(ThButton, self).__init__(**kwargs)
        self.font_name = Fonts.FONT_PLAY


class ThTabbedPanelItem(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(ThTabbedPanelItem, self).__init__(**kwargs)
        self.font_name = Fonts.FONT_PLAY_BOLD


class MainScreen(TabbedPanel):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class ThPopup(Popup):
    def __init__(self, **kwargs):
        super(ThPopup, self).__init__(**kwargs)
        self.font_name = Fonts.FONT_PLAY_BOLD
