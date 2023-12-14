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
    news_list = []

    news_block = soup.find_all('div', class_='newsblock')
    for block in news_block:
        date_start = block.find('span', {'class': 'dateofnews'}).get_text(strip=True).replace('\xa0', ' ')
        date_finish = block.find('span', {'class': 'end_dateofnews'}).get_text(strip=True).replace('\xa0', ' ')
        name = block.find('div', {'class': 'newsfromdatemarg'}).get_text(strip=True)
        description = block.find('div', {'class': 'newsfromdatemarg'}).get_text(strip=True)

        text = date_start + ' ' + date_finish + ' ' + name + ' ' + description
        link = 'https://moscow.kamin.ru' + block.find('div', {'class': 'newsfromdatemarg'}).a['href']

        news_list.append([text, link])

    return news_list


def flammen_gmbh_scr():
    soup = settings('https://flammen-gmbh.ru/news/')
    news_list = []

    news_block = soup.find_all('div', class_='news-card')
    for block in news_block:
        date_ = block.find('span', {'class': 'main-news-date'}).get_text(strip=True)
        description_1 = block.find('h3', {'class': 'main-news-title'}).get_text(strip=True)
        description_2 = block.find('p', {'class': 'main-news-text'}).get_text(strip=True)

        text = date_ + ' ' + description_1 + ' ' + description_2
        link = 'https://flammen-gmbh.ru' + block.find('div', {'class': 'main-news-item'}).a['href']

        news_list.append([text, link])

    return news_list


def schmid_scr():
    soup = settings('https://schmid.ru/action/')
    news_list = []

    news_block = soup.find_all('div', class_='block1200')
    for block in news_block:
        name = block.find('h1', {'class': 'mw600'}).get_text(strip=True)
        description = block.find('div', {'class': 'news-list'}).get_text(strip=True)

        text = name + ' ' + description
        link = 'https://schmid.ru' + block.find('div', {'class': 'news-list'}).a['href']

        news_list.append([text, link])

    return news_list


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
    news_list = []

    news_block = soup.find_all('article', class_='mk-blog-modern-item')
    for block in news_block:
        text = block.find('h3', {'class': 'the-title'}).get_text(strip=True)
        link = block.find('h3', {'class': 'the-title'}).a['href']

        news_list.append([text, link])

    return news_list


def belfortkamin_scr():
    soup = settings('https://belfortkamin.ru/news/')
    news_list = []

    news_block = soup.find_all('div', class_='post')
    for block in news_block:
        name = block.find('h3').get_text(strip=True)
        text = name + ' ' + block.find('div', {'class': 'text'}).get_text(strip=True)

        link = block.find('h3').a['href']

        news_list.append([text, link])

    return news_list


def lit_kom_scr():
    soup = settings('https://lit-kom.ru/news/')
    news_list = []

    news_block = soup.find_all('div', class_='ty-blog__item')
    for block in news_block:
        date = block.find('div', class_='ty-blog__date').get_text(strip=True)
        name = block.find('h2', class_='ty-blog__post-title').get_text(strip=True)
        description_list = block.find_all('p')
        description = ' '.join(desc.get_text(strip=True) for desc in description_list)

        text = date + ' ' + name + ' ' + description
        link = block.find('div', class_='ty-blog__read-more').a['href']

        news_list.append([text, link])

    return news_list


def ecokamin_scr():
    soup = settings('https://www.ecokamin.ru/novosti/')
    news_list = []

    html_news_block = soup.find('div', class_='items row')
    news_block = html_news_block.find_all('div', class_='col-md-12')
    for block in news_block:
        date = block.find('div', class_='period').get_text(strip=True)
        name = block.find('a', class_='dark-color').get_text(strip=True)
        html_description = block.find('div', class_='previewtext')
        description = html_description.get_text(strip=True) if html_description else ''

        text = date + ' ' + name + ' ' + description
        link = 'https://www.ecokamin.ru' + block.find('div', class_='link-block-more').a['href']

        news_list.append([text, link])

    return news_list


