from .forms import CommentCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .models import Comment

@login_required
def comment_write(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    form = CommentCreationForm(request.POST)
    if form.is_valid():
        form.save(pub_user=request.user, article_type=article_detail)
    return redirect('/article/'+str(article_id))


@login_required
def comment_delete(request, comment_id):
    comment_detail = get_object_or_404(Comment, pk=comment_id)
    article_id = comment_detail.article.pk
    if request.user == comment_detail.writer:
        comment_detail.delete()

    return redirect('/article/'+str(article_id))
