import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys


class Window(Gtk.Window):
    def __init__(self, *args, name = "World", **kwargs):
        Gtk.Window.__init__(self, *args, **kwargs)
        self.set_default_size(200,200)
        self.set_title("Hello, World!")
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.connect("destroy", Gtk.main_quit)
        self.add(box)

        question = Gtk.Label(label="What is your name?")
        box.add(question)
        
        self.entry = Gtk.Entry(text="World")
        box.add(self.entry)

        button = Gtk.Button.new_with_mnemonic("Greet")
        button.connect("clicked", self.on_button_clicked, self)
        box.add(button)

        self.show_all()

    def on_button_clicked(self, button, parent):
        dialog = Gtk.MessageDialog(
                message_type=Gtk.MessageType.INFO,
                text=f"Hello, {parent.entry.get_text()}",
                parent=parent,
        )
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.run()
        dialog.destroy()

if __name__ == '__main__':
    Window(name = sys.argv[-1])
    Gtk.main()