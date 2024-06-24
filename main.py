from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.lang import Builder
from kivy import platform
import io
import contextlib
from kivy.core.clipboard import Clipboard
from kivy.uix.tabbedpanel import TabbedPanel
from autopep8 import fix_code


def ask_permission():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        permissions_ls = [Permission.INTERNET,
                          Permission.WRITE_EXTERNAL_STORAGE,
                          Permission.READ_EXTERNAL_STORAGE]

        request_permissions(permissions_ls)


ask_permission()

# Load the KV file
Builder.load_file('kv/main.kv')
from gui_buttons import ThButton, ThTabbedPanelItem


class CodeBoxLayout(BoxLayout):
    def on_run(self, out_label, code_input: CodeInput):

        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
            try:
                exec(code_input.text)
                out_label.text += stdout_capture.getvalue()
                out_label.text += stderr_capture.getvalue()
            except Exception as e:
                out_label.text += str(e)
                out_label.text += '\n'

    def on_paste(self, code_input: CodeInput):
        code_input.text = Clipboard.paste()

    def on_format(self, code_input: CodeInput):
        code_input.text = code_input.text = fix_code(code_input.text)

    def on_button2_click(self):
        print("Button 2 clicked!")


class MainScreen(TabbedPanel):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class MyKivyApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyKivyApp().run()
