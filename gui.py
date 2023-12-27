from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import os

class BackgroundApp(App):
    
    def build(self):
        # Create a main layout using StackLayout
        main_layout = BoxLayout(orientation = "vertical", padding = 0, spacing = 0)
        #
        heading_label = Label(text='CODE MOSAIC', font_size=20, color=(1, 1, 1, 1))
        main_layout.add_widget(heading_label)
        # nav bar layout
        nav_bar = BoxLayout(orientation = "horizontal", padding = 10, spacing = 10)
        path_input = TextInput(hint_text='Full path to file e.g. D:\Codes\Projects\Code Mosaic\\test.py', multiline=False)
        browse_button = Button(text="Browse",  size=(100, 50))
        nav_bar.add_widget(path_input)
        nav_bar.add_widget(browse_button)
        # ----

        # vertical bar 1 layout
        v_bar_layout1 = BoxLayout(orientation = "horizontal", padding = 10, spacing = 10)
        logo = Image(source = os.path.abspath("") + "/RES/logo1.jpg", allow_stretch=False, keep_ratio=False)
        v_bar_layout1.add_widget(logo)
        # > vertical bar 2 layout
        v_bar_layout2 = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        # > > option layout
        # height
        height_layout = BoxLayout(orientation = "horizontal", padding = 10, spacing = 10)
        height_label = Label(text='Height', font_size=20, color=(1, 1, 1, 1))
        height_input = TextInput(hint_text='Height', multiline=False)
        height_layout.add_widget(height_label)
        height_layout.add_widget(height_input)
        # width
        width_layout = BoxLayout(orientation = "horizontal", padding = 10, spacing = 10)
        width_label = Label(text='Width', font_size=20, color=(1, 1, 1, 1))
        width_input = TextInput(hint_text='Width', multiline=False)
        width_layout.add_widget(width_label)
        width_layout.add_widget(width_input)
        # font size
        font_size_layout = BoxLayout(orientation = "horizontal", padding = 10, spacing = 10)
        font_size_label = Label(text='Font Size', font_size=20, color=(1, 1, 1, 1))
        font_size_input = TextInput(hint_text='Font Size', multiline=False)
        font_size_layout.add_widget(font_size_label)
        font_size_layout.add_widget(font_size_input)
        # spacing
        spacing_layout = BoxLayout(orientation = "horizontal", padding = 10, spacing = 10)
        spacing_label = Label(text='Spacing', font_size=20, color=(1, 1, 1, 1))
        spacing_input = TextInput(hint_text='Spacing', multiline=False)
        spacing_layout.add_widget(spacing_label)
        spacing_layout.add_widget(spacing_input)

        # > > ---- 
        v_bar_layout2.add_widget(height_layout)
        v_bar_layout2.add_widget(width_layout)
        v_bar_layout2.add_widget(font_size_layout)
        v_bar_layout2.add_widget(spacing_layout)
        # > ----
        v_bar_layout1.add_widget(v_bar_layout2)
        # ----
        
        main_layout.add_widget(nav_bar)
        main_layout.add_widget(v_bar_layout1)
        generate_button = Button(text="Generate",  size=(100, 50))
        main_layout.add_widget(generate_button)
        return main_layout

if __name__ == '__main__':
    BackgroundApp().run()
