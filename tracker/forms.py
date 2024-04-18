from .models import Project
from django.forms import ModelForm
from django import forms

class ProjectForm(ModelForm):
    field_order = ['title', 'remarks', 'link', 'status',]

    class Meta:
        model = Project
        fields = {'title', 'remarks', 'link', 'status',}

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = ''
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'What do you want to call this?'

        self.fields['remarks'].label = ''
        self.fields['remarks'].widget.attrs['class'] = 'form-control'
        self.fields['remarks'].widget.attrs['placeholder'] = 'Tell us more about this idea'

        self.fields['link'].label = ''
        self.fields['link'].widget.attrs['class'] = 'form-control'
        self.fields['link'].widget.attrs['placeholder'] = 'Where can we see this?'