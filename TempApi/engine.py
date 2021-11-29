import requests
import bs4

# Taking the city name as an input
def tempFunc(city):
    url = "https://google.com/search?q=weather+in+" + city

    # Sending HTTP request
    request_result = requests.get(url)

    # Pulling HTTP data from internet
    soup = bs4.BeautifulSoup(request_result.text
                             , "html.parser")

    # Finding temperature in Celsius.
    # The temperature is stored inside the class "BNeawe".
    temp = soup.find("div", class_='BNeawe').text
    print("sending...")
    return temp
