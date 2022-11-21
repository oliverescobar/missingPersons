from django.db import models

# Create your models here.

class missingPerson(models.Model):
    date_missing = models.DateField((""), auto_now=False, auto_now_add=False)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)

    class Meta:
        db_table = 'people'
