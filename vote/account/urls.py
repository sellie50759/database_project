from django.urls import path
from . import views

urlpatterns = [
    path("create", views.UserCreateView.as_view(), name="create"),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout')
]