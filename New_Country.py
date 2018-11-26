import html
import re

from urllib.request import urlopen, Request

RP5_URL = 'http://example.webscraping.com'
headers = {'User agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;)'}

rp5_request = Request(RP5_URL, headers=headers)
rp5_page = urlopen(rp5_request).read()
rp5_content = rp5_page.decode('utf-8')

WINFO_CONTAINER_TAG = '<div id="results">'
RP5_TEMP_TAG = './/a[text() = 'Afghanistan']'

rp5_temp_tag = rp5_content.find(RP5_TEMP_TAG, rp5_content.find(WINFO_CONTAINER_TAG ))

rp5_temp_tag_size = len(RP5_TEMP_TAG)
rp5_temp_value_start = rp5_temp_tag + rp5_temp_tag_size

rp5_temp = ''
for char in rp5_content[rp5_temp_value_start:]:
    if char != '<':
        rp5_temp += char
    else:
        break

print('RP5: \n')
print(f'Temperature: {re.unescape(rp5_temp)} \n')


