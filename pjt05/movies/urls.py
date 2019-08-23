from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
    path('<int:pk_num>/', views.select),
    path('<int:pk_num>/edit/', views.edit),
    path('<int:pk_num>/update/', views.update),
    path('<int:pk_num>/delete/', views.delete),
]
