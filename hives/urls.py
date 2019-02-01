from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='hives_home'),
    path('index/', views.menu, name='hives_home'),
    path('menu/', views.menu, name='hives_home'),
    path('add/', views.add, name='add_hive'),
    path('list/', views.list, name='list_hives'),
    path('edit/', views.edit, name='edit_hive'),
    path('delete/', views.delete, name='delete_hive'),


    # api paths

    path('get_hive_simple_list/', views.get_hive_simple_list, name='get_hive_simple_list'),
    path('get_hive_full_list/', views.get_hive_full_list, name='get_hive_full_list'),
    path('is_hive_label_unique/', views.is_hive_label_unique, name='is_hive_label_unique'),

]
