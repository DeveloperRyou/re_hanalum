from django.shortcuts import render
from .forms import ArticleCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article


# Create your views here.
@login_required
def article(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    print(article_detail)
    return render(request, 'article.html', {'article': article_detail})


def write(request):
    if request.method == "POST":
        form = ArticleCreationForm(request.POST, request.FILES)
        if form.is_valid():
            pk = form.save(pub_user = request.user)
            return redirect('/article/'+str(pk))
        else:
            return render(request, 'write.html', {'form': form})
    else:
        form = ArticleCreationForm()
        return render(request, 'write.html', {'form': form})
