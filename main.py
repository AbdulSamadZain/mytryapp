from kivymd.app import MDApp
from kivymd.color_definitions import theme_colors
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from openpyxl.styles.alignment import horizontal_alignments


class CalculaterApp(MDApp):

    def build(self):
        self.fd = 0
        self.sd = 0
        self.ft = 0
        self.conti = 0
        self.result = 0
        self.ac = 0
        self.op = 0
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A200"
        screen = Screen()
        self.values = MDTextField(pos_hint={'center_x': 0.4, 'center_y': 0.65}, halign='right', size_hint_x=None,
                                  width=250)
        screen.add_widget(self.values)
        btn_7 = MDRoundFlatButton(text='7', pos_hint={'center_x': 0.28, 'center_y': 0.5}, on_release=self.add_7)
        screen.add_widget(btn_7)
        btn_8 = MDRoundFlatButton(text='8', pos_hint={'center_x': 0.37, 'center_y': 0.5}, on_release=self.add_8)
        screen.add_widget(btn_8)
        btn_9 = MDRoundFlatButton(text='9', pos_hint={'center_x': 0.46, 'center_y': 0.5}, on_release=self.add_9)
        screen.add_widget(btn_9)
        btn_4 = MDRoundFlatButton(text='4', pos_hint={'center_x': 0.28, 'center_y': 0.43}, on_release=self.add_4)
        screen.add_widget(btn_4)
        btn_5 = MDRoundFlatButton(text='5', pos_hint={'center_x': 0.37, 'center_y': 0.43}, on_release=self.add_5)
        screen.add_widget(btn_5)
        btn_6 = MDRoundFlatButton(text='6', pos_hint={'center_x': 0.46, 'center_y': 0.43}, on_release=self.add_6)
        screen.add_widget(btn_6)
        btn_1 = MDRoundFlatButton(text='1', pos_hint={'center_x': 0.28, 'center_y': 0.36}, on_release=self.add_1)
        screen.add_widget(btn_1)
        btn_2 = MDRoundFlatButton(text='2', pos_hint={'center_x': 0.37, 'center_y': 0.36}, on_release=self.add_2)
        screen.add_widget(btn_2)
        btn_3 = MDRoundFlatButton(text='3', pos_hint={'center_x': 0.46, 'center_y': 0.36}, on_release=self.add_3)
        screen.add_widget(btn_3)
        btn_0 = MDRoundFlatButton(text='0', pos_hint={'center_x': 0.28, 'center_y': 0.29}, on_release=self.add_0)
        screen.add_widget(btn_0)
        self.btn_point = MDRoundFlatButton(text='.', pos_hint={'center_x': 0.37, 'center_y': 0.29}, disabled=False,
                                           on_release=self.add_point)
        screen.add_widget(self.btn_point)
        btn_AC = MDFillRoundFlatButton(text='AC', pos_hint={'center_x': 0.28, 'center_y': 0.57},
                                       md_bg_color=(1.0, 0.0, 0.0, 1.0), on_release=self.add_C)
        screen.add_widget(btn_AC)
        btn_Plus = MDFillRoundFlatButton(text='+', pos_hint={'center_x': 0.55, 'center_y': 0.57},
                                         md_bg_color=(5.0 / 255.0, 180.0 / 255.0, 1.0, 1.0), on_release=self.add_number)
        screen.add_widget(btn_Plus)
        btn_Minus = MDFillRoundFlatButton(text='-', pos_hint={'center_x': 0.55, 'center_y': 0.5},
                                          md_bg_color=(5.0 / 255.0, 180.0 / 255.0, 1.0, 1.0),
                                          on_release=self.sub_number)
        screen.add_widget(btn_Minus)
        btn_Div = MDFillRoundFlatButton(text='/', pos_hint={'center_x': 0.55, 'center_y': 0.43},
                                        md_bg_color=(5.0 / 255.0, 180.0 / 255.0, 1.0, 1.0), on_release=self.div_number)
        screen.add_widget(btn_Div)
        btn_Mul = MDFillRoundFlatButton(text='x', pos_hint={'center_x': 0.55, 'center_y': 0.36},
                                        md_bg_color=(5.0 / 255.0, 180.0 / 255.0, 1.0, 1.0), on_release=self.mul_number)
        screen.add_widget(btn_Mul)
        btn_Res = MDFillRoundFlatButton(text='=', pos_hint={'center_x': 0.55, 'center_y': 0.29},
                                        md_bg_color=(5.0 / 255.0, 280.0 / 255.0, 150.0 / 255.0, 1.0),
                                        on_release=self.res)
        screen.add_widget(btn_Res)
        return screen

    def add_7(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 7)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "7"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "7"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "7"
            self.fd = self.values.text

    def add_8(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 8)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "8"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "8"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "8"
            self.fd = self.values.text

    def add_9(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 9)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "9"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "9"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "9"
            self.fd = self.values.text

    def add_4(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 4)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "4"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "4"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "4"
            self.fd = self.values.text

    def add_5(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 5)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "5"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "5"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "5"
            self.fd = self.values.text

    def add_6(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 6)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "6"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "6"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "6"
            self.fd = self.values.text

    def add_1(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 1)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "1"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "1"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "1"
            self.fd = self.values.text

    def add_2(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 2)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "2"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "2"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "2"
            self.fd = self.values.text

    def add_3(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 3)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "3"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "3"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "3"
            self.fd = self.values.text

    def add_0(self, obj):
        if self.conti is 1:
            self.sd = str(int(self.sd) * 10)
            self.sd = str(int(self.sd) + 0)
            if self.op is 1:
                self.result = str(int(self.fd) + int(self.sd))
            if self.op is 2:
                self.result = str(int(self.fd) - int(self.sd))
            if self.op is 3:
                self.result = str(int(self.fd) * int(self.sd))
            if self.op is 4:
                self.result = str(int(self.fd) / int(self.sd))
            self.values.text = str(self.result)
            self.values.hint_text = self.values.hint_text + "0"
        elif self.ac is 1:
            self.values.text = ''
            self.values.text = self.values.text + "0"
            self.fd = self.values.text
            self.ac = 0
        else:
            self.values.text = self.values.text + "0"
            self.fd = self.values.text

    def add_point(self, obj):
        self.values.text += '.'
        self.btn_point.disabled = True

    def add_C(self, obj):
        self.values.text = ''
        self.values.hint_text = ''
        self.sd = 0
        self.fd = 0
        self.result = 0
        self.conti = 0
        self.ft = 0
        self.ac = 0
        self.op = 0

    def add_number(self, obj):
        self.op = 1
        if self.ft is 0:
            self.values.hint_text = self.values.text + "+"
            self.ft = 1
            self.conti = 1
        else:
            self.values.hint_text = self.values.hint_text + "+"
            self.fd = self.result
            self.result = 0
            self.sd = 0

    def sub_number(self, obj):
        self.op = 2
        if self.ft is 0:
            self.values.hint_text = self.values.text + "-"
            self.ft = 1
            self.conti = 1
        else:
            self.values.hint_text = self.values.hint_text + "-"
            self.fd = self.result
            self.result = 0
            self.sd = 0

    def mul_number(self, obj):
        self.op = 3
        if self.ft is 0:
            self.values.hint_text = self.values.text + "x"
            self.ft = 1
            self.conti = 1
        else:
            self.values.hint_text = self.values.hint_text + "x"
            self.fd = self.result
            self.result = 0
            self.sd = 0

    def div_number(self, obj):
        self.op = 4
        if self.ft is 0:
            self.values.hint_text = self.values.text + "/"
            self.ft = 1
            self.conti = 1
        else:
            self.values.hint_text = self.values.hint_text + "/"
            self.fd = self.result
            self.result = 0
            self.sd = 0

    def res(self, obj):
        self.values.hint_text = self.values.text
        self.values.text = ''
        self.values.text = self.values.hint_text
        self.values.hint_text = ""
        self.sd = 0
        self.fd = 0
        self.result = 0
        self.conti = 0
        self.ft = 0
        self.fd = self.values.text
        self.ac = 1
        self.op = 0


CalculaterApp().run()
