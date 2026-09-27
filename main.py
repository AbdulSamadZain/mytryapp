from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)

class MyApp(App):
    def change_bg(self, color):
        if color == "red":
            Window.clearcolor = (1, 0, 0, 1)
        elif color == "green":
            Window.clearcolor = (0, 1, 0, 1)
        elif color == "blue":
            Window.clearcolor = (0, 0, 1, 1)

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        btn_layout = BoxLayout(size_hint_y=None, height=200, spacing=10, padding=10)

        # 1 hi function, 3 alag buttons
        btn_red = Button(text="Red", background_color=(1,0,0,1))
        btn_red.bind(on_press=lambda x: self.change_bg("red"))

        btn_green = Button(text="Green", background_color=(0,1,0,1))
        btn_green.bind(on_press=lambda x: self.change_bg("green"))

        btn_blue = Button(text="Blue", background_color=(0,0,1,1))
        btn_blue.bind(on_press=lambda x: self.change_bg("blue"))

        btn_layout.add_widget(btn_red)
        btn_layout.add_widget(btn_green)
        btn_layout.add_widget(btn_blue)

        main_layout.add_widget(BoxLayout()) # khali screen
        main_layout.add_widget(btn_layout)

        return main_layout

MyApp().run()