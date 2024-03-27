from django.urls import path 
from . import views
app_name = 'CRM'
urlpatterns = [
    path('/', views.home, name = 'home'),
    path('/login/', views.login, name = 'login'),
    path('/register/', views.register, name = 'register'),
    path('/logout/', views.logout, name = 'logout'),
    path('reset/', views.reset, name = 'reset'),
    path('setpass/<str:username>', views.setpass, name = 'setpass'),
    path('confirm/<int:key>/<str:username>', views.confirm, name = 'confirm'),
]