#!/usr/local/bin/python

import requests
import time

forecast_api_key = "976077bc200e901910c9111801f30434"

ip_buf = requests.get("http://freegeoip.net/json")
latitude = ip_buf.json()["latitude"]
longitude = ip_buf.json()["longitude"]

temp_url = "https://api.forecast.io/forecast/" + forecast_api_key + '/' + str(latitude) + ',' + str(longitude) + '?units=si'
temp_buf = requests.get(temp_url)
temp = temp_buf.json()["currently"]["temperature"]
now = temp_buf.json()["currently"]["summary"]
later = temp_buf.json()["minutely"]["summary"]
future = temp_buf.json()["daily"]["summary"]
sunrise_stamp = temp_buf.json()["daily"]["data"][0]["sunriseTime"]
sunset_stamp = temp_buf.json()["daily"]["data"][0]["sunsetTime"]

sunrise_time = time.strftime("%I:%M %p", time.localtime(sunrise_stamp)).lower()
sunset_time = time.strftime("%I:%M %p", time.localtime(sunset_stamp)).lower()

weathermark_url = "http://weather.mar.cx/" + str(latitude) + ',' + str(longitude)
weathermark = requests.get(weathermark_url).text.split('\n')[7].split('>')[1].split(' ')[0]
 
sign = u'\u02DA'

print ("%0.2f%sC %s | %s | %s" % (temp, sign, weathermark, now, later)).encode('utf8', 'replace')
#print ("%0.2f%sC %s | %s | %s | %s | %s | %s" % (temp, sign, weathermark, now, later, future, sunrise_time, sunset_time)).encode('utf8', 'replace')
