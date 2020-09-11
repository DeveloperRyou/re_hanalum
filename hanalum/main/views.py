from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from .youtube import youtube_parser
from .weather import weather_parser
from .cafeteria import cafeteria_parser
from article.models import Article
from board.models import Board
# Create your views here.

ARTICLE_NUM = 3


def main(request):
    datetime_now = datetime.now(tz=timezone.utc)
    datetime_past = datetime_now + timedelta(days=-7)
    # 청원게시판
    board_petition_type = Board.objects.get(board_id='petition')
    board_petition = Article.objects.filter(board_type=board_petition_type, created_at__range=[datetime_past, datetime_now])
    board_petition = board_petition.order_by('like_user_set')[:ARTICLE_NUM]
    # 자유게시판
    board_free_type = Board.objects.get(board_id='free')
    board_free = Article.objects.filter(board_type=board_free_type, created_at__range=[datetime_past, datetime_now])
    board_free = board_free.order_by('like_user_set')[:ARTICLE_NUM]
    # 날씨 크롤링, 날씨객체 반환
    # weather = weather_parser()
    # 급식 크롤링, 3개의 급식객체가 들어있는 리스트 반환
    cafeteria_list = cafeteria_parser()
    # 유튜브 크롤링, 3개의 유튜브객체가 들어있는 리스트 반환
    youtube_list = youtube_parser()
    return render(request, 'main.html', {'board_petition': board_petition, 'board_free': board_free, 'cafeteria_list': cafeteria_list, 'youtube_list': youtube_list})