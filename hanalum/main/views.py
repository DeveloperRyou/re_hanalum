from django.shortcuts import render
from .youtube import youtube_parser
# Create your views here.

def main(request):
    # 유튜브 크롤링
    youtube_list = youtube_parser()
    return render(request, 'main.html', {'youtube_list':youtube_list})