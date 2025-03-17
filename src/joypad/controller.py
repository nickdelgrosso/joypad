from abc import ABC, abstractmethod

class BaseControllerCallbacks:
    """
    Controller event callbacks.  Inherit from this class to make your own behavior.

    Example:
    ```python
    class PrintControls(BaseControllerCallbacks):
        def on_a_button_push(self):
            print('Jump!')
    ```
    """

    def on_a_button_push(self): ...
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
    def on_left_stick_move(self, x: float, y: float): ...
    def on_right_stick_move(self, x: float, y: float): ...
    def on_left_trigger_move(self, value: float): ...
    def on_right_trigger_move(self, value: float): ...

    

class IController:

    @property
    @abstractmethod
    def name(self) -> str:
        ...


    @abstractmethod    
    def register_callbacks(self, callbacks: BaseControllerCallbacks) -> None:
        ...