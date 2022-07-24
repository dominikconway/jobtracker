from django.db import models
from django.urls import reverse

class Job(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id':self.id})