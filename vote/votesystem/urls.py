from django.urls import path
from . import views

urlpatterns = [
    path("", views.VoteListView.as_view(), name="session_list"),
    path("vote/<int:pk>", views.Vote.as_view(), name="vote"),
    path('detail/<int:pk>', views.VoteDetailView.as_view(), name='session_detail'),
    path('create', views.CreateVoteSession.as_view(), name='session_create'),
]