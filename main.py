
import time
import pyglet


# %%
controller_man = pyglet.input.ControllerManager()
controllers = controller_man.get_controllers()
print(controllers)
controller = controllers[0]
controller.open()

@controller.event
def on_dpad_motion(controller, vector):
    print(controller, vector)


@controller.event
def on_button_press(controller, button_name):
    print(controller, button_name)

@controller.event
def on_stick_motion(controller, name, vector):
    print(name, vector)

@controller.event
def on_trigger_motion(controller, name, value):
    print(name, value)


while True:
    # Run a single iteration of Pyglet's event handling
    pyglet.clock.tick()           # Allows scheduled events to run
    pyglet.app.platform_event_loop.dispatch_posted_events()  
    time.sleep(0.01)  # sleep to avoid busy-wait

