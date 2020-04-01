"""
템블릿 코드 작성시 사용할 변수 커스터마이징 용 파일
sidebar : 사이드바 메뉴설정용 변수 정의
"""

from django.conf import settings
from main.models import Sidebar_category
from main.models import Sidebar_unit

def sidebar(request):
    """
    DB 참조후 사이드바 변수 정의
    """
    category = Sidebar_category.objects.order_by('menu_sort')
    unit = Sidebar_unit.objects.order_by('menu_sort')
    return {'category': category, 'unit': unit}