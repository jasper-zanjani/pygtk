import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class HelloWorld(Gtk.Window):
    def __init__(self, *args, name="World", **kwargs):
        super().__init__(*args, **kwargs)
        self.connect("destroy", Gtk.main_quit)
        self.set_title(f"Hello, {name}!")
        self.show_all()

window = HelloWorld(name=sys.argv[-1])
Gtk.main()