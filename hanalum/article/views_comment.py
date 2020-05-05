from .forms import CommentCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .models import Comment

@login_required
def comment_write(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            form.save(pub_user=request.user, article_type=article_detail)
    return redirect('/article/'+str(article_id))


@login_required
def comment_update(request, comment_id):
    comment_detail = get_object_or_404(Comment, pk=comment_id)
    article_detail = comment_detail.article_type
    if request.method == "POST":
        form = CommentCreationForm(request.POST, instance=comment_detail)
        if request.user == comment_detail.pub_user:
            form.save(pub_user=request.user, article_type=article_detail)
    return redirect('/article/'+str(article_detail.pk))


@login_required
def comment_delete(request, comment_id):
    comment_detail = get_object_or_404(Comment, pk=comment_id)
    article_id = comment_detail.article_type.pk
    if request.user == comment_detail.pub_user:
        comment_detail.delete()

    return redirect('/article/'+str(article_id))
