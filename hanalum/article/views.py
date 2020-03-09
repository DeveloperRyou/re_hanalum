from django.shortcuts import render
from .forms import CreateArticle


# Create your views here.

def article(request):
    return render(request, 'article.html')


def write(request):
    form = CreateArticle()

    return render(request, 'write.html', {'form': form})
