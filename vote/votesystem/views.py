from django.shortcuts import render, redirect
from django.views import View
from .forms import VoteForm, VoteSessionCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from django.views.generic import (
    ListView,
    DetailView,
)


class VoteListView(ListView):
    model = VoteSession
    queryset = VoteSession.objects.all()
    template_name = 'list.html'


class VoteDetailView(DetailView):
    model = VoteSession
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canvote'] = False
        if self.request.user.is_authenticated:
            session = VoteSession.objects.get(id=self.kwargs['pk'])
            canvote = IsUserCanVote(session, self.request.user) and session.IsSessionCanVote()
            context['canvote'] = canvote
        return context


class Vote(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        form = VoteForm()
        return render(request, "vote.html", locals())

    @method_decorator(login_required)
    def post(self, request, pk):
        form = VoteForm(request.POST)
        if form.is_valid():
            session = VoteSession.objects.get(id=pk)
            form = form.save(commit=False)
            form.voter = request.user
            form.session = session

            if IsUserCanVote(form.session, request.user) and form.session.IsSessionCanVote():
                Agree = form.is_agree
                if Agree:
                    session.agree +=1
                else:
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
            return redirect("/votesystem")
        return redirect("/votesystem")
# Create your views here.


def IsUserCanVote(session, user):
    queryset = VoteRecord.objects.filter(session=session)
    if queryset:
        for voteform in queryset:
            if voteform.voter == user:  # 代表已經對這個session進行過投票
                return False
    return True
