from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    a = "<h1>hi hello i am sathish</h1>"
    return HttpResponse(a)


def index2(request):
    b = "<h1>This is about page</h1>"
    return HttpResponse(b)

def index3(request):
    return render(request, "index.html", {})
