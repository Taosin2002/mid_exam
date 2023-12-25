from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    #  path('',views.home,name='home'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    # path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
]