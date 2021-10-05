import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.textbox = Gtk.Entry()

        button = Gtk.Button.new_with_mnemonic("_Add")
        button.connect("clicked", self.on_button_clicked)

        self.gen_treeview()
        scrolled_win = Gtk.ScrolledWindow.new(None,None)
        scrolled_win.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_win.add(self.treeview)

        box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.add(self.textbox)
        box.add(button)
        box.add(scrolled_win)
        self.add(box)
        self.set_size_request(200,200)

    def get_liststore(self):
        store = Gtk.ListStore.new((str,))
        store.append(["Socrates"])
        store.append(["Plato"])
        store.append(["Aristotle"])
        return store

    def gen_treeview(self):
        self.treeview = Gtk.TreeView.new()
        self.treeview.set_model(self.get_liststore())
        self.treeview.append_column(Gtk.TreeViewColumn("Greeks", Gtk.CellRendererText.new(), text=0))
        # self.treeview.append_column(Gtk.TreeViewColumn("Place of birth", Gtk.CellRendererText.new(), text=1))

    def on_button_clicked(self, button):
        model = self.treeview.get_model()
        model.append((self.textbox.get_text(),))


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.example.myapp')

    def do_activate(self):
        self.window = ApplicationWindow(application=self, title="Greeks")
        self.window.show_all()
        self.window.present()


if __name__ == '__main__':
    app = Application()
    app.run()