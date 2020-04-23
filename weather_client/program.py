import requests
import bs4
import collections

WeatherReport = collections.namedtuple("WeatherReport", "city,temp")


def main():
    print_header()
    country = input("What is the country code do you want the weather for (mx)? ")
    city = input("What is the city code do you want the weather for (monterrey)? ")

    html = get_html_from_web(country, city)

    weather_values = None
    if html:
        weather_feedback = get_weather_from_html(html)
    # display the forecast
    print("{} is {}".format(weather_feedback.city, weather_feedback.temp))


def get_html_from_web(country_code, city_code):
    url = "https://www.wunderground.com/weather/{}/{}".format(country_code, city_code)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ""


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    city = soup.find('h1').find("span").get_text()
    temperature = soup.find(class_="wu-value").get_text()
    return WeatherReport(city=city, temp=temperature)


def print_header():
    print("-----------------------------------------")
    print("           WEATHER CLIENT")
    print("-----------------------------------------")
    print()


if __name__ == "__main__":
    main()
