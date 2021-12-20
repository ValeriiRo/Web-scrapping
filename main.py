import requests
import bs4

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_d=1636900326; _ym_uid=1636900326599702034; _ga=GA1.2.198907196.1636900326; fl=ru; hl=ru; _gid=GA1.2.1441938967.1640004143; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1',
'Host': 'habr.com',
'If-None-Match': 'W/"36c59-8YDuVJVZXQ0rLbIWXxd1k8AbC0g"',
'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.940 Yowser/2.5 Safari/537.36'
}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    if KEYWORDS & hubs:
        datetime = article.find(class_='tm-article-snippet__datetime-published')
        title = article.find('a', class_='tm-article-snippet__title-link')
        span_title = title.find('span').text
        href = title['href']
        link = 'https://habr.com' + href

        print(f'Время размещения статьи: {datetime.text} \nЗаголовок: {span_title} \nСсылка на статью:{link}\n')