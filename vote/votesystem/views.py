from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VoteForm, VoteSessionCreateForm
from .models import *
from django.views.generic import (
    ListView,
    DetailView,
)


class VoteListView(LoginRequiredMixin, ListView):
    model = VoteSession
    queryset = VoteSession.objects.all()
    template_name = 'list.html'


class VoteDetailView(LoginRequiredMixin, DetailView):
    model = VoteSession
    template_name = 'detail.html'


class Vote(View):
    def get(self, request, pk):
        form = VoteForm()
        return render(request, "vote.html", locals())

    def post(self, request, pk):
        form = VoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.voter = request.user
            form.session = VoteSession.objects.get(id=pk)
            form.save()
            redirect("/votesystem")
        return redirect("/account/login")


class CreateVoteSession(View):
    def get(self, request):
        form = VoteSessionCreateForm()
        return render(request, "create.html", locals())

    def post(self, request):
        user = request.user
        form = VoteSessionCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.organizer = user
            form.save()
            redirect("/votesystem")
        return render(request, "create.html", locals())
# Create your views here.
