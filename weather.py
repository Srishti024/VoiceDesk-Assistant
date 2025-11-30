import requests

def Weather(city="Delhi"):

    # 1) Get latitude & longitude from city name
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_data = requests.get(geo_url).json()

    if not geo_data.get("results"):
        return "City not found."

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # 2) Get actual weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    weather_data = requests.get(weather_url).json()

    if "current_weather" not in weather_data:
        return "Weather data not available right now."

    temp = weather_data["current_weather"]["temperature"]
    wind = weather_data["current_weather"]["windspeed"]
    code = weather_data["current_weather"]["weathercode"]

    # Weather code meanings (simple)
    conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Foggy",
        51: "Light drizzle",
        61: "Light rain",
        80: "Rain showers",
    }

    desc = conditions.get(code, "Weather condition")

    return f"{temp}°C — {desc} — Wind {wind} km/h"
