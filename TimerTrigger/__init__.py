import datetime
import logging

import azure.functions as func
from .check_weather import get_weather_data

def main(mytimer: func.TimerRequest) -> None:
    api_key ="4a3251a0b240c7ea09c718c2640ab07a"
    city_name ="Chennai"

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Hello World at %s', utc_timestamp)
    
    
    weather_data = get_weather_data(api_key,city_name)
    
    if weather_data:
        print(f"Weather in {city_name}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Weather data not available.")

