from django.shortcuts import render


def index(request):
    return render(request, "index.html", locals())
# Create your views here.