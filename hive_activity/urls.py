from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='hive_activity_home'),
    path('index/', views.menu, name='hive_activity_home'),
    path('menu/', views.menu, name='hive_activity_home'),
    path('add/', views.add, name='add_hive_activity'),
    path('reference/', views.reference, name='hive_activity_reference'),

]
