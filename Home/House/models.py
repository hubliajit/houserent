from django.db import models

class House(models.Model):
    Name= models.CharField(max_length=100)
    Rentamount =models.IntegerField()
    Electricityrate=models.FloatField(max_length=1000)
    Perlitreuse =models.FloatField(max_length=1000)
    Timestamp =models.DateTimeField(auto_now=True,auto_now_add=False)
    updatedtime=models.DateTimeField(auto_now_add=False,auto_now=True)
    Escaltionpercent = models.IntegerField(default=5)

    def __str__(self):
        return self.Name


