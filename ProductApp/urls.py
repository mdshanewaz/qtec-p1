from django.urls import path
from ProductApp import views

app_name = 'ProductApp'

urlpatterns = [
    path('', views.home_view, name='home'),
]

