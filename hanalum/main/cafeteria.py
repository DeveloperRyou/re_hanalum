from urllib.request import urlopen
from bs4 import BeautifulSoup
from _datetime import datetime


class Cafeteria:
    title = None
    id = None
    menu = []

    def __init__(self, title, id, menu):
        self.title = title
        self.id = id
        self.menu = menu


def cafeteria_parser():
    now_datetime = datetime.now()
    now_str_datetime = now_datetime.strftime('%Y.%m.%d')
    html = urlopen("http://hanmin.hs.kr/?act=lunch.main2&month=" + now_str_datetime)
    bs = BeautifulSoup(html, "html.parser")

    cafeteria_list = [None, None, None]

    title_list = ["조식", "중식", "석식"]
    id_list = ["breakfast", "lunch", "dinner"]
    menu_list = [None, None, None]
    try:
        menus = bs.select('div.menuName span')
        for i in range(3):
            menu_list[i] = menus[i].text.split()
    except:
        for i in range(3):
            menu_list[i] = ["급식 정보가 없습니다"]

    # 조, 중, 석식
    for i in range(3):
        cafeteria_object = Cafeteria(title_list[i], id_list[i], menu_list[i])
        cafeteria_list[i] = cafeteria_object

    return cafeteria_list
