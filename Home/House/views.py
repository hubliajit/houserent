from django.db.models import Q, ExpressionWrapper,F
from django.db.models import Sum,Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import House
from .serializer import HouseSerializer
from django.shortcuts import render
from datetime import datetime, timedelta, date

class HouseList(APIView):

    def get(self, request):
        total_rent = House.objects.aggregate(Sum('Rentamount'))['datetime.month']
        num= House.objects.count()
        average_rent = total_rent / num
        total_use = House.objects.aggregate(Sum('Electricityrate'))['datetime.month']
        perunit= House.objects.count()
        average_unit = total_use / perunit
        total_litres = House.objects.aggregate(Sum('Perlitreuse'))['datetime.month']
        perlitre = House.objects.count()
        average_flow = total_litres/ perlitre

        return Response(total_rent,average_unit,average_flow)
