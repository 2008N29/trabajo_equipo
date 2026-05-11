from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


# Pantalla 1: ingresar nombre
class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", spacing=20, padding=50)

        self.textfield = MDTextField(
            hint_text="Escribe tu nombre",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
        )

        boton = MDRectangleFlatButton(
            text="Ir a saludo",
            pos_hint={"center_x": 0.5},
            on_release=self.cambiar_pantalla
        )

        layout.add_widget(self.textfield)
        layout.add_widget(boton)

        self.add_widget(layout)

    def cambiar_pantalla(self, instance):
        nombre = self.textfield.text
        self.manager.get_screen("pantalla2").mostrar_nombre(nombre)
        self.manager.current = "pantalla2"


# Pantalla 2: mostrar saludo
class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", spacing=20, padding=50)

        self.label = MDLabel(
            text="Hola!",
            halign="center"
        )

        boton = MDRectangleFlatButton(
            text="Regresar",
            pos_hint={"center_x": 0.5},
            on_release=self.regresar
        )

        layout.add_widget(self.label)
        layout.add_widget(boton)

        self.add_widget(layout)

    def mostrar_nombre(self, nombre):
        self.label.text = f"Hola que haces????"

    def regresar(self, instance):
        self.manager.current = "pantalla1"


# App principal
class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name="pantalla1"))
        sm.add_widget(Screen2(name="pantalla2"))
        return sm


if __name__ == "__main__":
    MyApp().run()