import html

from urllib.request import urlopen, Request

ACCU_URL = 'https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 61.0) Gecko/20100101 Firefox61/0', 'Host': 'www.google.com'}

accu_request = Request(ACCU_URL, headers=headers)
time = 500
accu_page = urlopen(accu_request, timeout=time,).read()
accu_page = str(accu_page)

ACCU_TEMP_TAG = '<span class="large-temp">'
accu_temp_tag_size = len(ACCU_TEMP_TAG)
accu_temp_tag_index = accu_page.find(ACCU_TEMP_TAG)
accu_temp_value_start = accu_temp_tag_index + accu_temp_tag_size
accu_temp = ''
for char in accu_page[accu_temp_value_start:]:
    if char != '<':
        accu_temp += char
    else:
        break

ACCU_WIND_TAG = '<span class="cond">'
accu_wind_tag_size = len(ACCU_WIND_TAG)
accu_wind_tag_index = accu_page.find(ACCU_WIND_TAG)
accu_wind_value_start = accu_wind_tag_index + accu_wind_tag_size
accu_wind = ''
for char in accu_page[accu_wind_value_start:]:
    if char != '<':
        accu_wind += char
    else:
        break
print('AccuWeather: \n')
print(f'Temperature: {accu_temp} \n')
print(f'Wind: {html.unescape(accu_wind)} \n')
