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


result_list = {'href': [], 'title': [], 'cost': [], 'about': [], 'category': []}


def get_item():
    soup = get_soup()
    first_div_dl = soup.find('div', class_='dl')
    all_first_href_a = first_div_dl.find_all('a')
    second_div_dl = soup.find('div', class_='dl').find_next('div', class_='dl')
    all_second_href_a = second_div_dl.find_all('a')
    all_second_href_a = all_second_href_a[:-7]
    all_href_a = all_first_href_a + all_second_href_a

    for item in all_href_a:
        result_list['href'].append('https://www.list.am/ru' + item.get('href'))
        result_list['title'].append(item.find_next('div').find('div').get_text())
        if item.find_next('div', class_='p') is not None:
            result_list['cost'].append(item.find_next('div', class_='p').get_text())
        else:
            result_list['cost'].append('')
        if item.find_next('div', class_='at') is not None:
            result_list['about'].append(item.find_next('div', class_='at').get_text())
        else:
            result_list['about'].append('')
        result_list['category'].append(item.find_next('div', class_='c').get_text())
    return result_list


print(get_item())
