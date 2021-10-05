import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import sys, itertools


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, name = "world", **kwargs):
        super().__init__(*args, **kwargs)

        with open("/home/jasper/notes/docs/Coding/Dogfood/raven.txt") as f:
            self.raven = itertools.cycle([l.strip() for l in f.readlines()])

        self.label = Gtk.Label.new(f"Hello {name}")
        button = Gtk.Button.new()
        button.title="Next"
        button.connect("clicked", self.on_button_clicked)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.add(self.label)
        vbox.add(button)
        self.add(vbox)
        self.set_size_request(200,200)
    
    def on_button_clicked(self, button):
        self.label.txt = next(self.raven)


class Application(Gtk.Application):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, application_id="org.example.myapp", **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, name = self.name, title = f"Hello, {self.name}!")
        self.window.show_all()
        self.window.present()

if __name__ == '__main__':
    app = Application(sys.argv[-1])
    app.run()
