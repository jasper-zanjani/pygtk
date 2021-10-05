import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import csv

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        with open('/home/jasper/dogfood/csv/starships.csv',mode='r') as f:
            reader = csv.reader(f)
            self.headers = [h.title() for h in next(reader)]
            self.data = [r for r in reader]

        self.treeview = Gtk.TreeView(model=Gtk.ListStore.new((str,str,str,str)))
        for h in self.headers:
            column = Gtk.TreeViewColumn(h, Gtk.CellRendererText(), text=self.headers.index(h))
            column.set_sort_column_id(self.headers.index(h))
            self.treeview.append_column(column)

        for r in self.data:
            self.treeview.get_model().append(r)

        self.treeview.connect('row-activated', self.on_row_activated)

        self.add(self.treeview)
        self.set_size_request(-1,-1)

    def on_row_activated(self, treeview, path, col):
        model = treeview.get_model()
        dialog = Gtk.MessageDialog(
            message_type=Gtk.MessageType.INFO,
            text=model[path][:],
            parent = self
        )
        dialog.add_button("OK", Gtk.ResponseType.OK)
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