from pynput.keyboard import Key, Listener


class KeyboardListener:

    def __init__(self):
        self.strokes = 0


    def start(self):
        # Collect events until released
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


    def on_press(self, key):
        self.strokes += 1

    def on_release(self, key):
        print('{0} release'.format(key))
        if key == Key.esc:
            # Stop listener
            return False
if __name__ == '__main__':
    kl = KeyboardListener()
    kl.start()
