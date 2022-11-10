import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url).json()

print(response['value'])