import requests
import time
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import InfluxDBClient, Point
token = 'HI7Bf1mCLsqCjGlpqYMayMHP40aPVf9OquxMwMhtyN2hsfiKLsylI3yjiBvUpzsrNTT86eKrevnUInLttzA9pQ=='
bucket = 'test'
client = InfluxDBClient('http://localhost:8086', token = token, org='weather')

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()


while True:
    def return_weather(city):
        city = "bogota"
        url = f'https://es.wttr.in/{city}?format=j1'

        response = requests.get(url)
        weather_dic = response.json()

        temp_c = weather_dic["current_condition"][0]['temp_C']
        desc_temp = weather_dic["current_condition"][0]['lang_es']
        desc_temp = desc_temp[0]['value']
        humidity = weather_dic['current_condition'][0]['humidity']

        return temp_c, desc_temp, humidity


    def main():
        city = 'Bogota'
        temp_c, desc_temp, humidity = return_weather(city)
        if temp_c != 0 and humidity !=0:
            print(f'La temperatura actual de {city} es {temp_c}°C, {desc_temp} y la humedad es {humidity}%')

            p = Point("AllData").tag("Ciudad", city).field("temperature", float(temp_c)).field('humidity', float(humidity))
            write_api.write(bucket=bucket, org='weather', record=p)


    time.sleep(1)

    if __name__ == '__main__':
        main()