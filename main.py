import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

def get_headers():
    headers = Headers(browser='safari', os='mac')
    return headers.generate()

response = requests.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=get_headers())
hh_main = response.text

soup = BeautifulSoup(hh_main, features='html.parser')

article_list = soup.find_all('div', class_='serp-item')
# print(len(article_list))

parsed = []
for article in article_list:
    salary_ = article.find(attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
    name_ = article.find(attrs={'data-qa': 'serp-item__title'})
    city_ = article.find(attrs={'data-qa': 'vacancy-serp__vacancy-address'})
    href_ = article.find(attrs={'data-qa': 'href'})
    # print(article)

salary_parsed = salary_.text
name_parsed = name_.text
city_parsed = city_.text
print(salary_parsed, name_parsed, city_parsed)

# with open('hh.json', 'w', encoding='utf-8') as f:
#     json.dump(article, f)
