from . import views

from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('tip/', views.Tip.as_view(), name='tip'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]