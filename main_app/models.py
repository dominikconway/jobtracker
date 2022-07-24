from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.company
