from datetime import datetime

from flask import Flask

from req import get_weather

city_id = 524901
apikey = '24901&APPID=1f32ee241668ef1b8bf43d5d44aab63c'

app = Flask(__name__)


@app.route('/')
def index():
	url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric'%(city_id, apikey)
	weather = get_weather(url)

	print(weather)
	
	cur_date = datetime.now().strftime('%d.%m.%Y')
	result = '<p><b>Температура:</b> %s</p>' %weather['main']['temp']
	result += '<p><b>Город:</b> %s</p>' %weather['name']
	result += '<p><b>Дата:</b> %s</p>' %cur_date
	return result

if __name__ == "__main__":
	app.run()