def kamin_sklad_scr():
    soup = settings('https://kamin-sklad.ru/news/')
    news_list = []

    news_block = soup.find_all('div', class_='item clearfix item_block')
    for block in news_block:
        date = block.find('div', class_='date_small').get_text(strip=True)
        name = block.find('div', class_='item-title').get_text(strip=True)
        html_desc = block.find('div', class_='preview-text').get_text(strip=True)

        text = date + ' ' + name + ' ' + html_desc
        link = 'https://kamin-sklad.ru' + block.find('div', class_='item-title').a['href']

        news_list.append([text, link])

    return news_list


def easysteam_scr():
    soup = settings('https://easysteam.ru/news')
    news_list = []

    news_block = soup.find_all('div', class_='col-12 col-md-6 col-lg-4 mb-4 mb-sm-5')
    for block in news_block:
        text = block.find('div', class_='news-card__description').get_text(strip=True)
        link = block.a['href']

        news_list.append([text, link])

    return news_list


def prometall_scr():
    soup = settings('https://prometall.ru/actions')
    news_list = []

    news_block = soup.find_all('div', class_='t686')
    for block in news_block:
        name = block.find('div', class_='t-card__title t-title t-title_xxs').get_text(strip=True)
        description = block.find('div', class_='t-card__descr t-descr t-descr_xs').get_text(strip=True)

        text = name + ' ' + description
        link = 'https://prometall.ru/' + block.find('div', class_='t-card__title t-title t-title_xxs').a['href']

        news_list.append([text, link])

    return news_list


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


def dantexgroup_scr():
    soup = settings("https://dantexgroup.ru/about/news/")
    news_list = []

    news_blocks = soup.find_all('div', class_='box')
    for block in news_blocks:
        date = block.find('span', class_='date').get_text(strip=True)
        name = block.find('h3').get_text(strip=True)
        link = 'https://dantexgroup.ru' + block.find('h3').a['href']
        description = block.find('p').get_text(strip=True)

        text = date + ' ' + name + ' ' + description

        news_list.append([text, link])
    return news_list


def t_m_f_scr():
    soup = settings("https://t-m-f.ru/company/news/")
    news_list = []

    news_blocks = soup.find_all('div', class_='item clearfix item_block')
    for block in news_blocks:
        name = block.find('div', class_='item-title').get_text(strip=True)
        link = 'https://t-m-f.ru' + block.find('div', class_='item-title').a['href']
        description = block.find('div', class_='preview-text').get_text(strip=True)

        text = name + ' ' + description

        news_list.append([text, link])
    return news_list


def kamin_scr():
    soup = settings("https://kamin.ru/skidkiakcii/")
    news_list = []

    news_blocks = soup.find_all('div', class_='newsblock')
    for block in news_blocks:
        date_start = block.find('span', class_='dateofnews').get_text(strip=True).replace('от', 'от ').replace('202', ' 202')
        date_finish = block.find('span', class_='end_dateofnews').get_text(strip=True).replace('до', 'до ').replace('202', ' 202')
        link = 'https://kamin.ru' + block.find('h3').a['href']
        description = block.find('div', class_='newsfromdatemarg').get_text(strip=True)

        text = date_start + ' ' + date_finish + ' ' + description

        news_list.append([text, link])
    return news_list


def saunaru_scr():
    soup = settings("https://saunaru.com/collection/frontpage")
    news_list = []

    news_blocks = soup.find_all('form', class_='product-preview')
    for block in news_blocks:
        description = block.find('div', class_='product-preview__title').get_text(strip=True)
        link = 'https://saunaru.com' + block.find('div', class_='product-preview__title').a['href']

        html_price = block.find('div', class_='product-preview__price')
        html_old_price = html_price.find('span', class_='product-preview__price-old')
        old_price = 'Цена до акции: ' + html_old_price.get_text(strip=True) if html_old_price else ''
        html_cur_price = html_price.find('span', class_='product-preview__price-cur')
        cur_price = 'Цена с акцией: ' + html_cur_price.get_text(strip=True) if html_cur_price else ''

        text = description + ' ' + old_price + ' ' + cur_price

        news_list.append([text, link])
    return news_list


