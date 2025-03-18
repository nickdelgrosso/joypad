from dataclasses import dataclass
import pyxel
import joypad

@dataclass
class App:
    x: float = 0
    y: float = 0

class Controls(joypad.BaseControls):

    def __init__(self, app: App):
        self.app = app
    
    def on_left_stick_move(self, x, y):
        
        self.app.x = x
        self.app.y = y


app = App()
manager = joypad.Manager()
for controller in manager.controllers:
    print(controller.name)
    controller.nintendo_mode = True
    controller.register_callbacks(Controls(app=app))
# manager.listen()

pyxel.init(160, 120, fps=60)

def update():
    manager.dispatch_events()
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(round(80 + 80*app.x) - 10, round(60 - 60*app.y) - 10, 20, 20, 11)


pyxel.run(update, draw)