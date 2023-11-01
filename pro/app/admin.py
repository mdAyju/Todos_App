from django.contrib import admin
from app.models import DataModel


@admin.register(DataModel)
class DataAdmin(admin.ModelAdmin):
    list_display=['id','name','locality','mobile','state','zipcode']
