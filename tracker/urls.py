from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('viewproject/<project_id>/', views.viewproject, name='viewproject'),
    path('delproject/<project_id>/', views.delproject, name='delproject'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]