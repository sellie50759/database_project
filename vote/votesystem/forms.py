from django import forms
from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class VoteForm(ModelForm):
    class Meta:
        model = VoteRecord
        fields = ["is_agree"]
        labels = {"is_agree": "投票"}


class VoteSessionCreateForm(ModelForm):
    class Meta:
        model = VoteSession
        fields = ["title","start_time","end_time","description"]
        widgets = {
            'start_time': DateInput(),
            'end_time': DateInput(),
        }