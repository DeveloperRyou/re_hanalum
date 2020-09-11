from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

# class Weather:
#     present_date = None
#     present_temp = None
#     present_state = None
#     present_compare = None
#     present_air = None

#     future_date = None
#     future_temp = None
#     future_state = None
#     future_percentage = None

#     def __init__(self):
#         html = urlopen("https://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=02480350")
#         bs = BeautifulSoup(html,"html.parser")

#         text = bs.select('div.w_now2 div.fl>em')[0].text.strip()
#         present_temp = ''
#         for ch in text:
#             if ch.isdigit():
#                 present_temp += ch
#         present_state = bs.select('div.w_now2 div.fl>em>strong')[0].text
#         try:
#             present_compare = int(float(bs.select('div.w_now2 div.fl>p>span.temp>strong')[0].text))
#         except:
#             present_compare = 0
#         present_air = bs.select('div.w_now2 div.fl>p>a>span>em')[0].text

#         future_temp = int(float(bs.select('li.nm>span')[2].text))
#         text = bs.select('li.info')[2].text
#         future_state = ''
#         for ch in text:
#             if ch == '강':
#                 break
#             future_state += ch
#         future_percentage = bs.select('li.info>span')[2].text

#         self.present_date = datetime.datetime.now()
#         self.present_temp = present_temp
#         self.present_state = present_state
#         self.present_compare = present_compare
#         self.present_air = present_air

#         self.future_date = self.present_date + datetime.timedelta(days=1)
#         self.future_temp = future_temp
#         self.future_state = future_state
#         self.future_percentage = future_percentage

def weather_parser():
    return None
    # return Weather()