from talon import Module
import win32api, win32con 

mod = Module()

@mod.action_class
class MouseActions:
    def mouse_reset(dx: int, dy: int):
        """Moves mouse for cursor visibility on windows profile login"""
        win32api.mouse_event(
            win32con.MOUSEEVENTF_MOVE,
            int(dx),
            int(dy),
            0,
            0)