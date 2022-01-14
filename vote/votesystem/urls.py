from django.urls import path
from . import views

urlpatterns = [
    path("", views.VoteListView.as_view(), name="list"),
    path("vote/<int:pk>", views.Vote.as_view(), name="vote"),
    path('detail/<int:pk>', views.VoteDetailView.as_view(), name='detail'),
    path('create', views.CreateVoteSession.as_view(), name='create'),
]