from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.lang import Builder
from kivy import platform
from gui_buttons import ThButton
import io
import contextlib

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
                        Permission.READ_EXTERNAL_STORAGE])


# Load the KV file
Builder.load_file('kv/main.kv')


class MyBoxLayout(BoxLayout):
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

    def on_button2_click(self):
        print("Button 2 clicked!")


class MyKivyApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyKivyApp().run()
