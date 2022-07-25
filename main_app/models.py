from datetime import date
from django.db import models
from django.urls import reverse

INTERVIEWS = (
    ('I', 'Interview'),
    ('E', 'Email'),
    ('C', 'CallBack')
)

class Job(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id':self.id})
    
    def got_followup(self):
        return len( self.followup_set.filter(date=date.today()) )

class Followup(models.Model):
    date = models.DateField('follow-up date')
    interview = models.CharField(
        max_length=1,
        choices=INTERVIEWS,
        default=INTERVIEWS[0][0]
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_interview_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']