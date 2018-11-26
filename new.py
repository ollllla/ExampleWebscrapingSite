from urllib.request import urlopen, Request

ACCU_URL = "https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561"

headers = {'User agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

accu_request = Request(ACCU_URL, headers=headers)
#time = 50
accu_page = urlopen(accu_request, timeout=50).read()
print(accu_page)

