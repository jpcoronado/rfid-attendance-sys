import eel
eel.init('web')

@eel.expose
def my_python_method(param1, param2):
	print(param1, param2)

def print_return(n):
	print('Return from JavaScript: ', n)

eel.start('main.html', block=False)

eel.js_what_year()(print_return)

@eel.expose
def py_what_year():
	import datetime
	return "The year is " + str(datetime.datetime.now().year)

while True:
	eel.sleep(10)