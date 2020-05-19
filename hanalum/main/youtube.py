from urllib.request import urlopen
from bs4 import BeautifulSoup


class Youtube:
    title = None
    href = None
    img_src = None

    def __init__(self, title, href, img_src):
        self.title = title
        self.href = href
        self.img_src = img_src


def youtube_parser():
    html = urlopen("https://www.youtube.com/channel/UCreDKYaD9FakIAFEop8EddA/videos")
    bs = BeautifulSoup(html,"html.parser")

    a_tag = bs.select('div.yt-lockup-content a')
    img_tag = bs.select('div.yt-lockup-thumbnail img')

    youtube_list = [None, None, None]
    try:
        for i in range(3):
            youtube_object = Youtube(a_tag[i]['title'], a_tag[i]['href'], img_tag[i]['src'])
            youtube_list[i] = youtube_object
    except:
        pass
    return youtube_list
