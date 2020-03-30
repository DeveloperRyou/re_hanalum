from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Board

# Create your views here.
def board(request, board_id):
    board_detail = get_object_or_404(Board, board_id=board_id)
    return render(request, 'board.html', {'board': board_detail})
