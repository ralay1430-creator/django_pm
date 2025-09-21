from django import forms
from . import models

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ["category", "title", "description"]   # ✅ الحقول الصحيحة
        widgets = {
            "category": forms.Select(),                 # قائمة منسدلة للفئة
            "title": forms.TextInput(attrs={"class": "form-control"}),  # إدخال نص
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),  # مربع نص
        }
