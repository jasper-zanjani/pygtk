import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        question = Gtk.Label.new("What is your name?")

        # self.entry = Gtk.Entry.neW()
        # self.entry.set_text("World")
        
        self.entry = Gtk.Entry(text="World")
        
        button = Gtk.Button.new_with_mnemonic("Say hello to me")
        button.connect("clicked", self.on_button_clicked)

        prompt = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        prompt.add(question)
        prompt.add(self.entry)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box.add(prompt)
        box.add(button)
        self.add(box)
        # self.set_size_request(200,200)

    def on_button_clicked(self, button):
        print(f"Hello, {self.entry.get_text()}!")

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.example.myapp')

    def do_activate(self):
        self.window = ApplicationWindow(application=self)
        self.window.show_all()
        self.window.present()

if __name__ == '__main__':
    app = Application()
    app.run()