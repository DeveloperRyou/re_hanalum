import json
from django.shortcuts import render
from .forms import ArticleCreationForm
from .forms import CommentCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime
from .models import Article
from board.models import Board
from django.http import HttpResponse


@login_required
def article(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    comment_form = CommentCreationForm()

    # user가 추천을 눌렀는지 검사
    try:
        article_detail.like_set.get(user=request.user)
        user_liked = 1
    except:
        user_liked = 0

    # user가 비추천을 눌렀는지 검사
    try:
        article_detail.dislike_set.get(user=request.user)
        user_disliked = 1
    except:
        user_disliked = 0

    response = render(request, 'article.html', {'article': article_detail, 'comment_form': comment_form,
                                                'user_liked': user_liked, 'user_disliked': user_disliked})

    # 조회수 증가 코드
    cookie_name = 'watched'
    tomorrow = datetime.datetime.replace(datetime.datetime.now(), hour=23, minute=59, second=0)
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(article_id) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{article_id}', expires=expires)
            article_detail.num_view = article_detail.num_view + 1
            article_detail.save()
    else:
        response.set_cookie(cookie_name, article_id, expires=expires)
        article_detail.num_view = article_detail.num_view + 1
        article_detail.save()

    return response


@login_required
def article_write(request, board_id):
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


@login_required
def article_update(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)

    if request.user == article_detail.pub_user:
        if request.method == "POST":
            form = ArticleCreationForm(request.POST, request.FILES, instance=article_detail)
            if form.is_valid():
                #유저가 게시판에 등록할수 있는지 검사 필요
                board_type = article_detail.board_type
                pk = form.save(pub_user=request.user, board_type=board_type)
                return redirect('/article/'+str(pk))
            else:
                return render(request, 'write.html', {'form': form})
        else:
            form = ArticleCreationForm(instance=article_detail)
            return render(request, 'write.html', {'form': form})
    else:
        return redirect('/article/' + str(article_detail.pk))

@login_required
def article_delete(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    board_id = article_detail.board_type.board_id
    if request.user == article_detail.pub_user:
        article_detail.delete()

    return redirect('/board/'+board_id)


@login_required
def article_like(request): #게시글 추천
    pk = request.POST.get('pk', None)
    article_info = get_object_or_404(Article, pk=pk)
    is_failed = 0

    try:
        article_info.dislike_set.get(user=request.user)  # 비추천 되어 있는지 검사
        message = "이미 비추천한 게시글입니다."
        is_failed = 1
    except:
        article_like_get, article_like_created = article_info.like_set.get_or_create(user=request.user)

        if not article_like_created:
            article_like_get.delete()
            message = "추천 취소"
        else:
            message = "추천"

    context = {'like_count':article_info.like_count,
               'message': message, 'is_failed': is_failed}
    return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
def article_dislike(request): #게시글 비추천
    pk = request.POST.get('pk', None)
    article_info = get_object_or_404(Article, pk=pk)
    is_failed = 0

    try:
        article_info.like_set.get(user=request.user) # 추천 되어 있는지 검사
        message = "이미 추천한 게시글입니다."
        is_failed = 1
    except:
        article_dislike_get, article_dislike_created = article_info.dislike_set.get_or_create(user=request.user)

        if not article_dislike_created:
            article_dislike_get.delete()
            message = "비추천 취소"
        else:
            message = "비추천"

    context = {'dislike_count':article_info.dislike_count,
               'message': message, 'is_failed': is_failed}

    return HttpResponse(json.dumps(context), content_type="application/json")
