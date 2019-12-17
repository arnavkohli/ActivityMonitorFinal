from pywinauto import Desktop

class WindowListener:

	def __init__(self):
		pass

	def get_window_names(self):
		windows = Desktop(backend='uia').windows()
		return [w.window_text() for w in windows]
	def get_windows(self):
		windows = Desktop(backend='uia').windows()
		return [w for w in windows]
