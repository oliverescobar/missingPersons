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

    def __str__(self):
        return (self.full_name)

    # return the full name of the people
    @property  # attribute contained within the object for e/ class to grab 1st and last name
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super(missingPerson, self).save()

    class Meta:
        db_table = 'people'
