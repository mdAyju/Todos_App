from django.urls import path
from app import views


urlpatterns=[ 
    path('',views.show,name='show'),
    path('add/',views.Register.as_view(),name='enter'),
    path('remove/',views.remove,name='remove'),
    path('edit/<int:pk>',views.Edit.as_view(),name='edit')
]

