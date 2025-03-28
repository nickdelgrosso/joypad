# Joypad

`joypad` is a lightweight Python library for detecting and interacting with standard two-stick game controllers (plus triggers, buttons, and more). It uses [Pyglet](https://github.com/pyglet/pyglet) under the hood to handle controller events asynchronously.

## Features

- **Simple Callbacks**: Define custom actions for button presses, trigger pulls, joystick movements, etc.  
- **Multi-Controller Support**: Detect and manage multiple connected controllers at once.  
- **Asynchronous Listening**: Controllers are polled in a separate thread, so your application stays responsive.  
- **Extendable**: Inherit from `BaseControllerCallbacks` to create rich, customized game inputs.

## Installation

1. Ensure you have [Python 3.7+](https://www.python.org/) installed.
2. Install `joypad` (once it’s available on PyPI):
   ```bash
   pip install joypad
   ```
3. That’s it! You’re ready to start using `joypad`.

## Getting Started

Here’s a quick example showing how to set up custom callbacks and start listening to events:

```python
import time
from joypad import BaseControls, Manager

# 1. Define your custom callbacks by extending BaseControls
class Controls(BaseControls):
    def __init__(self, name=""):
        self.name = name

    def on_a_button_push(self):
        print(f'{self.name} Pressed A.')

    def on_left_stick_move(self, x, y):
        print(f'{self.name} Moved Left Stick:', x, y)

    def on_right_trigger_move(self, value):
        print(f'{self.name} Pulled Right Trigger to Level {value}')

# 2. Create a Controller Manager and start the event detection loop
manager = Manager()
manager.listen()  # starts background thread for event polling. 


# 3. Get connected controllers and register your custom callbacks
controllers = manager.controllers
print(f'Detected {len(controllers)} controller{"s" if len(controllers) != 1 else ""}.')
for idx, controller in enumerate(controllers, start=1):
    controller.nintendo_mode = True  # if you want the nintendo button layout.
    controller.register_callbacks(Controls(f'Player {idx}'))

# 4. Keep your main application running
while True:
    # manager.dispatch_events()  # if you don't have listen() running on another thread, otherwise not needed.
    time.sleep(1)
```

When you run this script, `joypad` will print out the button presses, stick movements, and trigger activity for each detected controller.

---

## Callback Reference

Below is a reference table for all the callback methods you can override in your subclass of `BaseControllerCallbacks`. Each method corresponds to a specific controller event.

| **Method**                                | **Signature**                             | **Description**                                                                        |
|-------------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------|
| `on_a_button_push`                        | `on_a_button_push()`                      | Called when the A button is pressed.                                                   |
| `on_a_button_release`                     | `on_a_button_release()`                   | Called when the A button is released.                                                  |
| `on_b_button_push`                        | `on_b_button_push()`                      | Called when the B button is pressed.                                                   |
| `on_b_button_release`                     | `on_b_button_release()`                   | Called when the B button is released.                                                  |
| `on_x_button_push`                        | `on_x_button_push()`                      | Called when the X button is pressed.                                                   |
| `on_x_button_release`                     | `on_x_button_release()`                   | Called when the X button is released.                                                  |
| `on_y_button_push`                        | `on_y_button_push()`                      | Called when the Y button is pressed.                                                   |
| `on_y_button_release`                     | `on_y_button_release()`                   | Called when the Y button is released.                                                  |
| `on_left_shoulder_button_push`            | `on_left_shoulder_button_push()`          | Called when the left shoulder (LB) button is pressed.                                  |
| `on_left_shoulder_button_release`         | `on_left_shoulder_button_release()`       | Called when the left shoulder (LB) button is released.                                 |
| `on_right_shoulder_button_push`           | `on_right_shoulder_button_push()`         | Called when the right shoulder (RB) button is pressed.                                 |
| `on_right_shoulder_button_release`        | `on_right_shoulder_button_release()`      | Called when the right shoulder (RB) button is released.                                |
| `on_left_stick_button_push`               | `on_left_stick_button_push()`             | Called when the user presses the left stick button (i.e., clicks the stick).           |
| `on_left_stick_button_release`            | `on_left_stick_button_release()`          | Called when the user releases the left stick button.                                   |
| `on_right_stick_button_push`              | `on_right_stick_button_push()`            | Called when the user presses the right stick button (i.e., clicks the stick).          |
| `on_right_stick_button_release`           | `on_right_stick_button_release()`         | Called when the user releases the right stick button.                                  |
| `on_start_button_push`                    | `on_start_button_push()`                  | Called when the Start button is pressed.                                               |
| `on_start_button_release`                 | `on_start_button_release()`               | Called when the Start button is released.                                              |
| `on_back_button_push`                     | `on_back_button_push()`                   | Called when the Back button is pressed.                                                |
| `on_back_button_release`                  | `on_back_button_release()`                | Called when the Back button is released.                                               |
| `on_guide_button_push`                    | `on_guide_button_push()`                  | Called when the Guide button (often the Xbox button) is pressed.                       |
| `on_guide_button_release`                 | `on_guide_button_release()`               | Called when the Guide button is released.                                              |
| `on_dpad_center`                          | `on_dpad_center()`                        | Called when the D-Pad returns to center (neutral) position.                            |
| `on_dpad_up`                              | `on_dpad_up()`                            | Called when the D-Pad is pressed up.                                                   |
| `on_dpad_up_left`                         | `on_dpad_up_left()`                       | Called when the D-Pad is pressed diagonally up-left.                                   |
| `on_dpad_left`                            | `on_dpad_left()`                          | Called when the D-Pad is pressed left.                                                 |
| `on_dpad_down_left`                       | `on_dpad_down_left()`                     | Called when the D-Pad is pressed diagonally down-left.                                 |
| `on_dpad_down`                            | `on_dpad_down()`                          | Called when the D-Pad is pressed down.                                                 |
| `on_dpad_down_right`                      | `on_dpad_down_right()`                    | Called when the D-Pad is pressed diagonally down-right.                                |
| `on_dpad_right`                           | `on_dpad_right()`                         | Called when the D-Pad is pressed right.                                                |
| `on_dpad_up_right`                        | `on_dpad_up_right()`                      | Called when the D-Pad is pressed diagonally up-right.                                  |
| `on_left_stick_move`                      | `on_left_stick_move(x: float, y: float)`  | Called when the left stick moves, providing the new X/Y values.                        |
| `on_right_stick_move`                     | `on_right_stick_move(x: float, y: float)` | Called when the right stick moves, providing the new X/Y values.                       |
| `on_left_trigger_move`                    | `on_left_trigger_move(value: float)`       | Called when the left trigger is moved (range typically 0.0 to 1.0).                    |
| `on_right_trigger_move`                   | `on_right_trigger_move(value: float)`      | Called when the right trigger is moved (range typically 0.0 to 1.0).                   |

### Notes on Usage

- You only need to override the methods you care about. If you don’t define a callback, it will simply be ignored.  
- The ranges for stick movement (`x`, `y`) and trigger movement (`value`) may vary depending on the controller and OS drivers but typically are normalized between -1.0 to 1.0 for sticks and 0.0 to 1.0 for triggers.

---

## Troubleshooting

1. **No controllers detected**  
   - Make sure your controller is properly plugged in or paired (for wireless).  
   - Check if other applications can see it. If not, you may need to install drivers.

2. **Callback Methods Not Firing**  
   - Verify you’ve spelled and implemented the callback method correctly.  
   - Ensure you use `register_callbacks()` on the correct controller object, and that `controller_manager.listen()` has been called.

3. **Multiple Controllers**  
   - Each connected controller is managed separately. Call `controller.register_callbacks(...)` for each controller.

---

## Contributing

Contributions are welcome! If you have ideas, bug reports, or feature requests:
1. Open an issue describing your idea or the problem you found.
2. Submit a pull request if you want to implement the fix or feature yourself.

## License

`joypad` is distributed under the MIT License. See [LICENSE](./LICENSE) for details.

---

Happy gaming! Feel free to modify the callback methods to shape your game’s input logic exactly how you want. If you have any questions, please open an issue on GitHub or reach out to the community.