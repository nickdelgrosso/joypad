
import time
import pyglet

class BaseControllerInterface:

    def on_a_button_push(self):
         print('pressed A!')

    def on_a_button_release(self): ...
    def on_b_button_push(self):  ...
    def on_b_button_release(self): ...
    def on_x_button_push(self):  ...
    def on_x_button_release(self): ...
    def on_y_button_push(self):  ...
    def on_y_button_release(self): ...
    def on_left_shoulder_button_push(self):  ...
    def on_left_shoulder_button_release(self): ...
    def on_right_shoulder_button_push(self):  ...
    def on_right_shoulder_button_release(self): ...
    def on_left_stick_button_push(self):  ...
    def on_left_stick_button_release(self): ...
    def on_right_stick_button_push(self):  ...
    def on_right_stick_button_release(self): ...
    def on_start_button_push(self):  ...
    def on_start_button_release(self): ...
    def on_back_button_push(self):  ...
    def on_back_button_release(self): ...
    def on_guide_button_push(self):  ...
    def on_guide_button_release(self): ...
    def on_dpad_center(self): ...
    def on_dpad_up(self): ...
    def on_dpad_up_left(self): ...
    def on_dpad_left(self): ...
    def on_dpad_down_left(self): ...
    def on_dpad_down(self): ...
    def on_dpad_down_right(self): ...
    def on_dpad_right(self): ...
    def on_dpad_up_right(self): ...

    


def register_interface(controller: pyglet.input.Control, interface: BaseControllerInterface):
        
        @controller.event
        def on_dpad_motion(controller, vector):
            funs = {
                 (0, 0): interface.on_dpad_center,
                 (0, 1): interface.on_dpad_up,
                 (-1, 1): interface.on_dpad_up_left,
                 (-1, 0): interface.on_dpad_left,
                 (-1, -1): interface.on_dpad_down_left,
                 (0, -1): interface.on_dpad_down,
                 (1, 1): interface.on_dpad_down_right,
                 (1, 0): interface.on_dpad_right,
                 (1, 1): interface.on_dpad_up_right,
            }
            print(controller, vector.x, vector.y)


        @controller.event
        def on_button_press(controller, button_name):
            print('pressed', button_name)
            funs = {
                 'x': interface.on_x_button_push,
                 'y': interface.on_y_button_push,
                 'a': interface.on_a_button_push,
                 'b': interface.on_b_button_push,
                 'leftshoulder': interface.on_left_shoulder_button_push,
                 'rightshoulder': interface.on_right_shoulder_button_push,
                 'leftstick': interface.on_left_stick_button_push,
                 'rightstick': interface.on_right_stick_button_push,
                 'start': interface.on_start_button_push,
                 'back': interface.on_back_button_push,
                 'guide': interface.on_guide_button_push,
            }
            fun = funs[button_name]
            fun()

        @controller.event
        def on_button_release(controller, button_name):
            print('released', button_name)
            funs = {
                 'x': interface.on_x_button_release,
                 'y': interface.on_y_button_release,
                 'a': interface.on_a_button_release,
                 'b': interface.on_b_button_release,
                 'leftshoulder': interface.on_left_shoulder_button_release,
                 'rightshoulder': interface.on_right_shoulder_button_release,
                 'leftstick': interface.on_left_stick_button_release,
                 'rightstick': interface.on_right_stick_button_release,
                 'start': interface.on_start_button_release,
                 'back': interface.on_back_button_release,
                 'guide': interface.on_guide_button_release,
            }
            fun = funs[button_name]
            fun()




        # @controller.event
        # def on_stick_motion(controller, name, vector):
        #     print(name, vector)

        # @controller.event
        # def on_trigger_motion(controller, name, value):
        #     print(name, value)


        
        

    
# %%
controller_man = pyglet.input.ControllerManager()
controllers = controller_man.get_controllers()
print(controllers)
controller = controllers[0]
controller.open()

interface = BaseControllerInterface()
register_interface(controller, interface)


while True:
    # Run a single iteration of Pyglet's event handling
    pyglet.clock.tick()           # Allows scheduled events to run
    pyglet.app.platform_event_loop.dispatch_posted_events()  
    time.sleep(0.01)  # sleep to avoid busy-wait

