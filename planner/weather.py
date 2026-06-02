import requests

API_KEY = "e7c387845ad6d113cfdb86dc3dbdc5d8"

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    return response.json()