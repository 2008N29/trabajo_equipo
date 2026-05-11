from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

KV = '''
ScreenManager:
    PantallaInicio:
    PantallaResultado:

<PantallaInicio>:
    name: "inicio"

    MDBoxLayout:
        orientation: "vertical"
        padding: 30
        spacing: 20

        MDLabel:
            text: "Ingresa tus datos"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: nombre
            hint_text: "Nombre"
            helper_text: "Campo obligatorio"
            helper_text_mode: "on_error"

        MDTextField:
            id: edad
            hint_text: "Edad"
            helper_text: "Solo números"
            helper_text_mode: "on_error"
            input_filter: "int"

        MDRaisedButton:
            text: "Continuar"
            pos_hint: {"center_x": 0.5}
            on_release: app.validar_datos(nombre.text, edad.text)

<PantallaResultado>:
    name: "resultado"

    MDBoxLayout:
        orientation: "vertical"
        padding: 30
        spacing: 20

        MDLabel:
            id: mensaje
            text: ""
            halign: "center"

        MDRaisedButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = "inicio"
'''