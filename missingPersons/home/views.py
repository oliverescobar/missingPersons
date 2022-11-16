from django.shortcuts import render
from django.http import HttpResponse


def indexPageView(request):
    return HttpResponse("This is the index page")

def firstPageView(request):
    return HttpResponse('this is the first page!')

def indexbootstrapPageView(request):
    return render(request, 'homepages/indexbootstrap.html')