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
    
    def get_clicks(self):
        return self.clicks

    def reset_clicks(self):
        self.clicks = 0
        
if __name__ == '__main__':
    ml = MouseListener()
    ml.start()

