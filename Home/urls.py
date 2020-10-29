from . import views
from django.urls import path

urlpatterns = [
    path('', views.travel, name='travel'),
    path('Register/', views.Register, name='Register'),
   ]