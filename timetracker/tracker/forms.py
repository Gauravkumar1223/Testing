# forms.py
from django import forms
from .models import TimeEntry

class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ['hours', 'description', 'day_type']
        widgets = {
            'hours': forms.NumberInput(attrs={'step': '0.5', 'min': '0', 'max': '24'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }