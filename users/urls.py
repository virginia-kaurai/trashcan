from django.urls import path,include




from . import views
from django.contrib.auth import views as auth_views
urlpatterns =[
    path('' , views.index, name='index'),
    path('registration/' , views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]