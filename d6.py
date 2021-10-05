import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random
from math import floor

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        scale_adj = Gtk.Adjustment.new(1,0,6,1,2,0)
        scale_lbl = Gtk.Label.new_with_mnemonic("Number of dice")

        self.scale = Gtk.Scale.new(Gtk.Orientation.HORIZONTAL, scale_adj)
        self.scale.set_digits(0)
        
        button = Gtk.Button.new_with_label("Throw")
        button.connect("clicked", self.on_button_clicked)
        self.label = Gtk.Label.new()

        scale_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        scale_box.add(scale_lbl)
        scale_box.add(self.scale)
        
        box = Gtk.Box.new(Gtk.Orientation.VERTICAL,5)
        box.pack_start(scale_box, False, True, 0)
        box.pack_start(button, False, True, 0)
        box.pack_start(self.label, False, True, 0)

        self.add(box)
        self.set_size_request(200,200)

    def on_button_clicked(self, button):
        dice = floor(self.scale.get_value())
        results = [random.randrange(6) for i in range(dice)]
        self.label.set_text(str(results))


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