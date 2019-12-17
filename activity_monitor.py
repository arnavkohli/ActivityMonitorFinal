from datetime import datetime, timedelta
from mouse_listener import MouseListener
from keyboard_listener import KeyboardListener
# from application_listener import ApplicationListener
from window_listener import WindowListener
import threading, logging
from terminaltables import AsciiTable
from textwrap import wrap
from allFiles import FileManager
from win32gui import GetWindowText, GetForegroundWindow


logging.basicConfig(filename='app.log', format='%(message)s', level=logging.INFO)

class ActivityMonitor:

	def __init__(self):
		self.ML = MouseListener()
		self.KL = KeyboardListener()
		# self.AL = ApplicationListener()
		#self.WL = WindowListener()
		self.last_time_stamp = datetime.now()

		self.interval = 5

		self.FM = FileManager()
		self.FM.allFiles(self.FM.basepath)
		print ('Intialised')

	def get_open_files(self, wins):
                res = []
                for file in self.FM.files:
                        if file in wins:
                                res.append(self.FM.files[file])
                if res == []:
                        return ['None']
                return res

	def log(self):

		table_data =[
			['Applications Open', ''],
			['Keyboard Strokes', ''],
			['Mouse Clicks', ''],
			['Timestamp', ''],
                        ['Files Open', '']
		]


		table = AsciiTable(table_data)
		max_width = table.column_max_width(1)

		#wins = self.WL.get_window_names()
		active = GetWindowText(GetForegroundWindow())

		# wrapped_string0 = '\n'.join(wrap('; '.join(self.AL.get_processes()), max_width))
		# table.table_data[0][1] = wrapped_string0
		windows_open = '\n'.join(wrap(active, max_width))
		table.table_data[0][1] = windows_open

		keyboard_strokes = '\n'.join(wrap(str(self.KL.strokes), max_width))
		table.table_data[1][1] = keyboard_strokes

		mouse_clicks = '\n'.join(wrap(str(self.ML.clicks), max_width))
		table.table_data[2][1] = mouse_clicks

		time_stamp = '\n'.join(wrap(str(self.last_time_stamp + timedelta(seconds=self.interval)), max_width))
		table.table_data[3][1] = time_stamp

		files = '\n'.join(wrap('; '.join(self.get_open_files(active)), max_width))
		table.table_data[4][1] = files


		print (table.table)
		# print (max_width)
		logging.info(table.table)

	def reset(self):
		self.ML.clicks = 0
		self.KL.strokes = 0
		self.last_time_stamp = datetime.now()


	def update(self):
		while True:
			if (datetime.now() - self.last_time_stamp).seconds >= self.interval:
				self.log()
				self.reset()


	def monitor(self):
		t0 = threading.Thread(target=self.update).start()
		t1 = threading.Thread(target=self.ML.start).start()
		t2 = threading.Thread(target=self.KL.start).start()

if __name__ == '__main__':
	am = ActivityMonitor()
	am.monitor()
