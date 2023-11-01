from django.urls import path
from app import views

urlpatterns = [
    path('',views.index),
    path('get/<int:pk>/',views.onlyOne),
    path('post/',views.post),
    path('edit/<int:pk>/',views.edit),
    path('del/<int:pk>/',views.remove),
    path('main/',views.main,name='home'),
    path('add/',views.add,name='add')
    # path('table/',views.table,name='table')
]
