from django import forms
from .models import Project, Task
from django.utils.translation import gettext as _

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "status", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter project title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Enter project description"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["description", "is_completed"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Task description"}),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
