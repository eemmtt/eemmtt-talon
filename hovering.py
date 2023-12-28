from talon import cron, ctrl
import win32api
from functools import wraps

def arg_logger(func):
            @wraps(func)
            def new_func(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except:
                    print(f"My args were: {str(args)}, {str(kwargs)}")
                    raise

            return new_func

class Hover:
    def __init__(self) -> None:
        self.pos = (0,0)
        self.job = None

    def on_interval(self) -> None:
        win32api.SetCursorPos(self.pos)

    @arg_logger
    def start(self) -> None:
        self.pos = ctrl.mouse_pos()
        self.job = cron.interval("4ms", self.on_interval)

    @arg_logger
    def stop(self) -> None:
        cron.cancel(self.job)

