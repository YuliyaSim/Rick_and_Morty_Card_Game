from django.urls import path
from card_app import views

app_name = 'card_app'
urlpatterns = [
    path('homepage/', views.home_page, name='homepage'),
    ]