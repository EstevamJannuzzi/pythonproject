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

        self.add_widget(Label(text='Equação do 2º Grau: ax² + bx + c = 0', font_size=30))

        self.input_a = TextInput(hint_text='Digite o valor de a', input_filter='float', multiline=False, height=40, size_hint_y=None)
        self.input_b = TextInput(hint_text='Digite o valor de b', input_filter='float', multiline=False, height=40, size_hint_y=None)
        self.input_c = TextInput(hint_text='Digite o valor de c', input_filter='float', multiline=False, height=40, size_hint_y=None)
        self.add_widget(self.input_a)
        self.add_widget(self.input_b)
        self.add_widget(self.input_c)

        self.btn_calcular = Button(text='Calcular', height=40, size_hint_y=None)
        self.btn_calcular.bind(on_press=self.calcular)
        self.btn_limpar = Button(text='Limpar', height=40, size_hint_y=None)
        self.btn_limpar.bind(on_press=self.limpar)
        botoes_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.5), spacing=10)
        botoes_layout.add_widget(self.btn_calcular)
        botoes_layout.add_widget(self.btn_limpar)
        self.add_widget(botoes_layout)

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

    def limpar(self, instance):
        self.input_a.text = ''
        self.input_b.text = ''
        self.input_c.text = ''
        self.resultado.text = ''

class Equacao2GrauApp(App):
    def build(self):
        Window.size = (500, 600)
        Window.clearcolor = (0.0, 0.2, 0.2, 1)
        return Equacao2GrauLayout()

if __name__ == '__main__':
    Equacao2GrauApp().run()
