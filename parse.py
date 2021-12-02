from bs4 import BeautifulSoup
import requests

INSTITUTE = {
    'http://brs.gstou.ru/Student/ViborGruppi?Facultet=1',
    'http://brs.gstou.ru/Student/ViborGruppi?Facultet=2',
    'http://brs.gstou.ru/Student/ViborGruppi?Facultet=1007',
    'http://brs.gstou.ru/Student/ViborGruppi?Facultet=3',
    'http://brs.gstou.ru/Student/ViborGruppi?Facultet=1006'
}

URL = 'http://brs.gstou.ru/' #Задается ссылка сайта
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 'accept': '*/*'} # Какая-то штука, чтобы нас не приняли за бота

def parse(): #Получается HTML-страницу, с которой дальше работаем
    html = get_html(URL)
    get_content(html.text) #Передаем полученный DOM для работы в след.метод

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r


def get_content(html_content): #Превращаем DOM в удобный для чтения формат
    soup = BeautifulSoup(html_content, 'html.parser') #Передаем наш DOM бибилиотеке bs4 фиг пойми зачем
    items = soup.find_all('a', class_='fonSsilki') #Здесь ситуация аналогичная
    get_page(items, soup)

def get_page(items, soup):
    for item in items: #Ну здесь более менее понятно, перебираем наш DOM, ищем там все файлы с ссылкой и забираем ссылки оттуда
        print(item.get('href'))
        if item in soup.select('a[href],a[data-href],a[href][data-href]'):
            print(True)
    
for institute in INSTITUTE:
    parse(institute) #наш парсер запускается десь


