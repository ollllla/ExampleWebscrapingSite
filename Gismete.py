import html

from urllib.request import urlopen, Request

RP5_URL = 'https://www.gismeteo.ua/ua/weather-lviv-14412/'

headers = {'User agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;)'}

rp5_request = Request(RP5_URL, headers=headers)
rp5_page = urlopen(rp5_request).read()
rp5_content = rp5_page.decode('utf-8')

WINFO_CONTAINER_TAG = '<h2 class="typeM hover">'
RP5_TEMP_TAG = '<div class="temp">'

rp5_temp_tag = rp5_content.find(RP5_TEMP_TAG, rp5_content.find(WINFO_CONTAINER_TAG ))

rp5_temp_tag_size = len(RP5_TEMP_TAG)
rp5_temp_value_start = rp5_temp_tag + rp5_temp_tag_size

rp5_temp = ''
for char in rp5_content[rp5_temp_value_start:]:
    if char != '<':
        rp5_temp += char
    else:
        break

WINFO_CONTAINER_TAG = '<div class="wicon wind">'
RP5_WIND_TAG = '<dd class="value m_wind ms">'

rp5_wind_tag = rp5_content.find(RP5_TEMP_TAG, rp5_content.find(WINFO_CONTAINER_TAG ))

rp5_wind_tag_size = len(RP5_WIND_TAG)
rp5_wind_value_start = rp5_wind_tag + rp5_wind_tag_size

rp5_wind = ''
for char in rp5_content[rp5_wind_value_start:]:
    if char != '<':
        rp5_wind += char
    else:
        break
print('RP5: \n')
print(f'Temperature: {html.unescape(rp5_temp)} \n')
print(f'TempFeeling: {html.unescape(rp5_wind)} \n')
