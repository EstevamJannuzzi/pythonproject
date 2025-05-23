from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class Equacao2GrauLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.spacing = 10

        self.add_widget(Label(text='Equação do 2º Grau: ax² + bx + c = 0', font_size=22))

        self.input_a = TextInput(hint_text='Digite o valor de a', input_filter='float', multiline=False)
        self.input_b = TextInput(hint_text='Digite o valor de b', input_filter='float', multiline=False)
        self.input_c = TextInput(hint_text='Digite o valor de c', input_filter='float', multiline=False)
        self.add_widget(self.input_a)
        self.add_widget(self.input_b)
        self.add_widget(self.input_c)

        self.btn_calcular = Button(text='Calcular', size_hint=(1, 0.5))
        self.btn_calcular.bind(on_press=self.calcular)
        self.add_widget(self.btn_calcular)

        self.resultado = Label(text='', font_size=18)
        self.add_widget(self.resultado)

    def calcular(self, instance):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            c = float(self.input_c.text)
            passos = f"a = {a}, b = {b}, c = {c}\n"
            passos += f"Delta = b² - 4ac = ({b})² - 4*{a}*{c}\n"
            delta = b**2 - 4*a*c
            passos += f"Delta = {delta}\n"
            if delta < 0:
                passos += "Delta negativo. Não existem raízes reais."
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                passos += f"x1 = (-b + √Delta) / 2a = ({-b} + √{delta}) / (2*{a}) = {x1}\n"
                passos += f"x2 = (-b - √Delta) / 2a = ({-b} - √{delta}) / (2*{a}) = {x2}"
            self.resultado.text = passos
        except Exception as e:
            self.resultado.text = f"Erro: {str(e)}"

class Equacao2GrauApp(App):
    def build(self):
        Window.size = (500, 400)
        return Equacao2GrauLayout()

if __name__ == '__main__':
    Equacao2GrauApp().run()
