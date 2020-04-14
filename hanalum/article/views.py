from django.shortcuts import render
from .forms import ArticleCreationForm
from .forms import CommentForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .models import Comment
"""from .models import Like"""
from board.models import Board


# 디버깅용 ip get code
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

"""@login_required"""
def article(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    form = CommentForm()
    ip = get_client_ip(request)
    print(ip)
    print(request.user)
    print(article_detail)

    return render(request, 'article.html', {'article': article_detail, 'form': form})


def write(request, board_id):
    if request.method == "POST":
        form = ArticleCreationForm(request.POST, request.FILES)
        if form.is_valid():
            #유저가 게시판에 등록할수 있는지 검사 필요
            board_type = get_object_or_404(Board, board_id=board_id)
            pk = form.save(pub_user=request.user, board_type=board_type)
            return redirect('/article/'+str(pk))
        else:
            return render(request, 'write.html', {'form': form})
    else:
        form = ArticleCreationForm()
        return render(request, 'write.html', {'form': form})

def article_like(request, pk):
    article = get_object_or_404(Article,pk=pk)
    user = User.objects.get(username=request.user)
    if article.likes.filter(id = user.id).exits():
        article.likes.remove(user)
    else:
        article.likes.add(user)
    return HttpResponse(str(article.total_likes()))

def like(request):
    post = Post.objects.get(pk=pk)
    value = Like.num_good
    article_like, article_like_created = article.like_set.get_or_create(user=request.user)

    if not post_like_created:
        article_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': article.like_count,
               'message': message,
               'nickname': request.user.profile.nickname}
    return HttpResponse(json.dumps(context), content_type="application/json")

def comment(request, article_id):
    if request.method == "POST":
        article = get_object_or_404(article, pk=article_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            comment.article = article
            comment.writer = request.user
            form.save()
    else:
        pass
      