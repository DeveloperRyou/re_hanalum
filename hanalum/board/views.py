from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Board
from article.models import Article

# Create your views here.
def board(request, board_id):
    board_detail = get_object_or_404(Board, board_id=board_id)
    articles = Article.objects.filter(board_type=board_detail)
    return render(request, 'board.html', {'board': board_detail, 'board_id': board_id, 'articles': articles})
