from datetime import datetime, timedelta
import threading

# For active windows
from win32gui import GetWindowText, GetForegroundWindow

# Listeners for Mouse and Keyboard Events
from mouse_listener import MouseListener
from keyboard_listener import KeyboardListener

# Logging
from terminaltables import AsciiTable
from textwrap import wrap
import logging, time

from allFiles import FileManager

'''
from window_listener import WindowListener
'''



logging.basicConfig(filename='app.log', format='%(message)s', level=logging.INFO)

class ActivityMonitor:

	def __init__(self):
                self.FM = FileManager()
                self.FM.allFiles(self.FM.basepath)
                self.ML = MouseListener()
                self.KL = KeyboardListener()
                self.start_time = datetime.now()
                self.report_interval_secs = 30 # seconds
                self.update_interval_secs = 5 # seconds
                self.total_clicks = 0
                self.total_keystrokes = 0
                self.last_time_stamp = self.start_time
                self.application_id = '{}{}{}{}{}{}'.format(
								self.start_time.month,
								self.start_time.day,
								self.start_time.year,
								self.start_time.hour,
								self.start_time.minute,
								self.start_time.second
							)

                self.reports = []
                self.last_report_time = self.start_time
                self.url = 'http://lviv.ixioo.com:8030/ActivityTracking'
                print ('Application ID {} initialised at {}'.format(self.application_id, self.start_time))

	def get_opened_files(self, active_window):
                res = []
                for file in self.FM.files:
                        if file in active_window:
                                res.append(self.FM.files[file])
                if res == []:
                        return ['None']
                return res

	def log(self):

		table_data =[
			['Active Window', ''],
			['Keyboard Strokes', ''],
			['Mouse Clicks', ''],
			['Timestamp', ''],
            ['Files Open', '']
		]


		table = AsciiTable(table_data)
		max_width = table.column_max_width(1)

		active_window = GetWindowText(GetForegroundWindow())

		active_window_str = '\n'.join(wrap(active, max_width))
		table.table_data[0][1] = active_window_str

		keyboard_strokes_str = '\n'.join(wrap(str(self.KL.strokes), max_width))
		table.table_data[1][1] = keyboard_strokes_str

		mouse_clicks_str = '\n'.join(wrap(str(self.ML.clicks), max_width))
		table.table_data[2][1] = mouse_clicks_str

		time_stamp_str = '\n'.join(wrap(str(self.last_time_stamp + timedelta(seconds=self.interval)), max_width))
		table.table_data[3][1] = time_stamp_str

		files_opened_str = '\n'.join(wrap('; '.join(self.get_opened_files(active)), max_width))
		table.table_data[4][1] = files_opened_str


		logging.info(table.table)

	def send_report(self, report):
		requests.post(
			url=self.url,
			data=report
		)


	def send_reports(self):
		# requests.post(
		# 	url=self.url,
		# 	data=self.reports
		# )
		print ('TOTAL: {}'format(len(self.reports)))
		print (self.reports)
		self.last_report_time = report_time
		self.reports = []

	def reset(self):
		self.ML.reset_clicks()
		self.KL.reset_strokes()
		self.last_time_stamp = datetime.now()

	def update(self):
		self.total_clicks += self.ML.get_clicks()
		self.total_keystrokes += self.KL.get_strokes()

		report_time = datetime.now()
		active_window = GetWindowText(GetForegroundWindow())
		opened_files = self.get_opened_files(active_window)
		report = {
			"ApplicationID": self.application_id,
			"InfoDataTime": report_time,
			"InfoDuration": report_time - self.start_time,
			"TitleActiveWindows": active_window,
			"MouseClicks": self.total_clicks,
			"KeysPressed": self.total_keystrokes,
			"OpenDocuments": opened_files
		}
		#print (report)

		# send report
		self.reports.append(report)



	def run(self):
		while True:
			now = datetime.now()
			upd_diff = now - self.last_time_stamp
			rep_diff = now - self.last_report_time
			#print (upd_diff.seconds, rep_diff.seconds)
			if upd_diff.seconds >= self.update_interval_secs:
				# self.log()
				self.update()
				self.reset()

			if rep_diff.seconds >= self.report_interval_secs:
				self.send_reports()
				
			time.sleep(1)
			



	def monitor(self):
		t0 = threading.Thread(target=self.run).start()
		t1 = threading.Thread(target=self.ML.start).start()
		t2 = threading.Thread(target=self.KL.start).start()

if __name__ == '__main__':
	am = ActivityMonitor()
	am.monitor()
