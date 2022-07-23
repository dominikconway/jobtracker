from django.shortcuts import render
from django.http import HttpResponse

class Job:
    def __init__(self, company, role, salary):
        self.company = company
        self.role = role
        self.salary = salary

jobs = [
    Job('Tesla', 'Software Engineer', 200000),
    Job('Microsoft', 'Systems Engineer', 125000),
    Job('Meta', 'React Engineer', 99000)
]

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
    return render(request, 'jobs/index.html', {'jobs': jobs })
