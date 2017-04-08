from django.shortcuts import render, HttpResponse
from django.utils import timezone
import pytz
from . import forms
import logging


# Create your views here.

data = []
logger = logging.getLogger('logs')


def form(request):
    now = timezone.now()
    if len(data) == 0:
        with open('../d04/logs', 'r') as f:
            for line in f:
                data.append(line.replace("\n", ""))
    if (request.method == 'POST'):
        form = forms.MyForm(request.POST)
        if form.is_valid():
            data.append(form.cleaned_data['name'] + " {0}:{1} {2}/{3}/{4}".format(int(now.hour)+2, now.minute, now.day, now.month, now.year))
            with open("../d04/logs", "a") as myfile:
                myfile.write(data[-1] + "\n")

    else:
        form = forms.MyForm()
    return render(request, "ex02/form.html", {'form' : form, 'data' : data})
