from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),  # ← تم تصحيح path والاستيراد
    path('', include("projects.urls")),
    path('admin/', admin.site.urls),
]