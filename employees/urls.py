from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_name, name='create_name'),
    path('read/', views.read_names, name='read_names'),
    path('update/<int:id>/', views.update_name, name='update_name'),
    path('delete/<int:id>/', views.delete_name, name='delete_name'),
]
