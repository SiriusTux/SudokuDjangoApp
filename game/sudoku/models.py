from django.db import models
from datetime import datetime

# Create your models here.
class Grid(models.Model):

    grid = models.CharField(max_length=81)
    difficulty = models.CharField(max_length=10, default='easy')
    source = models.CharField(max_length=255, default='Unknown')
    date = models.DateField(default=datetime.utcnow())

    def __str__(self):
        return f'Sudoku {self.id} from {self.source} date {self.date}'