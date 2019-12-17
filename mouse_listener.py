from pynput.mouse import Listener



class MouseListener:
    def __init__(self):
        self.clicks = 0

    def start(self):
        # Collect events until released
        with Listener(
                on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        self.clicks += 1
        print ('Pressed')
        # print('{0} at {1}'.format(
        #     'Pressed' if pressed else 'Released',
        #     (x, y)))
        # if not pressed:
        #     # Stop listener
        #     return False
if __name__ == '__main__':
    ml = MouseListener()
    ml.start()

