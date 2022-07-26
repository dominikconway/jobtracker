from django.forms import ModelForm
from .models import Followup, Tech_Stack

class FollowupForm(ModelForm):
  class Meta:
    model = Followup
    fields = ['date', 'interview']
  
class Tech_Stack_Form(ModelForm):
  class Meta:
    model = Tech_Stack
    fields = ['skill', 'level']