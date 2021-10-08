import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

# builder = Gtk.Builder()
# builder.add_from_file('user_interface.glade')
builder = Gtk.Builder.new_from_file("user_interface.glade")

class Handler(object):
    def __init__(self):

        self.display = builder.get_object('display')
        self.display.set_text('0')


builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
