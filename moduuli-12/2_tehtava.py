import requests

city_name = input('Enter the name of a city: ')
api_key = '08f1c9900594aed1b611c91432a98723'
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

try:
    response = requests.get(request)
    response.raise_for_status()
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response["main"]["temp"] - 273.15
        weather_desc = json_response["weather"][0]["description"]
        print(f"Weather: {weather_desc}")
        print(f"Temperature: {temp:.1f} °C")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


