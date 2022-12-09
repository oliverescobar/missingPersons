from django.shortcuts import render
from home.models import missingPerson


def indexPageView(request):
    return render(request, 'homepages/index.html')


def HomePageView(request):
    return render(request, 'homepages/homepage.html')


def searchPageView(request):
    return render(request, 'homepages/search.html')


def addpersonPageView(request):
    if request.method == 'POST':
        missingperson = missingPerson()  # this is the missing persons' class we created
        missingperson.date_missing = request.POST['date_missing']
        missingperson.last_name = request.POST['last_name']
        missingperson.first_name = request.POST['first_name']
        missingperson.age_at_missing = request.POST['age_at_missing']
        missingperson.city = request.POST['city']
        missingperson.state = request.POST['state']
        missingperson.gender = request.POST['gender']
        missingperson.race = request.POST['race']

        missingperson.save()

        return HomePageView(request)
    else:
        return render(request, 'homepages/addperson.html')
