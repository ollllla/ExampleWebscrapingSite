import html

from urllib.request import urlopen, Request

RP5_URL = 'http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D1%83_%D0%9B%D1%8C%D0%B2%D0%BE%D0%B2%D1%96,_%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C'

headers = {'User agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;)'}

rp5_request = Request(RP5_URL, headers=headers)
rp5_page = urlopen(rp5_request).read()
rp5_content = rp5_page.decode('utf-8')

WINFO_CONTAINER_TAG = '<div id="ArchTemp">'
RP5_TEMP_TAG = '<span class="t_0" style="display: block;">'

rp5_temp_tag = rp5_content.find(RP5_TEMP_TAG, rp5_content.find(WINFO_CONTAINER_TAG ))

rp5_temp_tag_size = len(RP5_TEMP_TAG)
rp5_temp_value_start = rp5_temp_tag + rp5_temp_tag_size

rp5_temp = ''
for char in rp5_content[rp5_temp_value_start:]:
    if char != '<':
        rp5_temp += char
    else:
        break

WINFO_CONTAINER_TAG = '<div class="ArchiveTempFeeling">'
RP5_WIND_TAG = '<span class="t_0" style="display: block;">'

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
