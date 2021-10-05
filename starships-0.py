import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import csv

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ships = ['USS Enterprise', 'USS Defiant', 'USS Voyager']
        self.treeview = Gtk.TreeView(model=Gtk.ListStore.new((str,)))
        column = Gtk.TreeViewColumn("Ship", Gtk.CellRendererText(), text=0)
        self.treeview.append_column(column)
        for s in ships:
            self.treeview.get_model().append((s,))

        self.add(self.treeview)
        self.set_size_request(-1,-1)


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