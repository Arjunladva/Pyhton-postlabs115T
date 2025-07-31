from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text="Count: 0", font_size=32)
        layout.add_widget(self.label)

        button = Button(text="Increment", font_size=24)
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Count: {self.counter}"

if __name__ == '__main__':
    CounterApp().run()
