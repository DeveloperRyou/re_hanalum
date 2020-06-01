from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Board
from article.models import Article
from member.models import User

# Create your views here.
PAGE_SIZE = 10
def board(request, board_id, page=1):
    page_start = (page-1) * PAGE_SIZE
    board_detail = get_object_or_404(Board, board_id=board_id)
    board_count = Article.objects.filter(board_type=board_detail).count()

    articles = None

    # 검색기능
    if request.method == "POST":
        search_select = request.POST.get('search_select', None)
        search_content = request.POST.get('search_content', None)
        if search_select == "title":
            articles = Article.objects.filter(board_type=board_detail, title__icontains=search_content)
        if search_select == "content":
            articles = Article.objects.filter(board_type=board_detail, content__icontains=search_content)
        if search_select == "writer":
            search_user = None
            try:
                search_user = User.objects.get(nickname=search_content)
            except:
                pass
            articles = Article.objects.filter(board_type=board_detail, pub_user=search_user)
        if search_select == "article":
            articles = Article.objects.filter(board_type=board_detail, title__icontains=search_content) | \
                       Article.objects.filter(board_type=board_detail, content__icontains=search_content)
    else:
        articles = Article.objects.filter(board_type=board_detail)

    articles = articles.order_by('-created_at')[page_start:page_start+PAGE_SIZE]

    return render(request, 'board.html', {'board': board_detail, 'board_id': board_id, 'articles': articles,
                                          'board_count': board_count//10+1, 'start': (page-1)//10*10,
                                          'mobile_start': (page-1)//5*5, 'page': page})
