from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VoteForm, VoteSessionCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
    @method_decorator(login_required)
    def get(self, request, pk):
        form = VoteForm()
        return render(request, "vote.html", locals())

    @method_decorator(login_required)
    def post(self, request, pk):
        form = VoteForm(request.POST)
        if form.is_valid():
            isvote = False
            session = VoteSession.objects.get(id=pk)
            form = form.save(commit=False)
            form.voter = request.user
            form.session = session
            queryset = VoteRecord.objects.filter(session=form.session)
            if queryset:
                for voteform in queryset:
                    if voteform.voter == request.user: #代表已經對這個session進行過投票
                        isvote=True
                        break
            if isvote:
                pass
            else:
                Agree = form.is_agree
                if Agree:
                    session.agree +=1
                else :
                    session.disagree+=1
                session.total+=1
                session.save()
                form.save()
            detail = "/votesystem/detail/" + str(pk)
            return redirect(detail)
        return redirect("/account/login")


class CreateVoteSession(View):
    @method_decorator(login_required)
    def get(self, request):
        form = VoteSessionCreateForm()
        return render(request, "create.html", locals())

    @method_decorator(login_required)
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
