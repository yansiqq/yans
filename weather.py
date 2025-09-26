import requests
import sys

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"].capitalize()

            print(f"🌤 Weather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")
        else:
            print("❌ Error:", data.get("message", "Unknown error"))
    except Exception as e:
        print("⚠️ Failed to fetch weather data:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
    else:
        city = " ".join(sys.argv[1:])
        get_weather(city)
