import requests

def get_weather_data(api_key,city_name):
    base_url="http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city_name,
        "appid":api_key,
        "units":"matric"
    }

    try:
        response = requests.get(base_url,params=params)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None