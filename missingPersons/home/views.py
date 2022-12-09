from django.shortcuts import render
from .models import missingPerson


def indexPageView(request):
    return render(request, 'homepages/index.html')


def HomePageView(request):
    db_missing = missingPerson.objects.all()

    context = {
        "missingPerson":  db_missing
    }

    return render(request, 'homepages/homepage.html', context)


def searchPageView(request):
    # NO FREAKING CLUE WHAT THE HECK HAPPENED. WE TRIED SO BEAUTIFULLY HARD FOR HOURS BUT SADLY COULD NOT LINK THE FUN LITTLE WEBSITE TO SHOW THE SEARCH RESULTS. IT PROBABLY WORKS THOUGH...
    try:
        first_name = request.GET['first_name']
        db_missing = missingPerson.objects.filter(first_name=first_name)
    except:
        db_missing = missingPerson.objects.all()

    context = {
        'missingPerson': db_missing
    }

    return render(request, 'homepages/search.html', context)
    # sFirst = request.GET['first_name']
    # return render(request, 'homepages/search.html', context)


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
