from win32gui import GetWindowText, GetForegroundWindow

from window_listener import WindowListener
import time


wl = WindowListener()
wins = wl.get_window_names()

current = GetWindowText(GetForegroundWindow())

print (wins)
print (current)


time.sleep(5)


print (GetWindowText(GetForegroundWindow()))
