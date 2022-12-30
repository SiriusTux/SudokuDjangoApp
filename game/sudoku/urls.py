from django.urls import path

from . import views

app_name = 'sudoku'
urlpatterns = [
    path('', views.start, name='start'),
    path('to_solve/<int:id>', views.to_solve, name='to_solve'),
    path('solved/<int:id>', views.solved, name='solved')
]