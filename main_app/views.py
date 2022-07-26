from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Job, Tech_Stack
from .forms import FollowupForm

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
    stack_job_doesnt_have = Tech_Stack.objects.exclude(id__in = job.tech_stack.all().values_list('id'))
    followup_form = FollowupForm()
    return render(request, 'jobs/detail.html', {
        'job': job, 'followup_form': followup_form,
        'tech_stack': stack_job_doesnt_have
    })

def add_followup(request, job_id):
    form = FollowupForm(request.POST)
    if form.is_valid():
        new_followup = form.save(commit=False)
        new_followup.job_id = job_id
        new_followup.save()
    return redirect('detail', job_id=job_id)

def assoc_tech_stack(request, job_id, tech_stack_id):
  # Note that you can pass a toy's id instead of the whole object
  Job.objects.get(id=job_id).tech_stack.add(tech_stack_id)
  return redirect('detail', job_id=job_id)

class Tech_stackList(ListView):
  model = Tech_Stack

class Tech_stackDetail(DetailView):
  model = Tech_Stack

class Tech_stackCreate(CreateView):
  model = Tech_Stack
  fields = '__all__'

class Tech_stackUpdate(UpdateView):
  model = Tech_Stack
  fields = ['skill', 'level']

class Tech_stackDelete(DeleteView):
  model = Tech_Stack
  success_url = '/techstack/'

