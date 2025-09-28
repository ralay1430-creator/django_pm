# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Project, Task
from .forms import ProjectCreateForm, TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project/list.html"
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = "project/create.html"
    success_url = reverse_lazy("project_list")  # ← الاسم مطابق للـ urls.py


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = "project/update.html"

    def get_success_url(self):
        return reverse("project_list")  # ← الرجوع لقائمة المشاريع


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "project/delete.html"
    success_url = reverse_lazy("project_list")  # ← الاسم مطابق للـ urls.py


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "project/task.html"
    http_method_names = ["post"]

    def form_valid(self, form):
        project_id = self.kwargs.get("project_id")
        form.instance.project = Project.objects.get(pk=project_id)
        messages.success(self.request, "New task added")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("project_update", args=[self.object.project.id])


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse("project_update", args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return reverse("project_update", args=[self.object.project.id])
