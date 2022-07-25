from django.forms import ModelForm
from .models import Followup

class FollowupForm(ModelForm):
  class Meta:
    model = Followup
    fields = ['date', 'interview']