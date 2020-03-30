from django.shortcuts import render
from .forms import ArticleCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from member.models import User

# Create your views here.
"""@login_required"""
def article(request):
    return render(request, 'article.html')


def write(request):
    if request.method == "POST":
        form = ArticleCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(pub_user = request.user)
            return redirect('article')
        else:
            return render(request, 'write.html', {'form': form})
    else:
        form = ArticleCreationForm()
        return render(request, 'write.html', {'form': form})


def like(request):
    user = Like.user
    value = Like.num_good
    if  value == 0:
        value = 1
    else: # 기존값이 -1 (비추천) or 1(추천)
        if value == 1: #추천을 이미 했으면서 또 할때
                value = 0 #추천취소
    return render(request, 'article.html', {'value':value})