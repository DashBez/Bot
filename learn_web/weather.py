import requests


def weather_in_city (city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params ={
        "key" : "209eedf3a15248dab5d40221191012",
        "q":  city_name,
        "format": "json",
        "num_of_days":1,
        "lang":"ru"
    }
    result = requests.get(weather_url,params = params)
    weather = result.json()
    if "data" in weather:
        if "current_condition" in weather["data"]:
            try:
                return(weather["data"]["current_condition"][0])
            except(IndexError,TypeError):
                return False
    return weather

if __name__ == "__main__":
    print(weather_in_city('Saint-Petersburg'))