from django import forms
from coach.models import Coach

class CreateCoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('firstName', 'lastName', 'email', 'phone', 'location', 'hobby')

