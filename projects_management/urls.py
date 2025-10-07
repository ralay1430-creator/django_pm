from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.utils.translation import gettext as _

admin.site.site_header = _("Projects Management")
admin.site.site_title = _("Projects Management")

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),  # ← تم تصحيح path والاستيراد
    path('', include("projects.urls")),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
]