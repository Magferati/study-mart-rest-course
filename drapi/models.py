from django.db import models

# Create your models here.
class Aiquest(models.Model):
    techer_name=models.CharField(max_length=25)
    course_name = models.CharField(max_length=20)
    course_time = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return self.techer_name
