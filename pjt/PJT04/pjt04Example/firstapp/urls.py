from django.urls import path
from . import views
# from 다른앱 import views as views2


urlpatterns = [
    path('', views.index),
    path('example/', views.example)
]
