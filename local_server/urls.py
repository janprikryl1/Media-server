from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('file/', views.file, name='file'),
    path('folder/', views.folder, name='folder'),

]