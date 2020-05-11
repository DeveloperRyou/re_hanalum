from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from .youtube import youtube_parser
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
    # 유튜브 크롤링
    youtube_list = youtube_parser()
    return render(request, 'main.html', {'board_petition':board_petition, 'board_free':board_free, 'youtube_list':youtube_list})