import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def settings(url_):
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    response = requests.get(url_, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def moscow_kamin_scr():
    soup = settings('https://moscow.kamin.ru/skidkiakcii/')
    moscow_kamin_list = []

    news_block = soup.find_all('div', class_='newsblock')
    for block in news_block:
        date_start = block.find('span', {'class': 'dateofnews'}).get_text(strip=True).replace('\xa0', ' ')
        date_finish = block.find('span', {'class': 'end_dateofnews'}).get_text(strip=True).replace('\xa0', ' ')
        name = block.find('div', {'class': 'newsfromdatemarg'}).get_text(strip=True)
        description = block.find('div', {'class': 'newsfromdatemarg'}).get_text(strip=True)

        text = date_start + ' ' + date_finish + ' ' + name + ' ' + description
        link = 'https://moscow.kamin.ru' + block.find('div', {'class': 'newsfromdatemarg'}).a['href']

        moscow_kamin_list.append([text, link])

    return moscow_kamin_list


def flammen_gmbh_scr():
    soup = settings('https://flammen-gmbh.ru/news/')
    flammen_gmbh_list = []

    news_block = soup.find_all('div', class_='news-card')
    for block in news_block:
        date_ = block.find('span', {'class': 'main-news-date'}).get_text(strip=True)
        description_1 = block.find('h3', {'class': 'main-news-title'}).get_text(strip=True)
        description_2 = block.find('p', {'class': 'main-news-text'}).get_text(strip=True)

        text = date_ + ' ' + description_1 + ' ' + description_2
        link = 'https://flammen-gmbh.ru' + block.find('div', {'class': 'main-news-item'}).a['href']

        flammen_gmbh_list.append([text, link])

    return flammen_gmbh_list


def schmid_scr():
    soup = settings('https://schmid.ru/action/')
    schmid_list = []

    news_block = soup.find_all('div', class_='block1200')
    for block in news_block:
        name = block.find('h1', {'class': 'mw600'}).get_text(strip=True)
        description = block.find('div', {'class': 'news-list'}).get_text(strip=True)

        text = name + ' ' + description
        link = 'https://schmid.ru' + block.find('div', {'class': 'news-list'}).a['href']

        schmid_list.append([text, link])

    return schmid_list


def schiedel_settings():
    cookies = {
        'pyCNQE': 'REmNbFTthcDSQiaqsBjZkHgCvOJryG',
        'REmNbFTthcDSQiaqsBjZkHgCvOJryG': 'b2e63c18bcea45f023878bd888c6b782-1701285686-1701285665',
        'pyCNQE_hits': '8',
        '_ym_uid': '1701285689787098273',
        '_ym_d': '1701285689',
        'tmr_lvid': '65d943ac64f83952418e7279be67e177',
        'tmr_lvidTS': '1701285688848',
        '_ym_isad': '2',
        '_ymab_param': '6ojOLb48Em_OG9RVPSx3zL09qwyKtymos43G9Krm7hv2Eh-LE1o9ThJ-sgUCg90oVR9Y5UOyooovyobrbtK3j4BJ5VU',
        'tmr_detect': '0^%^7C1701288053676',
        'ab_id': '5f2049823a2eb104352692bb5078df148d55e3a9',
        '_ym_visorc': 'w',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://schiedel.com.ru/news/',
        'Connection': 'keep-alive',
        # 'Cookie': 'pyCNQE=REmNbFTthcDSQiaqsBjZkHgCvOJryG; REmNbFTthcDSQiaqsBjZkHgCvOJryG=b2e63c18bcea45f023878bd888c6b782-1701285686-1701285665; pyCNQE_hits=8; _ym_uid=1701285689787098273; _ym_d=1701285689; tmr_lvid=65d943ac64f83952418e7279be67e177; tmr_lvidTS=1701285688848; _ym_isad=2; _ymab_param=6ojOLb48Em_OG9RVPSx3zL09qwyKtymos43G9Krm7hv2Eh-LE1o9ThJ-sgUCg90oVR9Y5UOyooovyobrbtK3j4BJ5VU; tmr_detect=0^%^7C1701288053676; ab_id=5f2049823a2eb104352692bb5078df148d55e3a9; _ym_visorc=w',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get('https://schiedel.com.ru/news/', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def schiedel_scr():
    soup = schiedel_settings()
    schiedel_list = []

    news_block = soup.find_all('article', class_='mk-blog-modern-item')
    for block in news_block:
        text = block.find('h3', {'class': 'the-title'}).get_text(strip=True)
        link = block.find('h3', {'class': 'the-title'}).a['href']

        schiedel_list.append([text, link])

    return schiedel_list


def belfortkamin_scr():
    soup = settings('https://belfortkamin.ru/news/')
    belfortkamin_list = []

    news_block = soup.find_all('div', class_='post')
    for block in news_block:
        name = block.find('h3').get_text(strip=True)
        text = name + ' ' + block.find('div', {'class': 'text'}).get_text(strip=True)

        link = block.find('h3').a['href']

        belfortkamin_list.append([text, link])

    return belfortkamin_list


def lit_kom_scr():
    soup = settings('https://lit-kom.ru/news/')
    lit_kom_list = []

    news_block = soup.find_all('div', class_='ty-blog__item')
    for block in news_block:
        date = block.find('div', class_='ty-blog__date').get_text(strip=True)
        name = block.find('h2', class_='ty-blog__post-title').get_text(strip=True)
        description_list = block.find_all('p')
        description = ' '.join(desc.get_text(strip=True) for desc in description_list)

        text = date + ' ' + name + ' ' + description
        link = block.find('div', class_='ty-blog__read-more').a['href']

        lit_kom_list.append([text, link])

    return lit_kom_list


def ecokamin_scr():
    soup = settings('https://www.ecokamin.ru/novosti/')
    ecokamin_list = []

    html_news_block = soup.find('div', class_='items row')
    news_block = html_news_block.find_all('div', class_='col-md-12')
    for block in news_block:
        date = block.find('div', class_='period').get_text(strip=True)
        name = block.find('a', class_='dark-color').get_text(strip=True)
        html_description = block.find('div', class_='previewtext')
        description = html_description.get_text(strip=True) if html_description else ''

        text = date + ' ' + name + ' ' + description
        link = 'https://www.ecokamin.ru' + block.find('div', class_='link-block-more').a['href']

        ecokamin_list.append([text, link])

    return ecokamin_list


def kamin_sklad_scr():
    soup = settings('https://kamin-sklad.ru/news/')
    kamin_sklad_list = []

    news_block = soup.find_all('div', class_='item clearfix item_block')
    for block in news_block:
        date = block.find('div', class_='date_small').get_text(strip=True)
        name = block.find('div', class_='item-title').get_text(strip=True)
        html_desc = block.find('div', class_='preview-text').get_text(strip=True)

        text = date + ' ' + name + ' ' + html_desc
        link = 'https://kamin-sklad.ru' + block.find('div', class_='item-title').a['href']

        kamin_sklad_list.append([text, link])

    return kamin_sklad_list


def easysteam_scr():
    soup = settings('https://easysteam.ru/news')
    easysteam_list = []

    news_block = soup.find_all('div', class_='col-12 col-md-6 col-lg-4 mb-4 mb-sm-5')
    for block in news_block:
        text = block.find('div', class_='news-card__description').get_text(strip=True)
        link = block.a['href']

        easysteam_list.append([text, link])

    return easysteam_list


def prometall_scr():
    soup = settings('https://prometall.ru/actions')
    prometall_list = []

    news_block = soup.find_all('div', class_='t686')
    for block in news_block:
        name = block.find('div', class_='t-card__title t-title t-title_xxs').get_text(strip=True)
        description = block.find('div', class_='t-card__descr t-descr t-descr_xs').get_text(strip=True)

        text = name + ' ' + description
        link = 'https://prometall.ru/' + block.find('div', class_='t-card__title t-title t-title_xxs').a['href']

        prometall_list.append([text, link])

    return prometall_list


def pkferrum_settings():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://pkferrum.ru',
        'Connection': 'keep-alive',
        'Referer': 'https://pkferrum.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        'https://feeds.tildacdn.com/api/getfeed/?feeduid=109303744201&recid=652384235&c=1701296979748&size=&slice=1'
        '&sort^%^5Bdate^%^5D=desc&filters^%^5Bdate^%^5D=&getparts=true',
        headers=headers,
    )

    return response.json()


def pkferrum_scr():
    pkferrum_list = []

    response = pkferrum_settings()
    posts_raw = response.get('posts', {})

    if posts_raw and len(posts_raw) > 0:
        for post in posts_raw:
            date = post.get('date', None)
            name = post.get('title', None)
            description = post.get('descr', None)

            text = date + ' ' + name + ' ' + description
            link = post.get('url', None)

            pkferrum_list.append([text, link])

    return pkferrum_list


if __name__ == "__main__":
    pkferrum_scr()
