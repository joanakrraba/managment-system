from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'assegnee',
                  'reporter', 'deadlineDate',
                  'created_by', 'last_modified_by',
                  'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'assegnee': forms.Select(attrs={'class': 'form-control'}),
            'reporter': forms.Select(attrs={'class': 'form-control'}),
            'deadlineDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'last_modified_by': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['last_modified_by'].required = False
