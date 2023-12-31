from django.urls import path
from . import views

app_name='myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
]
