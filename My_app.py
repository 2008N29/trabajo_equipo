from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        screen = Screen()

        # Botón que abre el menú
        self.menu_button = MDRectangleFlatButton(
            text="Abrir menú",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.open_menu
        )

        # Menú
        self.menu = MDDropdownMenu(
            caller=self.menu_button,
            items=[
                {"text": "Opción 1", "on_release": lambda: self.menu_callback("Opción 1")},
                {"text": "Opción 2", "on_release": lambda: self.menu_callback("Opción 2")},
                {"text": "Opción 3", "on_release": lambda: self.menu_callback("Opción 3")},
            ],
            width_mult=3,
        )

        # Barra de herramientas
        toolbar = MDToolbar(
            title="Mi aplicación",
            pos_hint={"top": 1}
        )
        toolbar.left_action_items = [["language-python", lambda x: print("Python")]]
        toolbar.right_action_items = [["settings", lambda x: print("Configuración")]]

        # Etiqueta
        label = MDLabel(
            text="Bienvenido a mi aplicación",
            halign="center",
            pos_hint={"center_y": 0.6},
        )

        # Agregar widgets
        screen.add_widget(toolbar)
        screen.add_widget(label)
        screen.add_widget(self.menu_button)

        return screen

    def open_menu(self, *args):
        self.menu.open()

    def menu_callback(self, text):
        print(text)
        self.menu.dismiss()

if __name__ == "__main__":
    MyApp().run()