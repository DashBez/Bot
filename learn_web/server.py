from flask import Flask
from weather import weather_in_city


app = Flask(__name__)

@app.route('/')    #декоратор 

def index():
    weather = weather_in_city("Saint-Petersburg")
    return f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    #   "Погода: {weather}".format(weather['temp_C']))
    #+"ощущается как: "+weather["FeelsLikeC"])

if __name__ == "__main__":
    app.run()