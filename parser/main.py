import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_soup():
    page = 1
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    url = f'https://www.list.am/category/54/{page}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


class Results:
    soup = get_soup()
    first_div_dl = soup.find('div', class_='dl')
    all_first_href_a = first_div_dl.find_all('a')
    second_div_dl = soup.find('div', class_='dl').find_next('div', class_='dl')
    all_second_href_a = second_div_dl.find_all('a')
    all_second_href_a = all_second_href_a[:-7]
    all_href_a = all_first_href_a + all_second_href_a

    def __init__(self, href, title, cost, about, category):
        self.href = href
        self.title = title
        self.cost = cost
        self.about = about
        self.category = category

    def get_data(self):

        for item in self.all_href_a:
            self.href = 'https://www.list.am/ru' + item.get('href')
            self.title = item.find_next('div').find('div').get_text()
            if item.find_next('div', class_='p') is not None:
                self.cost = item.find_next('div', class_='p').get_text()
            else:
                self.cost = "''"
            if item.find_next('div', class_='at') is not None:
                self.about = item.find_next('div', class_='at').get_text()
            else:
                self.about = "''"
            self.category = item.find_next('div', class_='c').get_text()
            print(self.href, self.title, self.cost, self.about, self.category)

