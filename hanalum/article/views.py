from django.shortcuts import render
from .forms import ArticleCreationForm


# Create your views here.

def article(request):
    return render(request, 'article.html')


def write(request):
    form = ArticleCreationForm()

    return render(request, 'write.html', {'form': form})
