from django.urls import path
from LoginApp import views

app_name = 'LoginApp'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.editprofile_view, name='profile'),
]

