from django import forms
from .models import Task,Client,Project,Attachment,Industry



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

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'description',
                  'active','industry',
                  'email','phone',
                  'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['client', 'name',
                  'status', 'start_date',
                  'end_date']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['task', 'file', 'created_by']
        widgets = {
            'task': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'create_by': forms.Select(attrs={'class': 'form-control','type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(AttachmentForm, self).__init__(*args, **kwargs)

class IndustryForm(forms.ModelForm):

    class Meta:
        model = Industry
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(IndustryForm, self).__init__(*args, **kwargs)

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'assegnee',
                  'reporter', 'deadlineDate',
                  'created_by', 'last_modified_by']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'assegnee': forms.Select(attrs={'class': 'form-control'}),
            'reporter': forms.Select(attrs={'class': 'form-control'}),
            'deadlineDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'last_modified_by': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(EditTaskForm, self).__init__(*args, **kwargs)
        self.fields['last_modified_by'].required = False


class EditAttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['task', 'file', 'created_by']
        widgets = {
            'task': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'create_by': forms.Select(attrs={'class': 'form-control','type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditAttachmentForm, self).__init__(*args, **kwargs)


class EditIndustryForm(forms.ModelForm):

    class Meta:
        model = Industry
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditIndustryForm, self).__init__(*args, **kwargs)

class EditClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'description',
                  'active','industry',
                  'email','phone',
                  'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(EditClientForm, self).__init__(*args, **kwargs)

class EditProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['client', 'name',
                  'status', 'start_date',
                  'end_date']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProjectForm, self).__init__(*args, **kwargs)