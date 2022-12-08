from django.shortcuts import render
from .models import missingPerson


def indexPageView(request):
    return render(request, 'homepages/index.html')


def HomePageView(request):
    return render(request, 'homepages/homepage.html')


def searchPageView(request):
    
    try:
        person_name = request.GET['person_name']
        missing_people = missingPerson.objects.filter(person_id=person_name)
    except:
        missing_people= missingPerson.objects.all()

    context ={
        'missing_people': missing_people
    }

    return render(request, 'homepages/search.html', context)


def addpersonPageView(request):
    return render(request, 'homepages/addperson.html')
