from django.contrib import admin
from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ["Name","Rentamount","Perlitreuse","Electricityrate","Timestamp","updatedtime","Escaltionpercent"]
    list_display_links = ["Name","Rentamount","Perlitreuse","Electricityrate","Timestamp","updatedtime","Escaltionpercent"]
    list_filter = ["Timestamp","updatedtime"]
    search_fields = ["Name"]
    #list_editable = ["Name","Rentamount","Perlitreuse","Electricityrate","Timestamp","updatedtime","Escaltionpercent"]

    class Meta:
         model = House





admin.site.register(House,HouseAdmin)