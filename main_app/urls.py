from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs_index, name='index'),
    path('jobs/<int:job_id>/', views.jobs_detail, name="detail"),
    path('jobs/create', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
    path('jobs/<int:job_id>/add_followup/', views.add_followup, name='add_followup'),
    path('techstack/', views.Tech_stackList.as_view(), name='tech_stack_index'),
    path('techstack/<int:pk>/', views.Tech_stackDetail.as_view(), name='tech_stack_detail'),
    path('techstack/create/', views.Tech_stackCreate.as_view(), name='tech_stack_create'),
    path('techstack/<int:pk>/update/', views.Tech_stackUpdate.as_view(), name='tech_stack_update'),
    path('techstack/<int:pk>/delete/', views.Tech_stackDelete.as_view(), name='tech_stack_delete'),
    path('techstack/<int:job_id>/assoc_tech_stack/<int:tech_stack_id>/', views.assoc_tech_stack, name='assoc_tech_stack'),
    path('accounts/signup/', views.signup, name='signup'),
]