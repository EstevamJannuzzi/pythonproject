from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout

class TabuadaApp(App):
    def build(self):
        Window.size = (380, 500)
        Window.clearcolor = (0.05, 0.05, 0.3, 1)  # Azul Marinho
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        titulo = Label(text='Escolha sua Tabuada', font_size=32, size_hint_y=None, height=60, color=(0.4,0.7,1,1))
        main_layout.add_widget(titulo)
        self.result = Label(text='', size_hint_y=0.7, font_size=22, color=(1,1,1,1), halign='center', valign='middle')
        self.result.bind(size=self._centralizar_label)
        main_layout.add_widget(self.result)
        # Layout inferior
        bottom_layout = AnchorLayout(anchor_x='center', anchor_y='bottom', size_hint_y=0.3)
        input_button_layout = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), width=310)
        # Centraliza o input
        input_anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        self.input = TextInput(hint_text='Digite um número', multiline=False, input_filter='int', size_hint=(None, None), width=300, height=40, font_size=24, halign='center')
        self.input.bind(focus=self._centralizar_input)
        input_anchor.add_widget(self.input)
        botoes_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(None, None), height=60)
        self.button = Button(text='Mostrar Tabuada', size_hint=(None, None), width=180, height=40, font_size=20)
        self.limpar = Button(text='Limpar', size_hint=(None, None), width=120, height=40, font_size=20)
        self.button.bind(on_press=self.mostrar_tabuada)
        self.limpar.bind(on_press=self.limpar_tela)
        botoes_layout.add_widget(self.button)
        botoes_layout.add_widget(self.limpar)
        input_button_layout.add_widget(input_anchor)
        input_button_layout.add_widget(botoes_layout)
        bottom_layout.add_widget(input_button_layout)
        main_layout.add_widget(bottom_layout)
        return main_layout

    def mostrar_tabuada(self, instance):
        num_text = self.input.text
        if num_text.isdigit():
            n = int(num_text)
            tabuada = '\n'.join([f"{n} x {i} = {n*i}" for i in range(1, 11)])
            self.result.text = tabuada
        else:
            self.result.text = 'Por favor, digite um número válido.'

    def limpar_tela(self, instance):
        self.input.text = ''
        self.result.text = ''

    def _centralizar_input(self, instance, value):
        instance.cursor = (len(instance.text), 0)

    def _centralizar_label(self, instance, value):
        instance.text_size = instance.size

if __name__ == "__main__":
    TabuadaApp().run()
