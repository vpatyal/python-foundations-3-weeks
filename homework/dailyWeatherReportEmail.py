import requests
import json
from dateutil import parser
from datetime import date
import smtplib
from email.message import EmailMessage

# inputs for open meteo weather API
daily_params = "weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset"
temperature_unit = "fahrenheit"
timezone = "America%2FNew_York"
start_date = date.today()
end_date = date.today()


def get_lon_lat(city, stateCode, countryCode, geoAPIKey):
    geocoding_api_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{stateCode},{countryCode}&appid={geoAPIKey}"
    response_geocoding_api = requests.get(geocoding_api_url)
    print(f"\nResponse Code from geoCoding API= {response_geocoding_api.status_code}")
    geocoding_api_data = json.loads(response_geocoding_api.text)

    if (response_geocoding_api.status_code == 200) & (len(geocoding_api_data) >= 1):
        geocoding_data = geocoding_api_data[0]
        print(f"city      : {geocoding_data['name']} \nstate     : {geocoding_data.get('state', 'Not found')} \ncountry   : {geocoding_data['country']}")
        print(f"latitude  : {geocoding_data['lat']}  \nlongitude : {geocoding_data['lon']}")
        return geocoding_api_data[0]['lat'], geocoding_api_data[0]['lon'], 0
    else:
        if len(geocoding_api_data) == 0:
            print(f"\n{city} {stateCode} {countryCode} is not available in the Geocoding database.")
        else:
            geocoding_error_response = geocoding_api_data[0]
            print(geocoding_api_data)
            print(f"\nAPI responded with error: {geocoding_error_response['message']}, error code: {geocoding_error_response['cod']}")
        return 0, 0, 1


def get_weather_details(latitude, longitude):
    weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily={daily_params}&temperature_unit={temperature_unit}&timezone={timezone}&start_date={start_date}&end_date={end_date}"
    response_openMeteo_api = requests.get(weather_api_url)
    print(f"\nResponse Code from Open Meteo weather API= {response_openMeteo_api.status_code}")
    weather_api_data = json.loads(response_openMeteo_api.text)

    if response_openMeteo_api.status_code == 200:
        weather_desc = get_weather_desc(weather_api_data['daily']['weathercode'][0])
        max_temp_in_c = f_to_c(weather_api_data['daily']['temperature_2m_max'][0])
        min_temp_in_c = f_to_c(weather_api_data['daily']['temperature_2m_min'][0])
        if weather_desc != 'NotAvailable':
            print(f"Weather             ==> {weather_desc}")
        print(f"Date                : {start_date}")
        print(f"Maximum temperature : {weather_api_data['daily']['temperature_2m_max'][0]} °F ({max_temp_in_c} °C)")
        print(f"Minimum temperature : {weather_api_data['daily']['temperature_2m_min'][0]} °F ({min_temp_in_c} °C)")
        print(f"Sunrise time        : {parser.parse(weather_api_data['daily']['sunrise'][0])}")
        print(f"Sunset  time        : {parser.parse(weather_api_data['daily']['sunset'][0])}")
        return[weather_desc, weather_api_data['daily']['temperature_2m_max'][0], weather_api_data['daily']['temperature_2m_min'][0], 
        max_temp_in_c, min_temp_in_c,  parser.parse(weather_api_data['daily']['sunrise'][0]),parser.parse(weather_api_data['daily']['sunset'][0]), 0]
    else:
        if weather_api_data['error'] == True:
            print(f"\nAPI responded with error: {weather_api_data['reason']}")
        return["None", 0, 0, 0, 0, 0, 0, 1]

def f_to_c(temp_f):
    return round(((temp_f - 32) * 5/9), 1)

def get_weather_desc(weather_code):
    weather_desc_dict = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light intensity",
        53: "Drizzle: moderate intensity",
        55: "Drizzle: dense intensity",
        56: "Freezing Drizzle: Light intensity",
        57: "Freezing Drizzle: Dense intensity",
        61: "Rain: Slight intensity",
        63: "Rain: Moderate intensity",
        65: "Rain: Heavy intensity",
        66: "Freezing Rain: Light intensity",
        67: "Freezing Rain: Heavy intensity",
        71: "Snow fall: Slight intensity",
        73: "Snow fall: Moderate intensity",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight",
        81: "Rain showers: Moderate",
        82: "Rain showers: Violent",
        85: "Snow showers slight",
        86: "Snow showers heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    return weather_desc_dict.get(weather_code, 'NotAvailable')

def get_user_input():
    user_input = input("Enter city, state and country code (e.g. Edison NJ USA) : ")
    print(user_input)
    return user_input

def send_email(msgContent):
    msg = EmailMessage()
    msg["to"] = "patyal@gmail.com"
    msg["from"] = "sujanianvp@gmail.com"
    msg["Subject"] = f"Daily Weather report for {date.today()}"
    msg.set_content(msgContent)
    config_file = open("C:\\Users\\vpatyal\\Dropbox\\learn\\repos\\python-foundations-3-weeks\\homework\\config.json")
    gmail_cfg = json.load(config_file)
    print(gmail_cfg)
    with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
        smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
        smtp.send_message(msg)   
        print("Email sent ! ")

def main():
    #  user_input = get_user_input()
    #  user_input_list = user_input.split(' ')
    #  print(user_input_list)
    #  city = user_input_list[0]
    #  stateCode = user_input_list[1]
    #  countryCode = user_input_list[2]
    latitude, longitude, lon_lat_return_code = get_lon_lat(city="Edison", stateCode="NJ", countryCode="US", geoAPIKey="b76a765eb4d5c56625624376db25b91a")
    print(f"returned values: {latitude}, {longitude}, {lon_lat_return_code}")
    if lon_lat_return_code == 0:
       weather_data = get_weather_details(latitude, longitude)
       if weather_data[7] == 0:
           print(f"returned values: {weather_data}")
           email_message = f"""Good morning VP, here is your daily weather report for Edison NJ US:
           Date                : {date.today()}
           Weather             ==> {weather_data[0]}
           Max temperature     : {weather_data[1]} °F ({weather_data[3]} °C)
           Min temperature     : {weather_data[2]} °F ({weather_data[4]} °C)
           Sunrise             : {weather_data[5]}
           Sunset              : {weather_data[6]}           
           """
       else:
           email_message = f"""Problem with the Daily weather script @Open Meteo API call, returned values: {weather_data}""" 
    else:
        email_message = f"""Problem with the Daily weather script @geoCoding API call, RC: {lon_lat_return_code}""" 
    
    send_email(email_message)

if __name__ == '__main__':
    main()