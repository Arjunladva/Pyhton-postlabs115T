from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.input_field = TextInput(hint_text="Enter text here", multiline=False, font_size=20)
        layout.add_widget(self.input_field)

        submit_button = Button(text="Display Text", font_size=24)
        submit_button.bind(on_press=self.display_text)
        layout.add_widget(submit_button)

        self.output_label = Label(text="", font_size=24)
        layout.add_widget(self.output_label)

        return layout

    def display_text(self, instance):
        typed_text = self.input_field.text
        self.output_label.text = f"You typed: {typed_text}"

if __name__ == '__main__':
    TextInputApp().run()
