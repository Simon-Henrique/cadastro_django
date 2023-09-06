from app_cad_users import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.listagem, name='listagem_users'),
    path('lista/',views.lista,name='lista'),
]
