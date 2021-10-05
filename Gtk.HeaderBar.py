import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(-1, -1)
        # headerbar = Gtk.HeaderBar(title=f"Hello, {name}!", subtitle="HeaderBar example", show_close_button=True)
        headerbar = Gtk.HeaderBar()
        headerbar.set_title(f"Hello, World!")
        headerbar.set_subtitle("HeaderBar example")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        button = Gtk.Button(label="Greet")
        button.connect("clicked", self.on_button_clicked, self)
        headerbar.add(button)

        self.entry = Gtk.Entry(text="World", name="entry")
        headerbar.add(self.entry)

    def on_button_clicked(self, button, parent):
        dialog = Gtk.MessageDialog(
            message_type=Gtk.MessageType.INFO,
            text=f"Hello, {parent.entry.get_text()}!",
            parent=parent,
        )
        dialog.add_button("O_K", Gtk.ResponseType.OK)
        dialog.run()
        dialog.destroy()

class HeaderBar(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.example.headerbar")
    
    def do_activate(self):
        self.window = ApplicationWindow(application=self)
        self.window.show_all()
        self.window.present()

if __name__ == '__main__':
    app = HeaderBar()
    app.run()