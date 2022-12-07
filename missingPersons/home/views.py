from django.shortcuts import render


def indexPageView(request):
    return render(request, 'homepages/index.html')


def HomePageView(request):
    return render(request, 'homepages/homepage.html')


def searchPageView(request):
    return render(request, 'homepages/search.html')


def addpersonPageView(request):
    return render(request, 'homepages/addperson.html')
