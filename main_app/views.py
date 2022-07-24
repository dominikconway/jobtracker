from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Job

# class Job:
#     def __init__(self, company, role, salary):
#         self.company = company
#         self.role = role
#         self.salary = salary

# jobs = [
#     Job('Tesla', 'Software Engineer', 200000),
#     Job('Microsoft', 'Systems Engineer', 125000),
#     Job('Meta', 'React Engineer', 99000)
# ]

class JobCreate(CreateView):
    model = Job
    fields = '__all__'

class JobUpdate(UpdateView):
    model = Job
    fields = "__all__"

class JobDelete(DeleteView):
    model = Job
    success_url = '/jobs/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs })

def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/detail.html', {'job': job})

