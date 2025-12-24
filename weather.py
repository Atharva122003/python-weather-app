import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print(f"❌ City not found: {city}\n")
            return

        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description'].title()
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Condition: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def main():
    print("☀️ Python Weather App")
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye! 🌤️")
            break
        elif city:
            get_weather(city)
        else:
            print("Please enter a valid city name.\n")

if __name__ == "__main__":
    main()
