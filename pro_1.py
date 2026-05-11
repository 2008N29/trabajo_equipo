from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class AppCursos(App):

    def build(self):

        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        
        with layout.canvas.before:
            Color(1, 0.75, 0.8, 1)  # rosa claro
            self.bg = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_bg, pos=self._update_bg)

        
        titulo = Label(
            text='Nit y Ale',
            font_size=32,
            bold=True,
            size_hint=(1, 0.15),
            color=(0, 0, 0, 1)
        )

        
        subtitulo = Label(
            text='Pantalla Principal',
            font_size=22,
            size_hint=(1, 0.1),
            color=(0, 0, 0, 1)
        )

        
        contenedor = BoxLayout(orientation='vertical', padding=15)
        
        with contenedor.canvas.before:
            Color(1, 1, 1, 1)  
            self.box_bg = Rectangle(size=contenedor.size, pos=contenedor.pos)

        contenedor.bind(size=self._update_box, pos=self._update_box)

        cursos = GridLayout(cols=1, spacing=10)

        lista = [
            " Programación Básica",
            " Diseño Web",
            " Bases de Datos",
            " Inteligencia Artificial"
        ]

        for curso in lista:
            btn = Button(
                text=curso,
                size_hint_y=None,
                height=50,
                background_color=(0.2, 0.6, 0.9, 1)
            )
            cursos.add_widget(btn)

        contenedor.add_widget(cursos)

        
        boton = Button(
            text='Inscribirse / Continuar',
            size_hint=(1, 0.15),
            background_color=(0.1, 0.8, 0.3, 1)
        )

        boton.bind(on_press=self.inscribirse)

       
        layout.add_widget(titulo)
        layout.add_widget(subtitulo)
        layout.add_widget(contenedor)
        layout.add_widget(boton)

        return layout

    
    def _update_bg(self, instance, value):
        self.bg.size = instance.size
        self.bg.pos = instance.pos

    
    def _update_box(self, instance, value):
        self.box_bg.size = instance.size
        self.box_bg.pos = instance.pos

    def inscribirse(self, instance):
        print("Inscripción o continuación")

if __name__ == '__main__':
    AppCursos().run()