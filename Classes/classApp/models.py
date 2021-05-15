from django.db import models


# Create your models here.
# Created a class for my Admin page with attributes to fill.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=65, null=False)
    course_number = models.IntegerField( null=False)
    instructor = models.CharField(max_length=65, null=False)
    duration = models.FloatField(max_length=50, null=False)

    object = models.Manager()

    def __str__(self):
        return self.title