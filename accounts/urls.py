from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
]