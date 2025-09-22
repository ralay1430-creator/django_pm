from django import forms
from .models import Project, Task

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "status", "category"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["description", "is_completed"]
