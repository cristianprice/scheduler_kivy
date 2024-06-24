from autopep8 import fix_code
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.clipboard import Clipboard
import contextlib
import io
from kivy import platform
from kivy.lang import Builder
from kivy.uix.codeinput import CodeInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from gui_components import ThButton, ThTabbedPanelItem, MainScreen, ThPopup


def ask_permission():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        permissions_ls = [Permission.INTERNET,
                          Permission.WRITE_EXTERNAL_STORAGE,
                          Permission.READ_EXTERNAL_STORAGE]

        request_permissions(permissions_ls)


ask_permission()


def execute_code(out_label, code_input):
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


class CodeBoxLayout(BoxLayout):
    def on_run(self, out_label, code_input: CodeInput):
        execute_code(out_label, code_input)

    def on_paste(self, code_input: CodeInput):
        code_input.text = Clipboard.paste()

    def on_format(self, code_input: CodeInput):
        code_input.text = code_input.text = fix_code(code_input.text)

    def on_load_file(self):
        ThPopup(title='Hey There').open()


class MyKivyApp(App):
    def build(self):
        Builder.load_file('kv/main.kv')
        return MainScreen()


if __name__ == '__main__':
    MyKivyApp().run()
