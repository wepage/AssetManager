import datetime


class Debugger:
    # Class variable to control logging state
    is_active = True

    @classmethod
    def log(cls, type, message):
        if cls.is_active:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[DEBUGGER][{current_time}] [{type}] {message}", flush=True)
