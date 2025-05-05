import requests

def get_weather(city):
    api_key = "Add Your API KEY Here"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Debugging: print the full response
    print("API Response:", data)

    if response.status_code != 200 or "main" not in data:
        return f"❌ Could not retrieve weather for {city}. Reason: {data.get('message', 'Unknown error')}"

    try:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        return (
            f"🌤️ Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {description.capitalize()}"
        )
    except KeyError as e:
        return f"⚠️ Failed to parse weather data: missing field {e}"
