from django.db import models



class Stock(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    electricrate= models.IntegerField()
    waterusage =  models.IntegerField()
    #imdbscore = models.FloatField()
    #genre = models.CharField(max_length=1000, default= True)
    #thumbnail = models.ImageField(default='default.png', blank=True)
    date= models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
