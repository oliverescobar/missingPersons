from django.http import HttpResponse

def indexPageView(request):
    return HttpResponse("This is the index page")
