from kivy.uix.button import Button
from gui_themes import Fonts


class ThButton(Button):
    def __init__(self, **kwargs):
        super(ThButton, self).__init__(**kwargs)
        self.font_name = Fonts.FONT_PLAY
