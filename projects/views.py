from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Project, Task
from .forms import ProjectCreateForm, TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project/list.html"
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user.id}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = "project/update.html"

    def test_func(self):
        return self.get_object().user_id == self.request.user.id

    def get_success_url(self):
        return reverse("project_list")


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "project/delete.html"
    success_url = reverse_lazy("project_list")

    def test_func(self):
        return self.get_object().user_id == self.request.user.id


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "project/task.html"
    http_method_names = ["post"]

    def test_func(self):
        project_id = self.kwargs.get("project_id")
        project = Project.objects.get(pk=project_id)
        return project.user_id == self.request.user.id

    def form_valid(self, form):
        project_id = self.kwargs.get("project_id")
        form.instance.project = Project.objects.get(pk=project_id)
        messages.success(self.request, "New task added")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("project_update", args=[self.object.project.id])

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def test_func(self):
        # حماية التحديث: فقط مالك المشروع يمكنه تعديل المهام
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse("project_update", args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task

    def test_func(self):
        # حماية الحذف: فقط مالك المشروع يمكنه حذف المهام
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse("project_update", args=[self.object.project.id])