def only_scr():
    soup = settings("https://www.only.ru/company/novosti/")
    news_list = []

    news_blocks = soup.find_all('div', class_='articles')
    for block in news_blocks:
        name = block.find('div', class_='article_item').get_text(strip=True)
        link = 'https://www.only.ru' + block.find('div', class_='article_item').a['href']
        description = block.find('div', class_='summary').get_text(strip=True)

        text = name + ' ' + description

        news_list.append([text, link])
    return news_list


def contactplus_scr():
    soup = settings("https://contactplus.ru/company/news/")
    news_list = []

    news_blocks = soup.find_all('div', class_='news-item')
    for block in news_blocks:
        day = block.find('span', class_='news-date-day').get_text(strip=True)
        month = block.find('span', class_='news-date-my').get_text(strip=True)
        description = block.find('div', class_='news-desc').get_text(strip=True)
        link = 'Нет ссылки'

        text = day + ' ' + month + '\n' + description

        news_list.append([text, link])
    return news_list


def kaminmeta_scr():
    soup = settings("https://www.kaminmeta.ru/akzii/")
    news_list = []

    news_blocks = soup.find_all('div', class_='action-item c_fix')
    for block in news_blocks:
        name = block.find('div', class_='action-item-dsc').find('a', class_='action-item-title').get_text(strip=True)
        html_date = block.find('div', class_='action-item-dsc').find('div', class_='action-item-date')
        date = html_date.get_text(strip=True) if html_date else ''
        link = 'https://www.kaminmeta.ru' + block.find('div', class_='action-item-dsc').a['href']

        text = date + '\n' + name
        news_list.append([text, link])
    return news_list


def feringer_scr():
    soup = settings("https://www.feringer.ru/aktsii/")
    news_list = []

    news_blocks = soup.find_all('div', class_='col-md-6')
    for block in news_blocks:
        date = block.find('div', class_='stocks-item__date').get_text(strip=True)
        description = block.find('div', class_='stocks-item__name').get_text(strip=True)
        link = 'https://www.feringer.ru' + block.find('div', class_='stocks-item__content').a['href']

        text = date + '\n' + description

        news_list.append([text, link])

    soup_2 = settings("https://www.feringer.ru/articles/")

    news_blocks_2 = soup_2.find_all('div', class_='article_item')
    for block_2 in news_blocks_2:
        date_2 = block_2.find('p', class_='date_articles').get_text(strip=True)
        name_2 = block_2.find('a').get_text(strip=True)
        description_2 = block_2.find('div', class_='description_article').get_text(strip=True)
        link_2 = 'https://www.feringer.ru' + block_2.a['href']

        text_2 = date_2 + '\n' + ' ' + name_2 + ' ' + description_2

        news_list.append([text_2, link_2])
    return news_list


def gefestgroup_scr():
    soup = settings("https://gefestgroup.ru/news/")
    news_list = []

    news_blocks = soup.find_all('div', class_='b-post-wrapper')
    for block in news_blocks:
        date = block.find('p', class_='font-size-xs mb-0 ml-auto text-white-70').get_text(strip=True)
        name = block.find('div', class_='b-post-name h4 text-white').get_text(strip=True)
        description = block.find('p', class_='mb-0 font-size-sm text-white').get_text(strip=True)
        link = block.a['href']

        text = date + '\n' + name + ' ' + description

        news_list.append([text, link])
    return news_list


def evrokamin_scr():
    soup = settings("https://www.evrokamin.ru/sale/")
    news_list = []

    news_blocks = soup.find('div', class_='items row').find_all('div', class_='col-md-12')
    for block in news_blocks:
        date = block.find('div', class_='period').get_text(strip=True)
        name = block.find('div', class_='title').get_text(strip=True)
        link = 'https://www.evrokamin.ru' + block.find('div', class_='title').a['href']

        text = date + '\n' + name

        news_list.append([text, link])
    return news_list


if __name__ == "__main__":
    evrokamin_scr()
