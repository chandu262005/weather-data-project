import requests

# Ask the user for the city name
city_name = input("Enter the city name: ")
API_key = 'fa3b38a2389e98261d4c4150ef6460c3'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"{city_name} Temperature")
    print('Weather is:', data['weather'][0]['description'])
    print('Current temperature is:', data['main']['temp'], '°C')
    print('Feels like:', data['main']['feels_like'], '°C')
    print('Humidity is:', data['main']['humidity'], '%')
else:
    print("City not found or API request failed.")
