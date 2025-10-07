from django.contrib import admin
from django.db.models import Count
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_at', 'tasks_count']
    list_per_page = 20
    list_editable = ['status']
    list_select_related = ['category', 'user']

    def tasks_count(self, obj):
        # عدد المهام لكل مشروع
        return obj.tasks_count
    tasks_count.short_description = "Tasks"

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 20
