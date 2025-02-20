
from django.contrib import admin
from django.urls import path
from home.views import home,updateTask,delete,completed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name = "home"),
    path("update/<int:id>",updateTask,name="update"),
    path("delete/<int:id>", delete, name = "delete"),
    path("copmleted/<int:id>", completed, name = "completed"),
]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
