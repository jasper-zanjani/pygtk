import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.entry = Gtk.Entry(text="World")
        button = Gtk.Button.new_with_mnemonic("Greet")
        button.connect("clicked",self.on_button_clicked, self)
        box.add(self.entry)
        box.add(button)
        self.add(box)

    def on_button_clicked(self, button, parent):
        dialog = Gtk.Dialog(title="Greeting", parent=parent, modal = True)
        dialog.add_button("Ok", Gtk.ResponseType.OK)
        label = Gtk.Label(label=f"Hello, {parent.entry.get_text()}")
        dialog.vbox.pack_start(label, False, False, 0)
        dialog.show_all()
        dialog.run()
        dialog.destroy()

    def on_button_clicked(self, button, parent):
        dialog = Gtk.MessageDialog(
            message_type=Gtk.MessageType.INFO,
            text=f"Hello, {parent.entry.get_text()}",
            parent=parent,
        )
        dialog.add_button("O_K", Gtk.ResponseType.OK)
        dialog.run()
        dialog.destroy()

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