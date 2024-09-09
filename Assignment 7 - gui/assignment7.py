from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
class MyBoxLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        self.sound_button = SoundLoader.load("click.mp3")
        self.cookie_sound = SoundLoader.load("yay.mp3")
        return MyBoxLayout()

    def get_started(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hi {name}! What's up"
        

    def clear_output(self):
        self.root.ids.output_label.text = ""
        self.root.ids.cookie_image.source = ""
        self.root.ids.cookie_image.size_hint = (None,None)
        self.root.ids.cookie_image.size = (0,0)
        self.root.ids.cookie_image.pos_hint = {'center_x':0.5,'center_y':0.5}
    def cookie(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Here is your Cookie {name}"
        self.root.ids.cookie_image.source = "cookie.png"
        self.root.ids.cookie_image.size_hint = (None,None)
        self.root.ids.cookie_image.size = (200,200)
        self.root.ids.cookie_image.pos_hint = {'center_x':0.5,'center_y':0.5}
    
    def play_button_sound(self):
        if self.sound_button:
            self.sound_button.play()

    def play_cookie_sound(self):
        if self.cookie_sound:
            self.cookie_sound.play()

if __name__ == '__main__':
    MyApp().run()
