from django.urls import path
from profile_app import views

app_name = 'profile_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('create_profile/', views.CreateProfile.as_view(), name='create_profile')
]

