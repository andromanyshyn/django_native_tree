from django import forms

from .models import *

ORDERING_CHOICES = (
    ('name', 'name'),
    ('job_title', 'job_title'),
    ('salary', 'salary'),
)


class WorkersListForm(forms.Form):
    choice = forms.ChoiceField(choices=ORDERING_CHOICES)


class WorkerUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    job_title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    salary = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control py-4'}))

    class Meta:
        model = Workers
        fields = ['name', 'job_title', 'salary', 'image']
