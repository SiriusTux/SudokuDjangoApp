from django.shortcuts import render, redirect
from .utility import removeDot, grid_values
from .sudoku import solve
from .models import Grid
from django import forms
from random import choice

# Create your views here.
empty = '.................................................................................'

class LevelForm(forms.Form):
    level = forms.CharField(max_length=256)

def start(request):
    if request.method == 'POST':
        level_form = LevelForm(request.POST)
        if level_form.is_valid():
            level = level_form.cleaned_data.get('level').lower()
            queryset = Grid.objects.filter(difficulty=level)
            random_choice = choice([grid.id for grid in queryset])
            return redirect('sudoku:to_solve', id=random_choice)
    empty_grid = removeDot(grid_values(empty))
    difficulty_count = {'easy': len(Grid.objects.filter(difficulty='easy')), 
                        'medium': len(Grid.objects.filter(difficulty='medium')), 
                        'hard': len(Grid.objects.filter(difficulty='hard'))}
    return render(request, 'sudoku/start.html', {
        'grid': empty_grid, 
        'difficulty': difficulty_count
    })


def to_solve(request, id):
    grid = Grid.objects.get(pk=id)
    display_grid = removeDot(grid_values(grid.grid))
    return render(request, 'sudoku/solve.html', {
        'id': grid.id,
        'grid': display_grid,
        'description': grid
    })


def solved(request, id):
    to_solve = Grid.objects.get(pk=id).grid
    solved = solve(to_solve)
    return render(request, 'sudoku/solved.html', {
        'grid': solved
    })