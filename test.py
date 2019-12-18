import requests
import datetime

url = 'http://lviv.ixioo.com:8001/ActivityTracking'


data1 = {"ApplicationID": "TestID",
"InfoDataTime": str(datetime.datetime.now()),
"InfoDuration": 12345,
"TitleActiveWindows": "PyCharm",
"MouseClicks": 999,
"KeysPressed": 500,
"OpenDocuments": ['aaa', 'bbb', 'ccc']}

data2 = {"ApplicationID": "TestID",
"InfoDataTime": str(datetime.datetime.now()),
"InfoDuration": 12345,
"TitleActiveWindows": "PyCharm",
"MouseClicks": 999,
"KeysPressed": 500,
"OpenDocuments": ['aaa', 'bbb', 'ccc']}

data3 = {"ApplicationID": "TestID",
"InfoDataTime": str(datetime.datetime.now()),
"InfoDuration": 12345,
"TitleActiveWindows": "PyCharm",
"MouseClicks": 999,
"KeysPressed": 500,
"OpenDocuments": ['aaa', 'bbb', 'ccc']}

array = [
	data1,
	data2,
	data3
]


r = requests.post(url=url, json=array)

print (r.text)
