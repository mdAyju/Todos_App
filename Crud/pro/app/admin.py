from django.contrib import admin
from app.models import MobileModel

# Register your models here.
@admin.register(MobileModel)
class MobileAdmin(admin.ModelAdmin):
    list_display=['id','mobiles','price','ram','storage']