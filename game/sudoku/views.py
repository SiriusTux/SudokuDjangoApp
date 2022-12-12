from django.shortcuts import render
from django.http import HttpResponse
from . import utility
from .models import Grid

# Create your views here.
empty = '.................................................................................'

def start(request):
    empty_grid = utility.removeDot(utility.grid_values(empty))

    difficulty_count = {'easy': len(Grid.objects.filter(difficulty='easy')), 
                        'medium': len(Grid.objects.filter(difficulty='medium')), 
                        'hard': len(Grid.objects.filter(difficulty='hard'))}
    return render(request, "sudoku/start.html", {
        "grid": empty_grid, 
        "difficulty": difficulty_count
    })

