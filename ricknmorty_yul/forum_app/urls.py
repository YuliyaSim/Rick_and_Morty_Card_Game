from django.urls import path
from forum_app import views

app_name = 'forum_app'
urlpatterns = [
    path('forum/', views.forum, name='forum'),
    ]