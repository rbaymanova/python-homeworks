from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("tbody").find_all("tr")

weather_data = []
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temperature = int(cols[1].text.replace("°C", ""))  
    condition = cols[2].text
    weather_data.append({"day": day, "temperature": temperature, "condition": condition})

print("Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}C, {entry['condition']}")

hottest_day = max(weather_data, key=lambda x: x["temperature"])
print(f"Hottest day: {hottest_day['day']} ({hottest_day['temperature']}C)")

sunny_days = [day["day"] for day in weather_data if day["condition"] == "Sunny"]
print(f"Sunny days: {', '.join(sunny_days)}")

average_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"Average Temperature: {average_temp:.2f}C")
