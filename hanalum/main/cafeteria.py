from urllib.request import urlopen
from bs4 import BeautifulSoup
from _datetime import datetime


class Cafeteria:
    title = None
    menu = []

    def __init__(self, title, menu):
        self.title = title
        self.menu = menu


def cafeteria_parser():
    now_datetime = datetime.now()
    now_str_datetime = now_datetime.strftime('%Y.%m.%d')
    html = urlopen("http://hanmin.hs.kr/?act=lunch.main2&month=" + now_str_datetime)
    bs = BeautifulSoup(html, "html.parser")

    cafeteria_list = [None, None, None]
    title_list = ["조식", "중식", "석식"]
    try:
        menus = bs.select('div.menuName span')
        # 조, 중, 석식
        for i in range(3):
            menu = menus[i].text.split()
            cafeteria_object = Cafeteria(title_list[i], menu)
            cafeteria_list[i] = cafeteria_object
    except:
        pass

    return cafeteria_list
