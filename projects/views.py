from django.views.generic import ListView, CreateView   # استيراد ListView و CreateView
from django.urls import reverse_lazy                   # لإنشاء رابط نجاح بعد الحفظ
from . import models                                   # استيراد ملف models
from . import forms                                    # استيراد ملف forms

# Create your views here.

class ProjectListView(ListView):             # عرض قائمة المشاريع
    model = models.Project                   # تحديد أن البيانات من موديل Project
    template_name = "project/list.html"      # القالب المستخدم للعرض


class ProjectCreateView(CreateView):         # إنشاء مشروع جديد
    model = models.Project                  
    form_class = forms.ProjectCreateForm    
    template_name = "project/create.html"    
    success_url = reverse_lazy("project_list")  
