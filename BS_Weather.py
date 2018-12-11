import html
import argparse
import sys
from bs4 import BeautifulSoup

from urllib.request import urlopen, Request

ACCU_URL = 'https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561'
ACCU_TAGS = ('<span class="large-temp">', '<span class="cond">')


def get_request_headers():
    return {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 61.0)'}


def get_page_source(url):
    request = Request(url, headers=get_request_headers())
    page_source = urlopen(request).read()
    return page_source.decode('utf-8')


def get_tag_content(page_content, tag):
    tag_index = page_content.find(tag)
    tag_size = len(tag)
    value_start = tag_index + tag_size

    content = ''
    for c in page_content[value_start:]:
        if c != '<':
            content += c
        else:
            break
        return content


def get_weather_info(page_content):
    city_page = BeautifulSoup(page_content, 'html.parser')
    current_day_section = city_page.find('li', class_="night current first cl")

    weather_info = {}
    if current_day_section:
        current_day_url = current_day_section.find('a').attr['href']
        if current_day_url:
            current_day_page = get_page_source(current_day_url)
            if current_day_page:
                current_day = BeautifulSoup(current_day_page, 'html.parser')
                weather_details = current_day.find('div', attrs={'id': 'detail-now'})
                condition = weather_details.find('span', class_='cond')
                if condition:
                    weather_info['cond'] = condition.text
                temp = weather_details.find('span', class_='large-temp')
                if temp:
                    weather_info['temp'] = temp.text
                feal_temp = weather_details.find('span', class_='small-temp')
                if feal_temp:
                    weather_info['feal-temp'] = feal_temp.text
                wind_info = weather_details.find_all('li', class_='wind')
                if wind_info:
                    weather_info['wind'] = "".join(map(lambda t: t.text.strip(), wind_info))
    return weather_info


def produce_output(info):
    print('Accu Weather:\n')
    for key, value in info.items():
        print(f'{key}:{html.unescape(value)}')


def main(argv):
    KNOWN_COMMANDS = {'accu': 'AccuWeather', 'rp5': 'RP5'}
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Service name', nargs=1)
    params = parser.parse_args(argv)

    weather_sites = {'AccuWeather': (ACCU_URL, ACCU_TAGS)}

    if params.command:
        command = params.command[0]
        if command in KNOWN_COMMANDS:
            weather_sites = {
                KNOWN_COMMANDS[command]: weather_sites[KNOWN_COMMANDS[command]]

            }

    else:
        print("Unknown command")
        sys.exit(1)

    for name in weather_sites:
        url, tags = weather_sites[name]
        content = get_page_source(url)
        produce_output(get_weather_info(content))


if __name__ == 'main':
    main(sys.argv[1:])
