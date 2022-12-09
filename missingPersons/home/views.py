from django.shortcuts import render
from home.models import missingPerson


def indexPageView(request):
    return render(request, 'homepages/index.html')


def HomePageView(request):
    return render(request, 'homepages/homepage.html')


def searchPageView(request):
<<<<<<< HEAD

    return render(request, 'homepages/search.html')
=======
    try:
        missing_person = request.GET['missing_person']
        person = missingPerson.objects.filter(missing_person=missing_person)
    except:
        person = missingPerson.objects.all()

    context = {
    }

    return render(request, 'homepages/search.html', context)
    # sFirst = request.GET['first_name']
    # return render(request, 'homepages/search.html', context)
    
>>>>>>> 47309e81d07110e7bd0fe74951df3ce2a6222b77


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
