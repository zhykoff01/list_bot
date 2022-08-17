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


def get_top_item():
    first_div_dl = get_soup().find('div', class_='dl')
    all_href_a = first_div_dl.find_all('a')

    for item in all_href_a:
        result_list['href'].append('https://www.list.am/ru' + item.get('href'))
        result_list['title'].append(item.find_next('div').find('div').get_text())
        result_list['cost'].append(item.find_next('div', class_='p').get_text())
        result_list['about'].append(item.find_next('div', class_='at').get_text())
        result_list['category'].append(item.find_next('div', class_='c').get_text())
    return result_list


def get_item():
    second_div_dl = get_soup().find('div', class_='dl').find_next('div', class_='dl')
    all_href_a = second_div_dl.find_all('a')

    for item in all_href_a:
        result_list['href'].append('https://www.list.am/ru' + item.get('href'))
        result_list['title'].append(item.find_next('div').find('div').get_text())
        result_list['cost'].append(item.find_next('div', class_='p').get_text())
        result_list['about'].append(item.find_next('div', class_='at').get_text())
        result_list['category'].append(item.find_next('div', class_='c').get_text())
    return result_list


# print(get_top_item())
print(get_item())
