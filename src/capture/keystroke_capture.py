from pynput import keyboard
import time


class KeystrokeCapture:
    def __init__(self):
        self.keystrokes = []
        self.press_times = {}

    def _on_press(self, key):
        try:
            char = key.char
            self.press_times[char] = time.time()
        except AttributeError:
            # Ignore special keys (shift, ctrl, etc.)
            pass

    def _on_release(self, key):
        try:
            char = key.char
            press_time = self.press_times.pop(char, None)

            if press_time:
                release_time = time.time()
                self.keystrokes.append({
                    "key": char,
                    "press_time": press_time,
                    "release_time": release_time
                })

        except AttributeError:
            pass

        # Stop when Enter is pressed
        if key == keyboard.Key.enter:
            return False

    def capture(self, prompt="Type your password and press ENTER:"):
        self.keystrokes = []
        self.press_times = {}

        print(prompt)

        with keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        ) as listener:
            listener.join()

        return self.keystrokes