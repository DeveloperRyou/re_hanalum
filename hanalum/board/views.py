from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Board
from article.models import Article

# Create your views here.
PAGE_SIZE = 10
def board(request, board_id, page=1):
    page_start = (page-1) * PAGE_SIZE
    board_detail = get_object_or_404(Board, board_id=board_id)
    board_count = Article.objects.filter(board_type=board_detail).count()

    articles = Article.objects.filter(board_type=board_detail).order_by('-pub_date')[page_start:page_start+PAGE_SIZE]

    return render(request, 'board.html', {'board': board_detail, 'board_id': board_id, 'articles': articles,
                                          'board_count': board_count//10+1, 'start': (page-1)//10*10,
                                          'mobile_start': (page-1)//5*5, 'page': page})
