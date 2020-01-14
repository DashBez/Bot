import os
basedir = os.path.abspath(os.path.dirname(__file__)) 



WEATHER_DEFAULT_CITY = 'Saint-Petersburg'
WEATHER_API_KEY = "209eedf3a15248dab5d40221191012"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')