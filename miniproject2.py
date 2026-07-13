import requests
city=input("Enter city:")
url= f"https://wttr.in/{city}?format=j1"
response=requests.get(url)
data=response.json()
temp=data["current_condition"][0]["temp_C"]
print("Temperature:",temp,"C")
humidity=data["current_condition"][0]["humidity"]
condition=data["current_condition"][0]["weatherDesc"][0]["value"]
windspeed=data["current_condition"][0]["windspeedKmph"]
print("Humidity",humidity,"%")
print("weather:",condition)
print("Wind Speed:",windspeed,"km/h")
print("\n -----hourly forecast ----------")
hourly=data["weather"][0]["hourly"]
for hour in hourly:
    time=hour["time"]
    temp=hour["tempC"]
    Humidity=hour["humidity"]
    desc=hour["weatherDesc"][0]["value"]
    print(f"Time: {time} ,Temp: {temp}C , Humidity: {Humidity}%, Condition: {desc}")

