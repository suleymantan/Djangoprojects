from django.contrib import admin
from django.urls import path
from articles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.create_article, name='create_article'),
    path("read-article/<str:slug>",views.read_article,name="read-article"),
    path("comment/<str:slug>",views.comment,name="comment"),
    path("update/<int:id>",views.article_update,name="update"),
    path("delete/<int:id>",views.article_delete,name="delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
