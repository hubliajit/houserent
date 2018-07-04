from django.db.models import Q
from django.shortcuts import render
from datetime import datetime,timedelta
from django.db.models import Sum,Avg
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializer import StockSerializer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render
from datetime import datetime, timedelta, date


class StockList(APIView):



    def get(self,request):
        #stocks= Stock.objects.filter(date__range=["2018-06-04", "2018-07-04"])
        stocks=Stock.objects.filter(date__year='2018',
                            date__month='07')
        Stock.objects.aggregate(Sum('electricrate'))
        serilaizer = StockSerializer(stocks,many=True)
        return Response(serilaizer.data)

class Stocklist(APIView):
     def get(self,request):
         sum= Stock.objects.all().aggregate(Sum('electricrate'))
         return Response(sum)

class avgwateruse(APIView):
     def get(self,request):
         avg= Stock.objects.all().aggregate(Avg('waterusage'))
         return Response(avg)
