from django.urls import path
from customkit import views


urlpatterns = [
    path('', views.customkit, name='customkit')    
]
