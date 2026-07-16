from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World")


class HelloWorld(View):
    def get(self, request):
        return HttpResponse("hello india")


def home(request):
    form = ReservationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("success")
    return render(request, 'index.html', {'form': form})
