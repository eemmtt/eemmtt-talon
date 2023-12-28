from talon import Module, Context
from .hovering import Hover
import win32api, win32con 

mod = Module()
mod.tag("hovering", desc="Tag indicates whether mouse is hovering")
ctx = Context()
hover = Hover()

@mod.action_class
class MouseActions:
    def mouse_reset(dx: int, dy: int):
        """Moves mouse to make cursor visible on windows profile login"""
        win32api.mouse_event(
            win32con.MOUSEEVENTF_MOVE,
            int(dx),
            int(dy),
            0,
            0)
    
    def mouse_hover(state: str):
        """Keeps mouse hovering in initiated position"""
        def start():
            if "user.hovering" in ctx.tags:
                return
            ctx.tags = ["user.hovering"]
            hover.start()
        def stop():
            if "user.hovering" not in ctx.tags:
                return
            ctx.tags = []
            hover.stop()
            
        def toggle():
            if "user.hovering" in ctx.tags:
                ctx.tags = []
                hover.stop()
            else:
                ctx.tags = ["user.hovering"]
                hover.start()
        
        states = {
            "START": start,
            "STOP": stop,
            "TOGGLE": toggle,
        }
        
        try:
            states[state.upper()]()
        except KeyError:
            print(f"'{state}' is not a valid state for mouse_hover()-")
            print(f"\tValid states are: {list(states.keys())}")