from django.urls import path

from . import views

app_name = 'Homepage'
urlpatterns = [
    path('', views.index, name="index"),
    path('webhook/', views.webhook, name="webhook"),
    path('dbupdate/', views.DBUpdate, name="DB"),
    path('result/', views.result, name= 'result'),
    path('stream/',views.livefe, name='stream')
]
