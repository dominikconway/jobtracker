from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['company', 'role', 'salary']

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
      return super().form_valid(form)

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['company', 'role', 'salary']

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/jobs/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
@login_required
def jobs_index(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/index.html', {'jobs': jobs })

@login_required
def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    stack_job_doesnt_have = Tech_Stack.objects.exclude(id__in = job.tech_stack.all().values_list('id'))
    followup_form = FollowupForm()
    return render(request, 'jobs/detail.html', {
        'job': job, 'followup_form': followup_form,
        'tech_stack': stack_job_doesnt_have
    })

@login_required
def add_followup(request, job_id):
    form = FollowupForm(request.POST)
    if form.is_valid():
        new_followup = form.save(commit=False)
        new_followup.job_id = job_id
        new_followup.save()
    return redirect('detail', job_id=job_id)

@login_required
def assoc_tech_stack(request, job_id, tech_stack_id):
  # Note that you can pass a toy's id instead of the whole object
  Job.objects.get(id=job_id).tech_stack.add(tech_stack_id)
  return redirect('detail', job_id=job_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class Tech_stackList(LoginRequiredMixin, ListView):
  model = Tech_Stack

class Tech_stackDetail(LoginRequiredMixin, DetailView):
  model = Tech_Stack

class Tech_stackCreate(LoginRequiredMixin, CreateView):
  model = Tech_Stack
  fields = '__all__'

class Tech_stackUpdate(LoginRequiredMixin, UpdateView):
  model = Tech_Stack
  fields = ['skill', 'level']

class Tech_stackDelete(LoginRequiredMixin, DeleteView):
  model = Tech_Stack
  success_url = '/techstack/'

