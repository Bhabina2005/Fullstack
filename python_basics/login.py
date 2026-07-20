import requests
response = requests.get(
    "https://api.github.com/users/python"
)
data = response.json()
print(data)
