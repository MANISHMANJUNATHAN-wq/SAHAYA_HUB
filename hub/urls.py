from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update_status, name='update_status'),
    path('login/', views.volunteer_login, name='login'),
    path('signup/', views.volunteer_signup, name='signup'),
    path('logout/', views.volunteer_logout, name='logout'),
]