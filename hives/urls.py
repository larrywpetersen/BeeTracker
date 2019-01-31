from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='hives_home'),
    path('index/', views.menu, name='hives_home'),
    path('menu/', views.menu, name='hives_home'),
    path('add/', views.add, name='add_hive'),
    path('list/', views.list, name='list_hives'),

]
