from django.urls import path, include
from . import views

app_name = 'calculator'
urlpatterns = [
    path('calculator/<int:num1>/<int:num2>/', views.calculator),
]
