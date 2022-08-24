import time

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

from parser.adsresult import AdsResult


def get_soup(page):
    url = f'https://www.list.am/category/54/{page}'
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'lxml')


class AdsParser:

    def get_ads_from_page(self, page):
        try:
            soup = get_soup(page)

            first_div_dl = soup.find('div', class_='dl')
            all_first_href_a = first_div_dl.find_all('a')
            second_div_dl = soup.find('div', class_='dl').find_next('div', class_='dl')
            all_second_href_a = second_div_dl.find_all('a')
            all_second_href_a = all_second_href_a[:-7]
            all_href_a = all_first_href_a + all_second_href_a

            results = {}

            for item in all_href_a:

                ads_id = item.get('href')[6:]
                link = 'https://www.list.am/ru' + item.get('href')
                title = item.find_next('div').find('div').get_text()
                cost = ""
                about = ""
                if item.find_next('div', class_='p') is not None:
                    cost = item.find_next('div', class_='p').get_text()
                if item.find_next('div', class_='at') is not None:
                    about = item.find_next('div', class_='at').get_text()
                category = item.find_next('div', class_='c').get_text()

                results[ads_id] = (AdsResult(ads_id, link, title, cost, about, category))

            return results
        except (Exception, AttributeError) as error:
            print(error)
            return {}

    def get_ads_from_pages(self, from_page, to_page):
        result = {}
        for page in range(from_page, to_page):
            ads = self.get_ads_from_page(page)
            for i, key in enumerate(ads):
                result[key] = ads.get(key)
            # time.sleep(0.5)
            # print("Ads copied:", len(ads), sep=" ")
        return result

