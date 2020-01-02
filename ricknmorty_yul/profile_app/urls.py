from django.urls import path
from profile_app import views

app_name = 'profile_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/add_avatar', views.ProfileView.as_view(), name='add_avatar'),
    path('profile/', views.main_profile_view, name='profile')
]

