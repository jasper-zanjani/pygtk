import sys
import gi
import random
from gi.repository import Gtk
from enum import Enum, auto

gi.require_version('Gtk','3.0')

class Op(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"

class Equation:
    def __init__(self):
        self.op = random.sample(list(Op),1)[0]
        
        if self.op == Op.ADDITION:
            self.operands = [random.randint(3,20), random.randint(3,20)]
            self.result = sum(self.operands)
        elif self.op == Op.SUBTRACTION:
            self.operands = [random.randint(10,30), random.randint(1,10)]
            self.result = self.operands[0] - self.operands[1]

    def __str__(self):
        return f"{self.operands[0]}\n{self.op.value} {self.operands[1]}\n---\n= {self.result}"


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name
        self.equation = Equation()
        label = Gtk.Label.new(f"{self.equation}")
        self.add(label)
        self.set_size_request(200,100)

class Application(Gtk.Application):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, application_id="org.example.myapp", **kwargs)
        self.window = None
    
    def do_activate(self):
        if not self.window:
            self.window = AppWindow(self.name, application=self, title="PyGTK app")
        self.window.show_all()
        self.window.present()

if __name__ == '__main__':
    app = Application(sys.argv[-1])
    app.run()
