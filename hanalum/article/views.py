from django.shortcuts import render
from .forms import ArticleCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from member.models import User

# Create your views here.
@login_required
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
