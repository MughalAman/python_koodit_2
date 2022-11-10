import requests
api_key = 'YOUR_API_KEY'

def kelvin_to_celsius(kelvin):
    celcius = kelvin - 273.15
    return celcius


if __name__ == '__main__':
    city = input("Enter a city: ")

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(weather_url).json()

    description = response['weather'][0]['description']

    celcius = kelvin_to_celsius(response['main']['temp'])

    print(f"The weather in {city} is {description} and the temperature is {celcius:.1f} degrees Celsius.")